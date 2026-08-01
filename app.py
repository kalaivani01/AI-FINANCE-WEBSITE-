import streamlit as st

from src.data_loader import load_data
from src.qa_engine import (
    categorize_transaction,
)

from views.home import show_home
from views.dashboard import show_dashboard
from views.ai_insights import show_ai_insights
from views.ask_ai import show_ask_ai
from views.report import show_report
from views.budget_planner import show_budget_planner
from views.fraud_detection import show_fraud_detection
from views.budget_tracker import show_budget_tracker
from views.financial_health import show_financial_health
from views.monthly_trends import show_monthly_trends


# ------------------------------------
# Page Configuration
# ------------------------------------
st.set_page_config(
    page_title="AI Finance Analyst",
    page_icon="💰",
    layout="wide"
)
st.markdown("""
<style>

/* -----------------------------
IMPORT FONT
------------------------------*/
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* -----------------------------
MAIN BACKGROUND
------------------------------*/

.stApp{
background:
radial-gradient(circle at top left,#3b82f6 0%,transparent 25%),
radial-gradient(circle at bottom right,#7c3aed 0%,transparent 30%),
linear-gradient(135deg,#07121F,#0F172A,#111827);
background-attachment:fixed;
color:white;
}

/* -----------------------------
HEADER
------------------------------*/

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

/* -----------------------------
SIDEBAR
------------------------------*/

section[data-testid="stSidebar"]{

background:rgba(17,24,39,.82);

backdrop-filter:blur(20px);

border-right:1px solid rgba(255,255,255,.08);

}

/* -----------------------------
GLASS CARDS
------------------------------*/

div[data-testid="metric-container"]{

background:rgba(255,255,255,.08);

border-radius:22px;

padding:20px;

border:1px solid rgba(255,255,255,.10);

backdrop-filter:blur(18px);

box-shadow:0 10px 30px rgba(0,0,0,.30);

transition:.3s;

}

div[data-testid="metric-container"]:hover{

transform:translateY(-6px);

box-shadow:0 20px 45px rgba(124,58,237,.40);

}

/* -----------------------------
BUTTONS
------------------------------*/

.stButton>button{

width:100%;

border-radius:16px;

background:linear-gradient(90deg,#2563EB,#7C3AED);

color:white;

font-weight:700;

padding:12px;

border:none;

transition:.3s;

}

.stButton>button:hover{

transform:scale(1.03);

box-shadow:0 0 20px rgba(124,58,237,.45);

}

/* -----------------------------
UPLOAD
------------------------------*/

[data-testid="stFileUploader"]{

background:rgba(255,255,255,.07);

border-radius:20px;

padding:18px;

border:1px solid rgba(255,255,255,.08);

}

/* -----------------------------
DATAFRAME
------------------------------*/

[data-testid="stDataFrame"]{

border-radius:20px;

overflow:hidden;

}

/* -----------------------------
SUCCESS BOX
------------------------------*/

.stSuccess{

border-radius:18px;

}

/* -----------------------------
INFO BOX
------------------------------*/

.stInfo{

border-radius:18px;

}

/* -----------------------------
WARNING
------------------------------*/

.stWarning{

border-radius:18px;

}

/* -----------------------------
SCROLLBAR
------------------------------*/

::-webkit-scrollbar{

width:10px;

}

::-webkit-scrollbar-thumb{

background:#7C3AED;

border-radius:20px;

}

</style>
""", unsafe_allow_html=True)

# ------------------------------------
# Sidebar
# ------------------------------------
st.sidebar.title("💰 AI Finance Analyst")
st.sidebar.success("Powered by Groq + Llama")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "🤖 AI Insights",
        "💬 Ask AI",
        "📄 AI Report",
        "💰 Budget Planner",
        "🚨 Fraud Detection",
        "🎯 Budget Tracker",
        "❤️ Financial Health",
        "📈 Monthly Trends"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### 📌 About")

st.sidebar.info("""
AI Finance Analyst

Version: 1.0

Built with:
• Python
• Streamlit
• Groq Llama
• Pandas
• Plotly
""")

# ------------------------------------
# Main Title
# ------------------------------------
st.markdown("""
<div style="
max-width:700px;
margin:0 auto;
padding:18px;
border-radius:18px;
background:
linear-gradient(135deg,#2563EB,#7C3AED,#06B6D4);
text-align:center;
box-shadow:0 25px 60px rgba(0,0,0,.35);
margin-bottom:10px;
">

<h1 style="font-size:36px;color:white;">
💰 AI Finance Analyst
</h1>

<p style="font-size:16px;color:white;">

AI Powered Financial Intelligence Platform

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
Analyze your bank statements with **Artificial Intelligence**.

Upload your CSV, explore insights, detect fraud, plan budgets and generate AI-powered financial reports.
""")

st.divider()

# ------------------------------------
# Upload CSV
# ------------------------------------
uploaded_file = st.file_uploader(
    "Upload your bank statement (CSV)",
    type=["csv"]
)
# ------------------------------------
# Load Data
# ------------------------------------

if uploaded_file is not None:

    # Read CSV
    filtered_df = load_data(uploaded_file)

    st.success("✅ File uploaded successfully!")
# -------------------------------
# Temporary Category
# -------------------------------



    if "Category" not in filtered_df.columns:
        filtered_df["Category"] = "Other"
        # ------------------------------------
        # Navigation
        # ------------------------------------

        if page == "🏠 Home":
            show_home()

        elif page == "📊 Dashboard":
            show_dashboard(filtered_df)

        elif page == "🤖 AI Insights":
            show_ai_insights(filtered_df)

        elif page == "💬 Ask AI":
            show_ask_ai(filtered_df)

        elif page == "📄 AI Report":
            show_report(filtered_df)

        elif page == "💰 Budget Planner":
            show_budget_planner(filtered_df)

        elif page == "🚨 Fraud Detection":
            show_fraud_detection(filtered_df)

        elif page == "🎯 Budget Tracker":
            show_budget_tracker(filtered_df)

        elif page == "❤️ Financial Health":
            show_financial_health(filtered_df)

        elif page == "📈 Monthly Trends":
            show_monthly_trends(filtered_df)

    else:
        st.info("📂 Please upload a CSV file.")
        # ------------------------------------
        # Footer
        # ------------------------------------
st.divider()

st.subheader("💰 AI Finance Analyst v1.0")

st.markdown("Developed with  by Kalaivani Srinivasan")

st.caption("Powered by Streamlit • Groq • Llama • Python")

st.caption("© 2026 All Rights Reserved")