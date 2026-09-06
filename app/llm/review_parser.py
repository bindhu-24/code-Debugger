from langchain_core.output_parsers import JsonOutputParser

from app.schemas.review_schema import CodeReviewReport

parser = JsonOutputParser(pydantic_object=CodeReviewReport)

format_instructions = parser.get_format_instructions()