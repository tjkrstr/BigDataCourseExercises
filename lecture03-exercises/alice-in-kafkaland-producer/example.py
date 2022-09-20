from hdfs import InsecureClient
from kafka import KafkaProducer

# Create an insecure client that can read from HDFS
client = InsecureClient('http://namenode:9870', user='root')

# Read the alice in wonderland text file from HDFS
with client.read('/alice-in-wonderland.txt', encoding='utf-8') as reader:
    # Create a Kafka producer
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    # Read the file line by line
    for line in reader:
        # Send the line to Kafka
        producer.send('alice-in-kafkaland', line.encode('utf-8'))
    # Close the producer
    producer.close()

# Write each sentence in alice in wonderland to a kafka topic with a KafkaProducer
