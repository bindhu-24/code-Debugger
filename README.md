# 🤖 AI Code Review Agent

An **AI-powered automated code review system** that analyzes source code, detects bugs, security vulnerabilities, code-quality issues, and best-practice violations, and generates a structured code review report using **LLM + RAG + LangGraph**.

The system combines **OpenAI GPT-4o-mini**, **LangGraph**, **RAG**, **pgvector**, **PostgreSQL**, and **FastAPI** to provide context-aware and automated code reviews.

---

## 🚀 Project Overview

Traditional code reviews require developers to manually inspect code for:

* Bugs and potential runtime issues
* Security vulnerabilities
* Poor coding practices
* Readability problems
* Performance concerns
* Violations of coding standards

This project automates that process using an **LLM-based code review agent**.

The system accepts source code from the user and:

1. Analyzes the submitted code
2. Generates an embedding for semantic search
3. Retrieves relevant coding standards using **RAG**
4. Uses **GPT-4o-mini** to review the code against those standards
5. Generates a structured review
6. Assigns a quality score
7. Identifies issues with severity and category
8. Provides recommendations for fixing the issues
9. Stores the review results in PostgreSQL

---

## ✨ Key Features

* 🤖 **AI-powered code review**
* 🔍 **Bug detection**
* 🔐 **Security vulnerability detection**
* 📚 **RAG-based coding standards retrieval**
* 🧠 **Semantic search using embeddings**
* 🗄️ **PostgreSQL + pgvector**
* 🔄 **LangGraph multi-step workflow**
* ⚡ **FastAPI REST API**
* 📊 **Structured review reports**
* 📝 **Issue severity classification**
* 🎯 **Code quality scoring**
* 💾 **Persistent review history**
* 🖥️ **Streamlit frontend**
* 🐳 **Docker support**

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │    Streamlit UI     │
                    │                     │
                    │ Code + Language +   │
                    │ Context             │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     FastAPI         │
                    │      /review        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Review Service    │
                    └──────────┬──────────┘
                               │
                               ▼
             ┌──────────────────────────────────┐
             │          LangGraph Workflow      │
             │                                  │
             │  ┌───────────────┐               │
             │  │ Analyze Code  │               │
             │  └───────┬───────┘               │
             │          ▼                        │
             │  ┌───────────────┐               │
             │  │ Retrieve RAG  │               │
             │  └───────┬───────┘               │
             │          ▼                        │
             │  ┌───────────────┐               │
             │  │ Generate      │               │
             │  │ Review        │               │
             │  └───────┬───────┘               │
             │          ▼                        │
             │  ┌───────────────┐               │
             │  │ Finalize      │               │
             │  └───────┬───────┘               │
             │          ▼                        │
             │  ┌───────────────┐               │
             │  │ Save Report   │               │
             │  └───────────────┘               │
             └──────────────────────────────────┘
                         │
                         ▼
              ┌────────────────────────┐
              │ PostgreSQL + pgvector  │
              │                        │
              │ • Code submissions     │
              │ • Review reports       │
              │ • Coding standards     │
              │ • Embeddings           │
              └────────────────────────┘
```

---

# 🔄 RAG Pipeline

The project uses **Retrieval-Augmented Generation (RAG)** to provide coding standards to the LLM before generating the review.

```text
Submitted Code
      │
      ▼
Generate Embedding
      │
      ▼
text-embedding-3-small
      │
      ▼
1536-dimensional Vector
      │
      ▼
PostgreSQL + pgvector
      │
      ▼
Cosine Similarity Search
      │
      ▼
Top-K Relevant Standards
      │
      ▼
Coding Standards + Source Code
      │
      ▼
GPT-4o-mini
      │
      ▼
Structured Code Review
```

### Top-K Retrieval

The system currently retrieves the **Top 5 most relevant coding standards**.

For example:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The RAG system can retrieve standards such as:

```text
Avoid Mutable Default Arguments
Document Public Functions
Use PEP 8 Formatting
Use snake_case Naming
```

These standards are then supplied to the LLM as context.

---

# 🧠 LangGraph Workflow

LangGraph is used to orchestrate the code-review workflow.

```text
START
  │
  ▼
Analyze Code
  │
  ▼
Retrieve Coding Standards
  │
  ▼
Generate AI Review
  │
  ▼
Finalize Review
  │
  ▼
Save Review
  │
  ▼
END
```

### Workflow Nodes

#### 1. Analyze

Receives the submitted source code and prepares it for review.

#### 2. Retrieve

Uses the code as a semantic search query and retrieves relevant coding standards from PostgreSQL + pgvector.

#### 3. Generate Review

Sends the following context to GPT-4o-mini:

```text
Source Code
+
Programming Language
+
Relevant Coding Standards
+
Optional Context
```

The LLM identifies issues and generates:

* Score
* Summary
* Severity
* Category
* Line number
* Description
* Recommendation

#### 4. Finalize

Formats the generated review into the final review result.

#### 5. Save

Persists the structured review report into PostgreSQL.

---

# 🛠️ Technology Stack

| Category             | Technology                     |
| -------------------- | ------------------------------ |
| Programming Language | Python 3.x                     |
| Backend              | FastAPI                        |
| AI / LLM             | OpenAI GPT-4o-mini             |
| Embeddings           | OpenAI text-embedding-3-small  |
| Agent Orchestration  | LangGraph                      |
| LLM Framework        | LangChain                      |
| RAG                  | Retrieval-Augmented Generation |
| Vector Database      | pgvector                       |
| Database             | PostgreSQL                     |
| ORM                  | SQLAlchemy                     |
| Validation           | Pydantic                       |
| Frontend             | Streamlit                      |
| Containerization     | Docker                         |
| API Documentation    | Swagger / OpenAPI              |

---

# 📁 Project Structure

```text
ai-code-review-agent/
│
├── app/
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── models.py
│   │   └── init_db.py
│   │
│   ├── graph/
│   │   ├── nodes.py
│   │   ├── state.py
│   │   └── workflow.py
│   │
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   └── seed_standards.py
│   │
│   ├── schemas/
│   │   └── review_schema.py
│   │
│   ├── services/
│   │   └── review_service.py
│   │
│   └── main.py
│
├── streamlit/
│   └── app.py
│
├── tests/
│   └── test_graph.py
│
├── .env
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🗄️ Database Design

The application uses PostgreSQL with pgvector.

### Code Submissions

Stores the code submitted by the user.

```text
code_submissions
├── id
├── language
├── code
└── context
```

### Review Reports

Stores the generated AI review.

```text
review_reports
├── id
├── submission_id
├── score
├── summary
└── issues
```

### Coding Standards

Stores coding standards and their embeddings.

```text
coding_standards
├── id
├── title
├── language
├── category
├── content
└── embedding
```

---

# 📡 API

## POST `/review`

Reviews submitted source code.

### Request

```json
{
  "language": "python",
  "code": "query = 'SELECT * FROM users WHERE id=' + user_id",
  "context": "Login API"
}
```

### Response

```json
{
  "review_id": 13,
  "status": "completed",
  "review": {
    "score": 60,
    "summary": "The code contains a potential security vulnerability.",
    "issues": [
      {
        "severity": "High",
        "category": "Security",
        "line_number": 1,
        "description": "Potential SQL injection vulnerability.",
        "recommendation": "Use parameterized SQL queries."
      }
    ]
  }
}
```

---

# 📊 Review Output

Each issue contains:

| Field            | Description                                                                  |
| ---------------- | ---------------------------------------------------------------------------- |
| `severity`       | Low / Medium / High / Critical                                               |
| `category`       | Bug Risk / Security / Performance / Readability / Best Practice / Code Smell |
| `line_number`    | Line where the issue occurs                                                  |
| `description`    | Explanation of the problem                                                   |
| `recommendation` | Suggested solution                                                           |

The overall review also contains:

```text
Score
Summary
Issues
```

---

# 🔐 Example: Security Review

### Input

```python
query = "SELECT * FROM users WHERE id=" + user_id
```

### AI Review

```text
Score: 35

Issue:
Severity: High
Category: Security

Description:
Potential SQL injection vulnerability caused by
directly concatenating user input into the SQL query.

Recommendation:
Use parameterized queries instead of string concatenation.
```

---

# 🐍 Example: Bug Detection

### Input

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

### AI Review

```text
Score: 60

Issue:
Severity: High
Category: Bug Risk

Description:
The function uses a mutable list as a default argument.
The same list can be shared across multiple function calls.

Recommendation:
Use None as the default value and initialize the list
inside the function.
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd ai-code-review-agent
```

## 2. Create environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key

DATABASE_URL=postgresql://postgres:postgres@db:5432/code_review_db
```

> Never commit your `.env` file or API keys to GitHub.

GitHub recommends using security features such as secret scanning and push protection to help prevent credentials from being committed to repositories.

---

# 🐳 Run with Docker

Build and start the application:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```

Swagger API documentation:

```text
http://localhost:8000/docs
```

---

# 🧪 Testing

The project includes graph-level testing.

Run:

```bash
python test_graph.py
```

Example test cases include:

### Mutable Default Argument

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

### SQL Injection

```python
query = "SELECT * FROM users WHERE id=" + user_id
```

### Hardcoded Password

```python
password = "admin123"
```

### Division by Zero

```python
def divide(a, b):
    return a / b
```

### Clean Code

```python
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b
```

---

# 🔬 How the AI Components Work

## LLM

**GPT-4o-mini** is responsible for reasoning over the source code and retrieved coding standards.

It identifies:

* Bugs
* Security vulnerabilities
* Code smells
* Readability issues
* Best-practice violations

It then generates the structured review.

---

## Embeddings

The project uses:

```text
text-embedding-3-small
```

The embedding model converts the submitted code/query into a numerical vector.

This allows the system to perform **semantic similarity search** rather than simple keyword matching.

---

## pgvector

The generated embeddings are stored in PostgreSQL using the **pgvector** extension.

The system uses cosine distance to find the most relevant coding standards.

```text
Code
 ↓
Embedding
 ↓
Vector
 ↓
pgvector
 ↓
Cosine Similarity
 ↓
Top-K Standards
```

---

# 🎯 Why RAG?

Instead of asking the LLM to review code using only its general knowledge, the system provides relevant coding standards retrieved from the knowledge base.

This improves:

* Context awareness
* Consistency
* Domain-specific reviews
* Control over coding standards
* Explainability

The knowledge base can also be updated without retraining the LLM.

---

# 🔄 Complete Request Flow

```text
User
 │
 │ Submit Code
 ▼
Streamlit
 │
 ▼
FastAPI
 │
 ▼
Review Service
 │
 ▼
Create Code Submission
 │
 ▼
LangGraph
 │
 ├── Analyze Code
 │
 ├── Generate Embedding
 │
 ├── Search pgvector
 │
 ├── Retrieve Top-K Standards
 │
 ├── Send Code + Standards to GPT
 │
 ├── Generate Structured Review
 │
 ├── Validate with Pydantic
 │
 └── Save Review
 │
 ▼
PostgreSQL
 │
 ▼
API Response
 │
 ▼
Streamlit UI
```

---

# 📈 Future Enhancements

Possible future improvements include:

* GitHub Pull Request integration
* Automatic PR comments
* Multi-language support
* Additional coding standards
* Larger RAG knowledge base
* Review history dashboard
* Code diff analysis
* Authentication and authorization
* CI/CD integration
* Automated test generation
* Performance analysis
* LLM evaluation metrics
* Human feedback loop
* Multiple LLM provider support

---

# 🔒 Security Considerations

* Store API keys in environment variables.
* Never commit `.env` files.
* Validate incoming API requests.
* Limit maximum code input size.
* Sanitize and validate database inputs.
* Use parameterized SQL queries.
* Enable GitHub secret scanning for the repository.

---

# 💡 Key AI Concepts Demonstrated

This project demonstrates practical implementation of:

* **Generative AI**
* **Large Language Models**
* **Prompt Engineering**
* **Embeddings**
* **Vector Search**
* **RAG**
* **LangChain**
* **LangGraph**
* **Agentic Workflow**
* **Semantic Search**
* **Structured LLM Output**
* **Pydantic Validation**
* **FastAPI**
* **PostgreSQL**
* **pgvector**
* **Docker**

---

# 👩‍💻 Author

**Bindhu Selvi**

AI Engineer | Python | Generative AI | RAG | Agentic AI

---

## ⭐ Project Highlights

> **An end-to-end AI Code Review Agent that combines LLM reasoning, RAG-based coding standards retrieval, pgvector semantic search, LangGraph workflow orchestration, FastAPI, PostgreSQL, and Streamlit to automate software code reviews.**

If you find this project useful, consider giving the repository a ⭐.
