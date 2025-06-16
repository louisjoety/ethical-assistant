import streamlit as st
from streamlit_chat import message
from langchain.schema import HumanMessage, AIMessage
from utils.gemini_utils import get_gemini_summary

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "feedback" not in st.session_state:
    st.session_state.feedback = {}
if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None
if "first_query" not in st.session_state:
    st.session_state.first_query = True
if "last_feedback_negative" not in st.session_state:
    st.session_state.last_feedback_negative = False
if "last_feedback_positive" not in st.session_state:
    st.session_state.last_feedback_positive = False

if st.session_state.first_query:
    st.markdown(
        """
        <div style='
            text-align: center;
            font-size: 36px;
            margin: 50px 0;
            color: #444;
        '>What can I help with today?</div>
        """,
        unsafe_allow_html=True,
    )

def get_feedback(message_idx, disabled=False):
    options = ["👎", "👍"]
    selected = st.radio("Your feedback:", options, key=f"feedback_{message_idx}", horizontal=True, disabled=disabled)
    if selected is not None:
        st.session_state.feedback[message_idx] = selected
        st.markdown(f"You selected: {selected}")

        st.session_state.last_feedback_negative = (selected == "👎")
        st.session_state.last_feedback_positive = (selected == "👍")
    elif message_idx in st.session_state.feedback:
        stored = st.session_state.feedback[message_idx]
        st.markdown(f"Feedback: {stored}")

def answer_query(query):
    return get_gemini_summary(query)

prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.first_query = False
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    st.session_state.pending_prompt = prompt

for idx, msg in enumerate(st.session_state.chat_history):
    is_user = isinstance(msg, HumanMessage)
    message(
        msg.content,
        is_user=is_user,
        key=f"msg_{idx}",
        avatar_style="thumbs" if is_user else "bottts",
        seed=idx
    )

    if not is_user:
        is_last_answer = idx == len(st.session_state.chat_history) - 1
        get_feedback(idx, disabled=not is_last_answer)

if st.session_state.pending_prompt:
    with st.spinner("Thinking..."):
        answer = answer_query(st.session_state.pending_prompt)

    st.session_state.chat_history.append(AIMessage(content=answer))
    message(
        answer,
        is_user=False,
        key=f"msg_{len(st.session_state.chat_history) - 1}",
        avatar_style="bottts",
        seed=123
    )

    get_feedback(len(st.session_state.chat_history) - 1)

    st.session_state.pending_prompt = None
