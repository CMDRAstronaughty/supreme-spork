import streamlit as st

pages = {
    "Requirements":[
        st.Page("requirements.py", title = "Additional Requirements Page"),
        st.Page("issues.py", title = "Known Issues Page"),
        st.Page("lessons.py", title = "Lessons Learned Page")
    ],
    "Testing": [
        st.Page("test.py", title = "Testing Page"),
        st.Page("run_test.py", title = "Advanced Testing Page")
    ],
}

st.header(":green[UNCLASSIFIED//FOR OFFICIAL USE ONLY]")


pg = st.navigation(pages, position="top")
pg.run()