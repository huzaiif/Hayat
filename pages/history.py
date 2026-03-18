import streamlit as st
from database.db import get_chat_history, clear_chat_history

def show_history():
    st.title("Chat History 🕰️")
    st.markdown("View all your past interactions with Hayat.")
    
    user_id = st.session_state['user_id']
    
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("🗑️ Clear All History", use_container_width=True, key="clear_history_btn"):
            clear_chat_history(user_id)
            st.session_state.pop('messages', None)
            st.rerun()
            
    st.markdown("---")
    
    history = get_chat_history(user_id)
    
    if not history:
        st.info("No chat history found. Go to the Chatbot tab to start a conversation!")
        return

    for msg in history:
        with st.chat_message(msg['role']):
            st.caption(msg['timestamp'])
            st.markdown(msg['message'])

if __name__ == "__main__":
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        show_history()
    else:
        st.warning("Please log in to view this page.")
