from langgraph.graph import StateGraph, END
from app.graph.state import ReviewState
from app.graph.nodes import (
    analyze_code, 
    retrieve_standards,
    generate_review,
    finalize_review,
    save_review,
    should_finalize,
)

workflow = StateGraph(ReviewState)

workflow.add_node("analyze",analyze_code)
workflow.add_node("retrieve", retrieve_standards)
workflow.add_node("generate", generate_review)
workflow.add_node("finalize", finalize_review)
workflow.add_node("save", save_review)

workflow.set_entry_point("analyze")

workflow.add_edge("analyze", "retrieve")
workflow.add_edge("retrieve", "generate")

workflow.add_conditional_edges(
    
    "generate",
    should_finalize,
    {
        "finalize": "finalize",
        "end": END
    }
)

# workflow.add_edge("generate", "finalize")
workflow.add_edge("finalize", "save")
workflow.add_edge("save", END)

graph = workflow.compile()