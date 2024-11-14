import json
from kafka import KafkaConsumer
from collections import defaultdict

# Initialize the Kafka consumer for purchase-topic
consumer = KafkaConsumer(
    'purchase-topic',
    bootstrap_servers='localhost:9092',
    group_id='purchase-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Dictionary to keep track of total amount spent per user
user_total_spent = defaultdict(float)

# Consume messages and calculate running total
for message in consumer:
    purchase = message.value
    user_id = purchase["user_id"]
    amount = purchase["amount"]
    
    user_total_spent[user_id] += amount
    print(f"User {user_id} Total Spent: {user_total_spent[user_id]}")

