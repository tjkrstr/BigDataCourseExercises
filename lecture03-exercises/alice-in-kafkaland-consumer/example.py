from hdfs import InsecureClient
from kafka import KafkaConsumer


# Create a KafkaConsumer that consumes messages from the topic 'alice-in-kafkaland'
consumer = KafkaConsumer('alice-in-kafkaland', bootstrap_servers=['kafka:9092'], group_id='group1')

# # Combine all the messages into a single string
# text = ''
# for msg in consumer:
#     text += msg.value.decode('utf-8')

# # Write the string to HDFS in a file called 'alice-in-kafkaland.txt'
# client = InsecureClient('http://namenode:9870', user='root')
# with client.write('/alice-in-kafkaland.txt', encoding='utf-8', overwrite=True) as writer:
#     writer.write(text)

client = InsecureClient('http://namenode:9870', user='root')
with client.write('/alice-in-kafkaland.txt', encoding='utf-8', overwrite=True) as writer:
    writer.write("")

for msg in consumer:
    print(msg)
    with client.write('/alice-in-kafkaland.txt', encoding='utf-8', append=True) as writer:
        writer.write(msg.value.decode('utf-8'))
