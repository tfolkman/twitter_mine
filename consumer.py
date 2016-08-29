from kafka import KafkaConsumer


consumer = KafkaConsumer('twitter-stream')
for msg in consumer:
    print(msg)