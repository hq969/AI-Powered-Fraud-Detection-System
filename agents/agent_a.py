from typing import Dict

def detect_fraud(transaction: Dict) -> Dict:
    """
    Apply rule-based fraud checks
    """
    result = {"transaction_id": transaction["id"], "is_fraud": False, "reasons": []}

    # Example rules
    if transaction["amount"] > 10000:
        result["is_fraud"] = True
        result["reasons"].append("High transaction amount")
    if transaction["location"] != transaction["account_location"]:
        result["is_fraud"] = True
        result["reasons"].append("Location mismatch")
    
    return result
