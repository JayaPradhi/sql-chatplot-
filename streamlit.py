import streamlit as st
from model import get_few_shot_db_chain

st.title(" Text-based Personal Assistant(chatbot)")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)
