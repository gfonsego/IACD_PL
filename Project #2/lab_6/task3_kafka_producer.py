import json
import random
import time
from kafka import KafkaProducer

# Initialize the Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Define sample items and activities
items = ["book", "laptop", "phone", "headphones"]
activities = ["login", "page_view", "add_to_cart", "checkout"]

# Send random purchase transactions and user activities every 2 seconds
while True:
    # Send a purchase transaction to purchase-topic
    purchase_data = {
        "user_id": f"user{random.randint(1, 5)}",
        "amount": round(random.uniform(10, 100), 2),
        "item": random.choice(items)
    }
    producer.send('purchase-topic', purchase_data)
    print(f"Sent purchase: {purchase_data}")

    # Send a user activity to user-activity-topic
    activity_data = {
        "user_id": f"user{random.randint(1, 5)}",
        "activity": random.choice(activities)
    }
    producer.send('user-activity-topic', activity_data)
    print(f"Sent activity: {activity_data}")

    time.sleep(2)
