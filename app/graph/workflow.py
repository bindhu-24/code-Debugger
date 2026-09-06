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


def build_review_graph():

    workflow = StateGraph(ReviewState)

    # Nodes
    workflow.add_node("analyze", analyze_code)
    workflow.add_node("retrieve", retrieve_standards)
    workflow.add_node("generate_review", generate_review)
    workflow.add_node("finalize", finalize_review)
    workflow.add_node("save", save_review)

    # Entry point
    workflow.set_entry_point("analyze")

    # Analyze → RAG
    workflow.add_edge("analyze", "retrieve")

    # RAG → LLM
    workflow.add_edge("retrieve", "generate_review")

    # LLM → conditional
    workflow.add_conditional_edges(
        "generate_review",
        should_finalize,
        {
            "finalize": "finalize",
            "end": END,
        }
    )

    # Finalize → Save
    workflow.add_edge("finalize", "save")

    # Save → End
    workflow.add_edge("save", END)

    return workflow.compile()