from app.graph.workflow import build_review_graph

graph = build_review_graph()

initial_state = {
    "submission_id": 1,
    "language": "python",
    "code": """
    def add_item(item, items=[]):
    items.append(item)
    return items
    """,
    "context": "Simple addition function"
}


result = graph.invoke(initial_state)


print("\n========== LANGGRAPH RESULT ==========\n")

print("Analysis:")
print(result.get("analysis"))

print("\nRetrieved Standards:")
print(result.get("retrieved_standards"))

print("\nReview:")
print(result.get("review"))

print("\nSubmission ID:")
print(result.get("submission_id"))

print("\nReview Report ID:")
print(result.get("review_report_id"))

print("\nIssues Found:")
print(result.get("issues_found"))

print("\n======================================\n")