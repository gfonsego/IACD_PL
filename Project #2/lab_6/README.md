# Lab 6

## Step by Step

1. Start Zookeeper
`brew services start zookeeper`

2. Start Kafka
`brew services start kafka`

**TASK1**

3. Create a Kafka Topic
`kafka-topics --create --topic task1-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`

4. Write Kafka Producer
File: `task1_kafka_producer.py`

5. Write Kafka Consumer
File: `task1_kafka_consumer.py`

**TASK2**


**TASK3**

1. Create Kafka Topics: Purchase and User-Activity
`kafka-topics --create --topic purchase-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
`kafka-topics --create --topic user-activity-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`

2. Run Kafka Producer
File: `task3_kafka_producer.py`

3. Run Kafka Purchase Group
File: `task3_kafka_purchase_group.py`

3. Run Kafka Activity Group
File: `task3_kafka_activity_group.py`

## Results

### Task 1

* The information received by the consumer is exactly the same as the one sent by the producer.

### Task 2

### Task 3

* Each message will be processed according to the consumer group it belongs to, demonstrating how Kafka can handle multiple topics and consumer groups for different types of data processing.
