import streamlit as st
from features.chatbot import get_chat_response, init_chatbot
from database.db import save_chat, get_chat_history, clear_chat_history

def show_chat():
    st.title("Hayat Chatbot 💬")
    st.markdown("Ask any health-related questions. Your conversation history is securely saved.")
    
    user_id = st.session_state['user_id']
    
    # Add clear history button
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("🗑️ Clear History", use_container_width=True):
            clear_chat_history(user_id)
            st.session_state.pop('messages', None)
            st.rerun()

    st.markdown("---")
    
    if init_chatbot():
        # Load chat history from DB if not in session state
        if "messages" not in st.session_state:
            db_history = get_chat_history(user_id)
            st.session_state.messages = [{"role": row["role"], "content": row["message"]} for row in db_history]

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # React to user input
        if prompt := st.chat_input("Ask me anything about health topics..."):
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            save_chat(user_id, prompt, "user")
            
            with st.spinner("Thinking..."):
                response_text = get_chat_response(prompt)
                
            with st.chat_message("assistant"):
                st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            save_chat(user_id, response_text, "assistant")
    else:
        st.error("Failed to configure API. Please check your API Key in the .env file.")

if __name__ == "__main__":
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        show_chat()
    else:
        st.warning("Please log in to view this page.")
