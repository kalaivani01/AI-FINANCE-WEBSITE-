import streamlit as st

def show_monthly_trends(df):
    st.title("📈 Monthly Trends")

    if df is None or df.empty:
        st.warning("Please upload a bank statement first.")
        return

    st.subheader("Monthly Transactions")
    st.dataframe(df)