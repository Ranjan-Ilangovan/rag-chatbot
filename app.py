import streamlit as st
from rag import load_and_index_pdf, get_answer

# Page config
st.set_page_config(
    page_title="AI Document Q&A",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI Document Q&A Chatbot")
st.markdown("Upload a PDF and ask questions — powered by Llama3 + RAG")

# Sidebar
with st.sidebar:
    st.header("📄 Upload Document")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf"
    )

    if uploaded_file:
        with st.spinner("Reading and indexing PDF..."):
            vectorstore = load_and_index_pdf(uploaded_file)
            st.session_state.vectorstore = vectorstore
        st.success("✅ PDF indexed! Ask your questions.")
        st.info(f"📁 File: {uploaded_file.name}")

# Chat interface
st.header("💬 Ask Questions")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask anything about your document..."):
    if "vectorstore" not in st.session_state:
        st.warning("⚠️ Please upload a PDF first!")
    else:
        # Show user message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get AI answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                result = get_answer(
                    st.session_state.vectorstore,
                    prompt
                )
                answer = result["answer"]
                sources = result["sources"]

                # Show answer
                st.markdown(answer)

                # Show citations
                with st.expander("📚 Sources"):
                    for i, doc in enumerate(sources):
                        st.markdown(f"**Source {i+1} "
                                  f"(Page {doc.metadata.get('page', '?') + 1}):**")
                        st.markdown(f"> {doc.page_content[:300]}...")
                        st.divider()

        # Save assistant message
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })