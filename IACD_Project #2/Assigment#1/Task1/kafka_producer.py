from kafka import KafkaProducer
import json
import time
import random

# Initialize the Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Continuously send temperature readings every 2 seconds
sensor_id = 1
try:
    while True:
        temperature_reading = {
            "sensor_id": sensor_id,
            "temperature": round(random.uniform(15.0, 35.0), 1)  # Generate a random temperature
        }
        
        producer.send('task1-topic', value=temperature_reading)
        print(f"Sent: {temperature_reading}")
        time.sleep(2)
        
except KeyboardInterrupt:
    print("Producer stopped.")
finally:
    producer.close()