import streamlit as st
from rag_pipeline import retrieve_top_k_chunks, generate_answer

st.set_page_config(page_title="CrediTrust Chatbot", layout="centered")
st.title("📊 CrediTrust Complaint Assistant")

# Input form
with st.form("chat_form"):
    question = st.text_input("Type your question about a customer complaint:")
    submit = st.form_submit_button("Ask")
    clear = st.form_submit_button("Clear")

if clear:
    st.experimental_rerun()

if submit and question:
    with st.spinner("Searching..."):
        chunks = retrieve_top_k_chunks(question)
        answer = generate_answer(question, chunks)

        # Output answer
        st.subheader("💡 AI Answer")
        st.write(answer)

        # Display sources
        st.subheader("📚 Source Chunks")
        for i, chunk in enumerate(chunks, 1):
            st.markdown(f"**Source {i}** (Complaint ID: `{chunk['complaint_id']}`)")
            st.code(chunk["text"])
