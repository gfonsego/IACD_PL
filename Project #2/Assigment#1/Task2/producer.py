from kafka import KafkaProducer
import json
import random
import time

# Initialize the Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample users and activities
user_ids = [f"user{i}" for i in range(1, 5)]  # Generate 10 user IDs
activities = ["login", "logout", "purchase", "browse", "signup"]

try:
    while True:
        # Generate a random user activity log
        activity_log = {
            "user_id": random.choice(user_ids),
            "activity": random.choice(activities)
        }
        
        # Send the log to the Kafka topic
        producer.send('task2-topic', value=activity_log)
        print(f"Sent: {activity_log}")
        
        # Wait for a short duration before sending the next log
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\nStopping producer...")
finally:
    producer.flush()
    producer.close()
