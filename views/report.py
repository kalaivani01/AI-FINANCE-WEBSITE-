import streamlit as st
from src.qa_engine import ask_ai
from src.pdf_generator import create_pdf


def show_report(filtered_df):

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#2563EB,#7C3AED,#06B6D4);
        padding:35px;
        border-radius:25px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    ">
        <h1>📄 AI Financial Report</h1>
        <p style="font-size:18px;">
            Generate a professional financial report with AI-powered insights,
            spending analysis, and personalized recommendations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📊 Analysis", "Complete")

    with col2:
        st.metric("🤖 AI Engine", "Llama 3")

    with col3:
        st.metric("📑 Format", "PDF")

    st.markdown("### 📋 Report Includes")

    c1, c2 = st.columns(2)

    with c1:
        st.success("✅ Spending Summary")
        st.success("✅ Top Expense Categories")
        st.success("✅ Monthly Overview")

    with c2:
        st.info("💰 Saving Tips")
        st.info("📈 Financial Health Score")
        st.info("🤖 AI Recommendations")

    st.write("")

    if st.button("🚀 Generate Financial Report", use_container_width=True):

        data = filtered_df.to_string(index=False)

        prompt = f"""
You are an expert financial advisor.

Analyze this bank statement.

{data}

Provide:

1. Spending Summary

2. Top Expenses

3. Saving Tips

4. Financial Health Score (out of 10)

Keep the report professional, concise, and actionable.
"""

        with st.spinner("🤖 AI is preparing your financial report..."):

            report = ask_ai(prompt)

            if report.startswith("⚠️") or report.startswith("🔑"):
                st.error(report)
            else:
                st.success("✅ Report Generated!")
                st.write(report)

                pdf_file = create_pdf(report)

                with open(pdf_file, "rb") as file:

                    st.download_button(
                        "📥 Download PDF Report",
                        data=file,
                        file_name="AI_Financial_Report.pdf",
                        mime="application/pdf"
                    )

        pdf_file = create_pdf(report)

        with open(pdf_file, "rb") as file:

            st.download_button(
                "📥 Download Professional PDF Report",
                data=file,
                file_name="AI_Financial_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    st.markdown("---")

    st.markdown("""
    <div style="
        background:rgba(255,255,255,.05);
        padding:20px;
        border-radius:20px;
        text-align:center;
    ">
        📌 <b>Your report includes AI-driven financial analysis and recommendations based solely on the uploaded bank statement.</b>
    </div>
    """, unsafe_allow_html=True)