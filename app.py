
import streamlit as st
from dotenv import load_dotenv
import os
import shelve

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

#______________________ chat message history ___________________
# Load chat history from shelve file
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])


# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages


# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])


st.title("NyaaSaki Timeshares Query Bot")
with st.spinner("waking up the bot"):
    import backend
st.markdown("__🟢 The bot is online__")


if prompt := st.chat_input("How can I help?"):
    with st.chat_message("You", avatar=USER_AVATAR):
        st.session_state.messages.append({"role": "You", "content": prompt})
        st.markdown(prompt)
    with st.chat_message("Zofia", avatar=BOT_AVATAR):
        msg = backend.req(prompt)
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.markdown(msg)