# 🤖 AI Code Review Agent

An AI-powered code review system that analyzes source code for bugs, security vulnerabilities, code smells, readability issues, and best practice violations using Large Language Models and LangGraph orchestration.

## Features

* Multi-language code review support

  * Python
  * JavaScript
  * Java
  * C++
  * Go
* Security vulnerability detection
* Bug risk identification
* Code smell detection
* Readability analysis
* Best practice recommendations
* RAG-powered coding standards retrieval
* LangGraph workflow orchestration
* Review history tracking
* Code health score visualization
* Streamlit frontend UI
* FastAPI backend API

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* LangGraph
* LangChain
* OpenAI GPT Models

### Frontend

* Streamlit

### Database

* PostgreSQL
* pgvector

---

## Project Structure

```text
code-Debugger/
│
├── app/
│   ├── api/
│   ├── database/
│   ├── graph/
│   ├── llm/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── streamlit_app.py
│   └── pages/
│       └── review_history.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## LangGraph Workflow

1. Accept source code from user.
2. Store submission in database.
3. Retrieve relevant coding standards using RAG.
4. Analyze code using LLM.
5. Generate structured review report.
6. Save review results.
7. Return response to UI.

---

## API Endpoints

### Review Code

```http
POST /review
```

Example Request:

```json
{
  "language": "python",
  "code": "print('Hello World')",
  "context": "Example API"
}
```

---

### Review History

```http
GET /reviews
```

Returns all previously generated code reviews.

---

## Running the Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Activate virtual environment:

```bash
venv\Scripts\activate
```

Start Streamlit:

```bash
streamlit run frontend/streamlit_app.py
```

---

## Example Issues Detected

* SQL Injection
* Hardcoded Secrets
* Command Injection
* Infinite Loops
* Division by Zero
* Magic Numbers
* Missing Type Hints
* Duplicate Code
* Performance Bottlenecks

---

## Future Enhancements

* GitHub Pull Request Reviews
* SonarQube Integration
* PDF Report Export
* Authentication and User Management
* CI/CD Integration
* Docker Deployment

---
