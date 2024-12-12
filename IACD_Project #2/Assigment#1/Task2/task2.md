
1. ## Start Zookeeper and Kafka
  
  `sudo systemctl start zookeeper`

  `sudo systemctl start kafka`

2. ## Create a Kafka Topic
  
  `bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --topic task2-topic --partitions 3 --replication-factor 1`

3. ## Run Kafka Producer File: 
   
   `python3 producer.py` 

4. ## Behavior #1 -> Three consumers in activity-group are active:
   
    `python consumer.py activity-group consumer1`

    `python consumer.py activity-group consumer2`

    `python consumer.py activity-group consumer3`

    #### Each consumer consumes from 1 partition 

5. ## Behavior #2 -> Two consumers in activity-group are active:

    `python consumer.py activity-group consumer1`

    `python consumer.py activity-group consumer2`

    #### One consumer consumes from 2 partitions and the other consumes from the left partition
6. ## Behavior #1 -> Three consumers in activity-group are active:
   
    `python consumer.py activity-group consumer1`

    `python consumer.py activity-group consumer2`

    `python consumer.py activity-group consumer3`

    `python consumer.py activity-group consumer4`

    #### Only 3 consumers are able to consume and the 4th consumer dont consume from any partition 

