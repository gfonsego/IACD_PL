import json
from kafka import KafkaConsumer

# Initialize the Kafka consumer
consumer = KafkaConsumer(
    'task1-topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Consume messages from the topic and print them
for message in consumer:
    temperature_data = message.value
    print(f"Received: {temperature_data}")
