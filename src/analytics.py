import pandas as pd
import streamlit as st
import plotly.express as px


# ----------------------------------------
# Summary
# ----------------------------------------
def show_summary(df):

    st.subheader("📊 Financial Summary")

    total_income = df[df["Amount"] > 0]["Amount"].sum()

    total_expense = abs(df[df["Amount"] < 0]["Amount"].sum())

    balance = total_income - total_expense

    total_transactions = len(df)

    expense_df = df[df["Amount"] < 0]

    if not expense_df.empty:
        average_expense = abs(expense_df["Amount"].mean())
        highest_expense = abs(expense_df["Amount"].min())
    else:
        average_expense = 0
        highest_expense = 0

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Total Income", f"₹{total_income:,.2f}")
    col2.metric("💸 Total Expense", f"₹{total_expense:,.2f}")
    col3.metric("🏦 Balance", f"₹{balance:,.2f}")

    col4, col5, col6 = st.columns(3)

    col4.metric("📄 Transactions", total_transactions)
    col5.metric("📈 Avg Expense", f"₹{average_expense:,.2f}")
    col6.metric("🔥 Highest Expense", f"₹{highest_expense:,.2f}")


# ----------------------------------------
# Expense Chart
# ----------------------------------------
def show_expense_chart(df):

    expense = df[df["Amount"] < 0]

    if expense.empty:
        return

    fig = px.bar(
        expense,
        x="Description",
        y="Amount",
        title="Expenses"
    )

    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------
# Monthly Expense Chart
# ----------------------------------------
def show_monthly_expense_chart(df):

    df = df.copy()

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    df["Month"] = df["Date"].dt.strftime("%b %Y")

    monthly = (
        df.groupby("Month")["Amount"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        monthly,
        x="Month",
        y="Amount",
        title="Monthly Expenses"
    )

    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------
# Category Expense Chart
# ----------------------------------------
def show_category_expense_chart(df):

    if "Category" not in df.columns:
        return

    category = (
        df.groupby("Category")["Amount"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category,
        names="Category",
        values="Amount",
        title="Expense by Category"
    )

    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------
# Large Transactions
# ----------------------------------------
def show_large_transactions(df):

    st.subheader("🚨 Large Transactions")

    large = df[df["Amount"].abs() > 10000]

    if large.empty:
        st.info("No large transactions found.")
    else:
        st.dataframe(large)


# ----------------------------------------
# Monthly Spending Trend
# ----------------------------------------
def show_monthly_trend(df):

    df = df.copy()

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    df["Month"] = df["Date"].dt.strftime("%b %Y")

    monthly = (
        df.groupby("Month")["Amount"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly,
        x="Month",
        y="Amount",
        title="Monthly Spending Trend",
        markers=True
    )

    fig.update_layout(height=500)

    return fig
def show_top_merchants(df):

    st.subheader("🏪 Top 10 Spending Merchants")

    expense = df[df["Amount"] < 0].copy()

    if expense.empty:
        st.info("No expense transactions found.")
        return

    merchants = (
        expense.groupby("Description")["Amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        merchants,
        x="Description",
        y="Amount",
        title="Top 10 Spending Merchants"
    )

    st.plotly_chart(fig, use_container_width=True)