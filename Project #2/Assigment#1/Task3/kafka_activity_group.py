import json
from kafka import KafkaConsumer
from collections import defaultdict


# Initialize the Kafka consumer for user-activity-topic
consumer = KafkaConsumer(
    'user-activity-topic',
    bootstrap_servers='localhost:9092',
    group_id='activity-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)


# Dictionary to keep track of activity count per user
user_activity_count = defaultdict(int)


# Consume messages and count activities per user
for message in consumer:
    activity = message.value
    user_id = activity["user_id"]
    
    user_activity_count[user_id] += 1
    print(f"User {user_id} Activity Count: {user_activity_count[user_id]}")