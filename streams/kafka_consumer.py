from kafka import KafkaConsumer
import json

def consume_transactions(topic="transactions", bootstrap_servers="localhost:9092"):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        value_deserializer=lambda m: json.loads(m.decode("utf-8"))
    )
    for message in consumer:
        yield message.value
