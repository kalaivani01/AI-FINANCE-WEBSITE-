import streamlit as st
from src.qa_engine import detect_fraud


def show_fraud_detection(filtered_df):

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#DC2626,#F97316,#7C3AED);
        padding:35px;
        border-radius:25px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    ">
        <h1>🛡️ AI Fraud Detection</h1>
        <p style="font-size:18px;">
            Detect unusual spending patterns and identify potentially suspicious
            transactions using AI-powered analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🛡️ Protection", "Active")

    with col2:
        st.metric("🤖 AI Engine", "Llama 3")

    with col3:
        st.metric("⚡ Status", "Monitoring")

    st.markdown("### 🚨 AI Fraud Detection Checks")

    c1, c2 = st.columns(2)

    with c1:
        st.success("✅ Detect unusual spending")
        st.success("✅ Identify suspicious merchants")
        st.success("✅ Flag abnormal transactions")

    with c2:
        st.info("📊 Spending pattern analysis")
        st.info("💳 Transaction anomaly detection")
        st.info("🔍 AI risk assessment")

    st.write("")

    if st.button("🚀 Analyze Transactions", use_container_width=True):

        with st.spinner("🤖 AI is analyzing your transaction history..."):

            result = detect_fraud(filtered_df)

        st.success("✅ Analysis Completed Successfully!")

        st.markdown("## 🚨 Fraud Detection Report")

        st.markdown(f"""
        <div style="
        background:rgba(255,255,255,.08);
        padding:30px;
        border-radius:20px;
        border:1px solid rgba(255,255,255,.1);
        margin-bottom:20px;
        ">
        {result}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="
        background:rgba(255,255,255,.05);
        padding:20px;
        border-radius:20px;
        text-align:center;
    ">
        🛡️ <b>Security Tip:</b><br><br>
        Review your transactions regularly, enable bank alerts, and report any
        unfamiliar activity immediately.
    </div>
    """, unsafe_allow_html=True)