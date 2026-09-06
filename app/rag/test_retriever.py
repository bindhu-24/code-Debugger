from app.database.connection import SessionLocal
from app.rag.retriever import retrieve_standards

def test_retrieval():
    db = SessionLocal()

    try:
        query = """
        query = "SELECT * FROM users WHERE id=" + user_id
        """

        results = retrieve_standards(
            db=db,  
            query=query,
            language="python",
            category="Security",
            limit=5
        )

        print("\nRetrieved Standards:\n")

        for standard in results:
            print(f"Title: {standard.title}")
            print(f"Language: {standard.language}")
            print(f"Category: {standard.category}")
            print(f"Content: {standard.content}")
            # print(f"Description: {standard.description}")
            print(f"Embedding: {len(standard.embedding)}")

    finally:
        db.close()

if __name__ == "__main__":
    test_retrieval()

