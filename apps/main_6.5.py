import streamlit as st

st.title("langchain-streamlit-app")

prompt = st.chat_input("What is up?")
if prompt != "" and prompt is not None:
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = "こんにちは"
        st.markdown(response)
