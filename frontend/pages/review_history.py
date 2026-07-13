import streamlit as st
import requests

st.title("📜 Review History")
try:
    response = requests.get(
        "http://127.0.0.1:8000/reviews",
        timeout=10
    )

    if response.status_code == 200:
        reviews = response.json()

        for review in reviews:
            with st.expander(
                f"Review #{review['id']} | Score: {review['score']}"
            ):
                st.write(
                    f"### Summary\n{review['summary']}"
                )

                st.write("### Issues")

                for issue in review["issues"]:
                    st.write(
                        f"""
**Severity:** {issue['severity']}

**Category:** {issue['category']}

**Description:** {issue['description']}

**Recommendation:** {issue['recommendation']}
"""
                )
    else:
        st.error(
            f"API Error: {response.status_code}\n{response.text}"
        )

except requests.exceptions.ConnectionError:
    st.error(
        "Cannot connect to FastAPI backend.\n\n"
        "Please start the backend using:\n\n"
        "uvicorn app.main:app --reload"
    )