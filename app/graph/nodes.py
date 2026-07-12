from app.graph.state import ReviewState
from app.services.retrieval_service import retrieve_standards
from app.llm.chains import chain
from app.database.models import ReviewReport

def analyze_code_node(state: ReviewState):
    print("Analyzing code...")
    return state


def retrieve_standards_node(state: ReviewState):
    print("Retrieving standards...")

    standards = retrieve_standards(
        db=state["db"],
        code=state["code"]
    )

    retrieved_context = "\n\n".join(
        [
            f"""
Title: {item.title}
Category: {item.category}

Content:
{item.content}
"""
            for item in standards
        ]
    )

    state["standards"] = retrieved_context

    return state


def generate_review_node(state: ReviewState):
    print("Generating review...")

    result = chain.invoke(
        {
            "language": state["language"],
            "code": state["code"],
            "context": state["context"] or "",
            "standards": state["standards"]
        }
    )
    state["review_result"] = result
    return state


def save_review_node(state: ReviewState):
    print("Saving review...")

    review_data = state["review_result"]

    review = ReviewReport(
        submission_id=state["submission_id"],
        score=review_data["score"],
        summary=review_data["summary"],
        issues=review_data["issues"]
    )

    state["db"].add(review)
    state["db"].commit()
    state["db"].refresh(review)

    state["saved_review"] = review

    return state
