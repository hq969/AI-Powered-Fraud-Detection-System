from utils.redshift_client import get_redshift_connection

def log_to_redshift(fraud_result: dict, explanation: str):
    conn = get_redshift_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO fraud_logs (transaction_id, is_fraud, reasons, explanation)
        VALUES (%s, %s, %s, %s)
    """, (fraud_result["transaction_id"], fraud_result["is_fraud"], str(fraud_result["reasons"]), explanation))
    conn.commit()
    cur.close()
    conn.close()
