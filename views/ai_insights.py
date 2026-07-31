import streamlit as st
from src.qa_engine import generate_spending_insights


def show_ai_insights(filtered_df):

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#7C3AED,#2563EB,#06B6D4);
    padding:35px;
    border-radius:25px;
    color:white;
    text-align:center;
    margin-bottom:25px;
    ">

    <h1>🤖 AI Financial Intelligence</h1>

    <p style="font-size:18px;">
    Let Artificial Intelligence analyze your financial behaviour and
    generate smart recommendations.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1,col2,col3=st.columns(3)

    with col1:
        st.metric("🧠 AI Model","Llama 3")

    with col2:
        st.metric("⚡ Speed","<2 sec")

    with col3:
        st.metric("🎯 Accuracy","95%")

    st.write("")

    st.markdown("### 💡 What AI Can Do")

    c1,c2,c3=st.columns(3)

    with c1:
        st.success("✅ Detect spending patterns")

    with c2:
        st.info("📈 Predict financial trends")

    with c3:
        st.warning("🚨 Identify unusual expenses")

    st.write("")

    if st.button("🚀 Generate AI Insights"):

        with st.spinner("🤖 AI is analyzing your financial data..."):

            insights = generate_spending_insights(filtered_df)

            if insights.startswith("⚠️") or insights.startswith("🔑"):
                st.error(insights)
            else:
                st.success("✅ Analysis Completed!")
                st.write(insights)

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown("---")

    st.markdown("""
    <div style="
    text-align:center;
    padding:20px;
    border-radius:20px;
    background:rgba(255,255,255,.05);
    ">

    ✨ Powered by Groq + Llama AI

    </div>
    """, unsafe_allow_html=True)