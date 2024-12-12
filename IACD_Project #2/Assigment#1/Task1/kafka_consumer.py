from kafka import KafkaConsumer
import json

# Set up Kafka consumer
consumer = KafkaConsumer(
    'task1-topic',  # Topic to subscribe to
    bootstrap_servers='localhost:9092',  # Kafka broker address
    group_id='temperature-consumer-group',  # Consumer group ID
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON messages
)

# Consume messages from 'task1-topic' and print them
for message in consumer:
    print(f"Received message: {message.value}")
