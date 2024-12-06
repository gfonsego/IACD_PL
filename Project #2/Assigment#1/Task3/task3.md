1. Start Zookeeper
`sudo systemctl start zookeeper`

2. Start Kafka
`sudo systemctl start kafka`


3. Create Kafka Topics: Purchase and User-Activity
`kafka-topics --create --topic purchase-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
`kafka-topics --create --topic user-activity-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`


4. Run Kafka Producer
File: `kafka_producer.py`


5. Run Kafka Purchase Group
File: `kafka_purchase_group.py`


6. Run Kafka Activity Group
File: `kafka_activity_group.py`


**Results**

* Each message will be processed according to the consumer group it belongs to, demonstrating how Kafka can handle multiple topics and consumer groups for different types of data processing.