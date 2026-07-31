import streamlit as st


def show_budget_tracker(filtered_df):

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#10B981,#059669,#2563EB);
        padding:35px;
        border-radius:25px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    ">
        <h1>🎯 Budget Tracker</h1>
        <p style="font-size:18px;">
            Track your monthly spending, monitor your remaining budget,
            and stay on top of your financial goals.
        </p>
    </div>
    """, unsafe_allow_html=True)

    budget = st.number_input(
        "💰 Enter Monthly Budget (₹)",
        min_value=0.0,
        value=50000.0,
        step=1000.0,
    )

    expense = abs(
        filtered_df[filtered_df["Amount"] < 0]["Amount"].sum()
    )

    remaining = budget - expense

    progress = 0

    if budget > 0:
        progress = min(expense / budget, 1.0)

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("💸 Total Spent", f"₹{expense:,.2f}")

    with c2:
        st.metric("💰 Remaining", f"₹{remaining:,.2f}")

    with c3:
        st.metric("📊 Budget Used", f"{progress*100:.1f}%")

    st.write("")

    st.markdown("### 📈 Budget Progress")

    st.progress(progress)

    if progress < 0.50:
        st.success("🟢 Excellent! You're using less than 50% of your budget.")

    elif progress < 0.80:
        st.info("🟡 You're on track. Keep monitoring your spending.")

    elif progress < 1.0:
        st.warning("🟠 You've used most of your budget. Spend carefully.")

    else:
        st.error("🔴 Budget exceeded! Consider reducing discretionary spending.")

    st.markdown("---")

    st.markdown("### 💡 Budget Tips")

    tip1, tip2 = st.columns(2)

    with tip1:
        st.success("✅ Review subscriptions regularly")
        st.success("✅ Track large purchases")
        st.success("✅ Save before you spend")

    with tip2:
        st.info("💰 Set aside emergency savings")
        st.info("📊 Monitor monthly trends")
        st.info("🎯 Update your budget every month")

    st.markdown("""
    <div style="
        background:rgba(255,255,255,.05);
        padding:20px;
        border-radius:20px;
        text-align:center;
        margin-top:20px;
    ">
        <b>🎯 Goal:</b> Staying within your monthly budget is one of the easiest ways to improve long-term financial health.
    </div>
    """, unsafe_allow_html=True)