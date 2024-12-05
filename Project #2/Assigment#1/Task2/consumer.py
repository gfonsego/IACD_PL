from kafka import KafkaConsumer
import sys
import json

def consume(group_id, consumer_id):
    consumer = KafkaConsumer(
        'task2-topic',
        bootstrap_servers='localhost:9092',
        group_id=group_id,
        auto_offset_reset='earliest',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )
    print(f"Consumer {consumer_id} listening...")

    try:
        for message in consumer:
            print(f"Consumer {consumer_id} received: {message.value}")
    except KeyboardInterrupt:
        print(f"Consumer {consumer_id} stopped.")
    finally:
        consumer.close()

if __name__ == "__main__":
    group_id = sys.argv[1]
    consumer_id = sys.argv[2]
    consume(group_id, consumer_id)
