1. Start Zookeeper
`sudo systemctl start zookeeper`

2. Start Kafka
`sudo systemctl start kafka`

3. Create a Kafka Topic
`kafka-topics --create --topic task1-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`

4. Run Kafka Producer
`python kafka_producer.py`

5. Run Kafka Consumer
`python kafka_consumer.py`

**Results**

* The information received by the consumer is exactly the same as the one sent by the producer.