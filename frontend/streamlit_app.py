import streamlit as st
import requests

st.set_page_config(
    page_title="AI Code Review Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Code Review Agent")

language = st.selectbox(
    "Programming Language",
    [
        "python",
        "javascript",
        "java",
        "c++",
        "go"
    ]
)

code = st.text_area(
    "Paste your code here",
    height=300
)

context = st.text_input(
    "Optional Context",
    placeholder="Example: Login API"
)

if st.button("Review Code"):
    if not code.strip():
        st.warning("Please enter some code.")
    else:
        payload = {
            "language": language,
            "code": code,
            "context": context
        }

        with st.spinner("Reviewing code..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/review",
                    json=payload,
                    timeout=30
                )
            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to FastAPI backend.\n\n"
                    "Please start the backend using:\n\n"
                    "uvicorn app.main:app --reload"
                )
                st.stop()

        if response.status_code == 200:
            result = response.json()

            review = result["review"]
            score = review["score"]

            st.success("Review completed!")

            col1, col2 = st.columns([3, 1])
            with col1:
                st.progress(score / 100)

            with col2:
                st.metric("Score", f"{score}/100")

            if score >= 90:
                st.success(f"🟢 Excellent Code Quality ({score}/100)")
            elif score >= 70:
                st.warning(f"🟡 Good Code Quality ({score}/100)")
            elif score >= 50:
                st.warning(f"🟠 Moderate Code Quality ({score}/100)")
            else:
                st.error(f"🔴 Poor Code Quality ({score}/100)")

            st.subheader("Summary")
            st.write(review["summary"])

            st.subheader("Issues Found")

            if review["issues"]:
                for issue in review["issues"]:
                    with st.expander(
                        f"{issue['severity']} - {issue['category']}"
                    ):
                        st.write(issue["description"])
                        st.write(issue["recommendation"])
            else:
                st.success("No issues found.")

            st.subheader("Submitted Code")
            st.code(code, language=language)

        else:
            st.error(
                f"Failed to load review history.\n\n"
                f"Status Code: {response.status_code}\n"
                f"Response: {response.text}")

