from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# ----------------------------------------
# Generic AI Function
# ----------------------------------------

def ask_ai(prompt):

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        error = str(e)

        if "429" in error or "rate_limit" in error.lower():
            return "⚠️ AI service is busy. Please wait a few seconds and try again."

        elif "401" in error or "authentication" in error.lower():
            return "🔑 Invalid API Key. Please check your .env file."

        elif "404" in error:
            return "⚠️ AI model not found."

        else:
            return f"⚠️ Something went wrong.\n\n{error}"


# ----------------------------------------
# AI Categorization
# ----------------------------------------

def categorize_transaction(description):

    prompt = f"""
You are an intelligent financial assistant.

Categorize this bank transaction into exactly ONE category.

Categories:
- Food
- Transport
- Shopping
- Entertainment
- Housing
- Bills
- Healthcare
- Salary
- Education
- Investment
- Travel
- Other

Transaction:
{description}

Return ONLY the category name.
"""

    return ask_ai(prompt).strip()


# ----------------------------------------
# Spending Insights
# ----------------------------------------

def generate_spending_insights(df):

    data = df.to_string(index=False)

    prompt = f"""
Analyze this bank statement.

{data}

Provide:
- Highest spending category
- Biggest expense
- Spending pattern
- Saving suggestions
- Financial Health Score out of 10

Use bullet points.
"""

    return ask_ai(prompt)
# ----------------------------------------
# Fraud Detection
# ----------------------------------------

def detect_fraud(df):

    data = df.to_string(index=False)

    prompt = f"""
You are an expert financial fraud detection analyst.

Analyze this bank statement:

{data}

Provide:

- Suspicious transactions
- Unusually large expenses
- Duplicate transactions
- Possible fraud patterns
- Fraud Risk Score (out of 10)

Keep the answer short.
Use bullet points.
"""

    return ask_ai(prompt)


# ----------------------------------------
# Budget Planner
# ----------------------------------------

def generate_budget_plan(df):

    data = df.to_string(index=False)

    prompt = f"""
You are an expert financial planner.

Analyze this bank statement:

{data}

Create a personalized monthly budget.

Include:

- Estimated Monthly Income
- Housing Budget
- Food Budget
- Transport Budget
- Shopping Budget
- Entertainment Budget
- Savings Recommendation
- Emergency Fund Recommendation
- Budget Score (out of 10)

Use bullet points.
"""

    return ask_ai(prompt)


# ----------------------------------------
# Financial Health
# ----------------------------------------

def generate_health_score(df):

    data = df.to_string(index=False)

    prompt = f"""
You are a certified financial advisor.

Analyze this bank statement:

{data}

Provide:

- Financial Health Score (out of 10)
- Strengths
- Weaknesses
- Risks
- Top 5 Recommendations

Keep the answer short.
Use bullet points.
"""

    return ask_ai(prompt)