from app.graph.review_graph import review_graph

result = review_graph.invoke(
    {
        "language": "python",
        "code": "print('hello')",
        "context": "",
        "standards": "",
        "review": {}
    }
)

print(result)