import streamlit as st

st.title("StudyMate AI Academic Assistant")
st.write("Welcome to StudyMate! Use the sidebar to navigate through features.")

st.sidebar.title("Navigation")
st.sidebar.markdown("""
- PDF Q&A (pages/1_pdf_qa.py)
- Summarization (pages/2_summarization.py)
- Citation Management (pages/3_citation.py)
- Literature Discovery (pages/4_literature.py)
- Writing Assistant (pages/5_writing.py)
- Plagiarism Detection (pages/6_plagiarism.py)
- Text-to-Audio (pages/7_text_to_audio.py)
- Collaboration Tools (pages/8_collaboration.py)
- Conversational Interface (pages/9_conversational.py)
- Workflow Integration (pages/10_integration.py)
- Adaptive Learning (pages/11_adaptive.py)
""")

st.write("""
This home page links to all the features of StudyMate.  
Upload documents, ask questions, get summaries, manage citations, and much more—all powered by AI.
""")
