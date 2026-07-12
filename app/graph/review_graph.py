from langgraph.graph import StateGraph, END
from app.graph.state import ReviewState
from app.graph.nodes import (
    analyze_code_node, 
    retrieve_standards_node,
    generate_review_node,
    save_review_node
)

workflow = StateGraph(ReviewState)

workflow.add_node("analyze",analyze_code_node)
workflow.add_node("retrieve", retrieve_standards_node)
workflow.add_node("generate", generate_review_node)
workflow.add_node("save", save_review_node)

workflow.set_entry_point("analyze")

workflow.add_edge("analyze", "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "save")
workflow.add_edge("save", END)

graph = workflow.compile()