from streams.kafka_consumer import consume_transactions
from orchestrator.langgraph_flow import process_transaction

def main():
    for transaction in consume_transactions():
        result = process_transaction(transaction)
        print(f"Processed Transaction {transaction['id']}: {result['fraud_result']['is_fraud']}")

if __name__ == "__main__":
    main()
