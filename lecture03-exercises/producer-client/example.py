from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

while True:
    # input
    string = str(input())

    # # output
    # print(string)

    # send
    producer.send('foo', string.encode('utf-8'))
