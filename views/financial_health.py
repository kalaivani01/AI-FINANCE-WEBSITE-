import streamlit as st
from src.qa_engine import generate_health_score


def show_financial_health(filtered_df):

    st.header("❤️ Financial Health")

    st.write("Analyze your overall financial health using AI.")

    if st.button("Generate Health Score"):

        with st.spinner("Calculating your financial health..."):

            result = generate_health_score(filtered_df)

        st.success("Analysis Complete!")

        st.write(result)