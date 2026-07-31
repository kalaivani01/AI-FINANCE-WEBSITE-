import streamlit as st
from src.qa_engine import ask_ai


def show_ask_ai(filtered_df):

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#2563EB,#7C3AED,#06B6D4);
        padding:35px;
        border-radius:25px;
        text-align:center;
        color:white;
        margin-bottom:25px;
    ">
        <h1>🤖 AI Financial Assistant</h1>
        <p style="font-size:18px;">
            Ask questions about your uploaded bank statement and receive AI-powered answers.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 💬 Ask Anything")

    question = st.text_input(
        "",
        placeholder="Example: What was my highest expense this month?"
    )

    col1, col2 = st.columns([4, 1])

    with col2:
        ask = st.button("🚀 Ask AI", use_container_width=True)

    if ask:

        if question.strip() == "":
            st.warning("Please enter a question.")
            return

        data = filtered_df.to_string(index=False)

        prompt = f"""
You are an expert financial analyst.

Here is my bank statement:

{data}

Question:
{question}

Answer only using the uploaded bank statement.
"""

        with st.spinner("🤖 AI is thinking..."):

            answer = ask_ai(prompt)

        st.markdown("## 🤖 AI Response")

        st.markdown(f"""
<div style="
background:rgba(255,255,255,.08);
padding:30px;
border-radius:20px;
border:1px solid rgba(255,255,255,.1);
margin-top:10px;
">
{answer}
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
💡 <b>Try asking:</b><br><br>

• What is my largest expense?<br>
• Which category has the highest spending?<br>
• How much did I spend on food?<br>
• Which merchant appears most often?<br>
• Did I save more than I spent?
</div>
""", unsafe_allow_html=True)