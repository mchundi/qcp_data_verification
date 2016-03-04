from kafka import KafkaClient, SimpleConsumer
#import logging

#define and open Kafka consumer
def kafkaConnection():
    kafka = KafkaClient('99.192.203.99:9092')
    kafka.close();
    
def consumerProducer():
    consumer = SimpleConsumer(KafkaClient('99.192.203.99:9092'), "test-group", "qubit10",iter_timeout=10)
    #consumer=KafkaConsumer('qubit10', bootstrap_servers=['99.192.203.99:9092']);
    return consumer;

def consumerProcessor():
    #consumer = KafkaConsumer('qubitProcessor', bootstrap_servers=['99.192.203.99:9092']);
    consumer = SimpleConsumer(KafkaClient('99.192.203.99:9092'), "test-group", "qubitProcessor",iter_timeout=10)
    return consumer

def payloadConsumer(consumer):
    
    print 'in payloadConsumer'
    #consumer.max_buffer_size=0
    consumer.seek(0,0)
    
    #Log kafka error message
    #logging.basicConfig(
    #format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    #level=logging.DEBUG)
    
    messageCount=0
    for message in consumer: 
        #print "message:"
        print (message[1][3]) 
        if message[1][3]:
            messageCount += 1 
    print ("messageCount: {0}" .format(messageCount))
    print 'returning from payloadConsumer'
    return messageCount;