import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_anomaly(fraud_result: dict) -> str:
    """
    Generate natural language explanation using LLM
    """
    if not fraud_result["is_fraud"]:
        return "Transaction appears normal."
    
    prompt = f"Explain the following fraud reasons in simple language: {fraud_result['reasons']}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
