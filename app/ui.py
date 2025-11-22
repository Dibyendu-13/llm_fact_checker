import streamlit as st
from src.main import fact_check

st.title("🤖 LLM Fact Checker")

user_input = st.text_area("Enter a claim:")

if st.button("Check Fact"):
    with st.spinner("Checking..."):
        response = fact_check(user_input)
        st.json(response)
