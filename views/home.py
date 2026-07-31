import streamlit as st

def show_home():

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#2563EB,#7C3AED,#06B6D4);
        padding:45px;
        border-radius:30px;
        text-align:center;
        color:white;
        margin-bottom:30px;
        box-shadow:0 20px 50px rgba(0,0,0,.35);
    ">

    <h1 style="font-size:60px;margin-bottom:10px;">
    💰 AI Finance Analyst
    </h1>

    <p style="font-size:22px;opacity:.95;">
    Transform your bank statements into powerful financial insights using Artificial Intelligence.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🚀 Everything You Need In One Place")

    col1,col2,col3=st.columns(3)

    with col1:

        st.markdown("""
        <div style="
        background:rgba(255,255,255,.08);
        padding:25px;
        border-radius:20px;
        text-align:center;
        backdrop-filter:blur(18px);
        ">

        <h2>📊</h2>

        <h3>Dashboard</h3>

        <p>Visualize your income, expenses and savings instantly.</p>

        </div>
        """,unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div style="
        background:rgba(255,255,255,.08);
        padding:25px;
        border-radius:20px;
        text-align:center;
        backdrop-filter:blur(18px);
        ">

        <h2>🤖</h2>

        <h3>AI Insights</h3>

        <p>Receive smart recommendations powered by Llama AI.</p>

        </div>
        """,unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div style="
        background:rgba(255,255,255,.08);
        padding:25px;
        border-radius:20px;
        text-align:center;
        backdrop-filter:blur(18px);
        ">

        <h2>🚨</h2>

        <h3>Fraud Detection</h3>

        <p>Detect suspicious financial transactions instantly.</p>

        </div>
        """,unsafe_allow_html=True)

    st.write("")

    col4,col5,col6=st.columns(3)

    with col4:

        st.metric("📈 AI Accuracy","95%","+2%")

    with col5:

        st.metric("💳 Transactions","25K+")

    with col6:

        st.metric("⚡ Processing","< 2 sec")

    st.write("")

    st.markdown("## ⭐ Platform Features")

    feature1,feature2=st.columns(2)

    with feature1:

        st.success("✅ AI Powered Transaction Categorization")
        st.success("✅ Financial Health Score")
        st.success("✅ Monthly Trend Analysis")
        st.success("✅ Budget Planner")
        st.success("✅ Fraud Detection")

    with feature2:

        st.info("📄 AI Generated Reports")
        st.info("💬 Ask AI Anything")
        st.info("📈 Interactive Charts")
        st.info("💰 Expense Analysis")
        st.info("🔒 Secure Processing")

    st.markdown("---")

    st.markdown("""
    <div style="
    text-align:center;
    padding:25px;
    border-radius:20px;
    background:rgba(255,255,255,.05);
    ">

    <h2>✨ AI Finance Analyst v2.0</h2>

    Built with ❤️ using

    Streamlit • Groq • Llama • Plotly • Python

    </div>
    """,unsafe_allow_html=True)