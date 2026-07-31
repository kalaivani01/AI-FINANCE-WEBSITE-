import streamlit as st
import pandas as pd

from src.analytics import (
    show_summary,
    show_expense_chart,
    show_monthly_expense_chart,
    show_category_expense_chart,
    show_large_transactions,
    show_top_merchants,
)


def show_dashboard(filtered_df):
    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#2563EB,#7C3AED,#06B6D4);
    padding:35px;
    border-radius:25px;
    color:white;
    text-align:center;
    margin-bottom:30px;
    ">

    <h1>📊 Financial Dashboard</h1>

    <p>
    AI Powered Analytics & Financial Intelligence
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ----------------------------------------
    # Date Filter
    # ----------------------------------------

    st.divider()
    st.header("📅 Filter Transactions")

    filtered_df = filtered_df.copy()

    filtered_df["Date"] = pd.to_datetime(
        filtered_df["Date"],
        errors="coerce"
    )

    start_date = st.date_input(
        "Start Date",
        value=filtered_df["Date"].min()
    )

    end_date = st.date_input(
        "End Date",
        value=filtered_df["Date"].max()
    )

    filtered_df = filtered_df[
        (filtered_df["Date"] >= pd.Timestamp(start_date)) &
        (filtered_df["Date"] <= pd.Timestamp(end_date))
    ]

    # ----------------------------------------
    # Category Filter
    # ----------------------------------------

    if "Category" in filtered_df.columns:

        st.divider()
        st.header("📂 Filter by Category")

        categories = ["All"] + sorted(
            filtered_df["Category"].dropna().unique().tolist()
        )

        selected_category = st.selectbox(
            "Select Category",
            categories
        )

        if selected_category != "All":
            filtered_df = filtered_df[
                filtered_df["Category"] == selected_category
            ]

    # ----------------------------------------
    # Search Transactions
    # ----------------------------------------

    st.divider()
    st.header("🔍 Search Transactions")

    search = st.text_input("Search Description")

    if search:
        filtered_df = filtered_df[
            filtered_df["Description"]
            .str.contains(search, case=False, na=False)
        ]

    # ----------------------------------------
    # Bank Statement
    # ----------------------------------------

    st.divider()
    st.subheader("📋 Bank Statement")

    st.dataframe(filtered_df, use_container_width=True)
    # ----------------------------------------
    # Download Filtered Data
    # ----------------------------------------

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Filtered Transactions",
        data=csv,
        file_name="filtered_transactions.csv",
        mime="text/csv",
    )

    # ----------------------------------------
    # Dashboard Analytics
    # ----------------------------------------

    st.divider()

    show_summary(filtered_df)
    show_expense_chart(filtered_df)
    show_monthly_expense_chart(filtered_df)
    show_category_expense_chart(filtered_df)
    show_large_transactions(filtered_df)
    show_top_merchants(filtered_df)

    return filtered_df
