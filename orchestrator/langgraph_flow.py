from agents.agent_a import detect_fraud
from agents.agent_b import explain_anomaly
from agents.agent_c import log_to_redshift

def process_transaction(transaction):
    fraud_result = detect_fraud(transaction)
    explanation = explain_anomaly(fraud_result)
    log_to_redshift(fraud_result, explanation)
    return {"fraud_result": fraud_result, "explanation": explanation}
