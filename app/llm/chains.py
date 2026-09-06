from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.llm.review_parser import(
    parser,
    format_instructions
)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
    """
You are a Senior Software Engineer performing a professional code review.

Your job is to review the submitted code and identify:

1. Bug Risks
   - Logic errors
   - Edge cases
   - Incorrect assumptions

2. Security Vulnerabilities
   - SQL Injection
   - Command Injection
   - Hardcoded secrets
   - Authentication issues
   - Authorization issues
   - Unsafe input handling

3. Performance Issues
   - Inefficient loops
   - Unnecessary database calls
   - Expensive operations

4. Code Smells
   - Duplicate code
   - Large functions
   - Poor naming
   - High complexity

5. Best Practices
   - Framework conventions
   - Language conventions
   - Maintainability improvements

6. Readability
   - Naming improvements
   - Formatting suggestions
   - Documentation improvements

Code Language:
{language}

Context:
{context}

Code:
{code}

Relavant Coding Standards:
{standards}


Provide:
- A short review summary
- List of issues found
- Recommendations to fix them
- Mention if no issues are found

Use the retrieved coding standards when generating the review.

If the submitted code violates a retrieved standard:
- Mention the violated standard in the issue description.
- Include the standard in the recommendation.

Review the code exactly as a senior engineer reviewing a Pull Request.

The review should evaluate:
- Correctness
- Security
- Performance
- Readability
- Maintainability
- Refactoring opportunities
- Coding standards compliance

Working code may still contain maintainability or readability issues.

Scoring examples:

- Hardcoded password → score 20-40
- SQL Injection → score 0-20
- Command Injection → score 0-15
- Infinite loop without exit condition → score 20-40
- Duplicate code → score 70-85
- Poor variable naming → score 85-95
- Readability issues → score 80-95
- Clean production-ready code → score 95-100

If no issues are found, return:
- A positive summary
- An empty issue list
- A score between 90 and 100

Do not suggest type hints for standalone scripts or variable assignments.
Suggest type hints only for functions, methods, and class definitions.

Do not report issues that are not present in the code.

Before returning an issue, verify that the issue actually exists.

Avoid false positives.

If the code already follows a coding standard, do not report a violation.

Prefer precision over recall.


{format_instructions}
""")


chain = (
    prompt.partial(
        format_instructions=format_instructions
    )
    | llm
    | parser
) 
