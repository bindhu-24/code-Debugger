from app.graph.state import ReviewState
from app.database.connection import SessionLocal
from app.rag.retriever import retrieve_standards as rag_retrieve_standards
from openai import OpenAI
import os
from app.database.models import ReviewReport
from app.schemas.review_schema import CodeReviewReport

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_code(state: ReviewState):
    """
    Node 1:
    Analyze the submitted code.
    """

    code = state["code"]

    analysis = f"Code received for analysis. Length: {len(code)} characters."

    return {
        "analysis": analysis
    }


def retrieve_standards(state: ReviewState):
    db = SessionLocal()

    try:
        code = state["code"]
        language = state["language"]

        standards = rag_retrieve_standards(
            db=db,
            query=code,
            language=language,
            limit=5
        )

        formatted_standards = [
            {
                "title": standard.title,
                "category": standard.category,
                "content": standard.content
            }
            for standard in standards
        ]

        return {
            "retrieved_standards": formatted_standards
        }

    finally:
        db.close()
    
def generate_review(state: ReviewState):
    """
    Node 3:
    Generate an LLM-based code review using the retrieved coding standards
    from the RAG pipeline.

    Actual LLM integration will be connected later.
    """
    code = state.get("code", "")
    language = state.get("language", "")
    analysis = state.get("analysis", "")
    standards = state.get("retrieved_standards", [])

    standards_text = "\n\n".join(
        [
            f"Title:  {standard['title']}\n"
            f"Category: {standard['category']}\n"
            f"Rule: {standard['content']}"
            for standard in standards
        ]
    )

    prompt = f"""
    You are an expert code reviewer.
    Review the following code using the coding standards retrieved from the knowledge base.
    
    CODE:
    {code}

    INITIAL ANALYSIS:
    {analysis}

    RETRIEVED CODING STANDARDS:
    {standards_text}

    Instructions:

    1. Identify bugs and potential runtime problems.
    2. Identify security vulnerabilities.
    3. Check the code against the retrieved coding standards.
    4. Identify readability and maintainability issues.
    5. Provide clear recommendations.
    6. Do not report an issue unless there is evidence in the code.
    7. Give an overall score from 0 to 100.

    Return the review in a clear structured format.
    """

    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert code reviewer."},
            {"role": "user", "content": prompt}
        ],
        response_format=CodeReviewReport,
        temperature=0
    )

    review_text = response.choices[0].message.content
    review_result = CodeReviewReport.model_validate_json(review_text) 
    return {
        "review": review_text,
        "review_result": review_result.model_dump(),
        "issues_found": len(review_result.issues) > 0
    }


def finalize_review(state: ReviewState):
    """
    Node 4:
    Finalize the review result.
    """

    review = state.get("review", "")

    return {
        "review": f"Final Review:\n{review}"
    }


def save_review(state: ReviewState):
    """
    Node 5:
    Save the structuredreview result to PostgreSQL.
    """

    db = SessionLocal()

    try:
        submission_id = state.get("submission_id")
        review_result = state.get("review_result")

        if not submission_id:
            raise ValueError("Submission ID is required to save the review.")

        if not review_result:
            raise ValueError("Review result is empty. Cannot save an empty review.")
        # Assuming you have a ReviewReport model in your database
        review_report = ReviewReport(
            submission_id=submission_id,
            score = review_result["score"],
            summary = review_result["summary"],
            issues= review_result["issues"]
        )
        db.add(review_report)
        db.commit()
        db.refresh(review_report)

        print("======== SAVE REVIEW SUCCESS ========")
        print(f"Review report saved: {review_report.id}")
        return {
            "review_report_id": review_report.id
            # "save_review" : review_report
        }
    except Exception as e:
        db.rollback()
        print("======== SAVE REVIEW ERROR ========")
        print((e))
        raise

    finally:
        db.close()

def should_finalize(state: ReviewState):
    """
    Conditional edge.

    Decide whether Node 4 should execute.
    """

    if state.get("issues_found"):
        return "finalize"

    return "end" 
