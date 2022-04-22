from kafka import KafkaConsumer
from json import loads
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

class Consumer:
    
    def __init__(self, topic: str) -> None:
        self.topic = topic
        
    def create_consumer(self):
        try:
            consumer = KafkaConsumer(self.topic,
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                bootstrap_servers=['localhost:9092'], 
                value_deserializer=lambda x: loads(x.decode('utf-8')))
            for message in consumer:
                logging.info(f'Message: {message.value} | Topic: {message.topic}')
        except Exception as err:
            logging.exception(f'Error connect or send message: {err}')



if __name__ == "__main__":
    consumer = Consumer('dog')
    consumer.create_consumer()