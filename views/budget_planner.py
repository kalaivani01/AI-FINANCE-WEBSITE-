import streamlit as st
from src.qa_engine import generate_budget_plan


def show_budget_planner(filtered_df):

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#10B981,#2563EB,#7C3AED);
        padding:35px;
        border-radius:25px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    ">
        <h1>💰 AI Budget Planner</h1>
        <p style="font-size:18px;">
            Build a smarter monthly budget with AI-powered planning and
            personalized savings recommendations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🎯 Goal", "Smart Budget")

    with col2:
        st.metric("🤖 AI Engine", "Llama 3")

    with col3:
        st.metric("📅 Plan", "Monthly")

    st.markdown("### ✨ What You'll Receive")

    c1, c2 = st.columns(2)

    with c1:
        st.success("✅ Personalized monthly budget")
        st.success("✅ Spending recommendations")
        st.success("✅ Savings opportunities")

    with c2:
        st.info("📊 Category-wise allocation")
        st.info("💡 AI financial tips")
        st.info("🎯 Better money management")

    st.markdown("")

    if st.button("🚀 Generate Budget Plan", use_container_width=True):

        with st.spinner("🤖 AI is creating your personalized budget..."):

            budget = generate_budget_plan(filtered_df)

        st.success("✅ Budget Plan Generated!")

        st.markdown("## 💰 Your AI Budget Plan")

        st.markdown(f"""
        <div style="
        background:rgba(255,255,255,.08);
        padding:30px;
        border-radius:20px;
        border:1px solid rgba(255,255,255,.1);
        margin-bottom:20px;
        ">
        {budget}
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
        💡 <b>Tip:</b> Revisit your budget regularly as your income or spending habits change. Small adjustments over time can have a big impact on your savings.
    </div>
    """, unsafe_allow_html=True)

