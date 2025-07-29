import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.coordinator_agent import CoordinatorAgent
import uuid

st.set_page_config(layout="wide", page_title="Agentic RAG Chatbot")

agent = CoordinatorAgent()
trace_id = str(uuid.uuid4())

st.title("📄 Agentic RAG Chatbot")

uploaded_files = st.file_uploader("Upload documents", accept_multiple_files=True)
query = st.text_input("Enter your question")

if st.button("Submit") and uploaded_files and query:
    paths = []
    for file in uploaded_files:
        path = os.path.join("data/uploaded_files", file.name)
        with open(path, "wb") as f:
            f.write(file.read())
        paths.append(path)

    response_msg = agent.run_pipeline(paths, query, trace_id)
    st.subheader("📤 Answer")
    st.write(response_msg["payload"]["response"])
