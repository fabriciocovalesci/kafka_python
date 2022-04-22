
from kafka import KafkaProducer
import json
import ssl
import datetime
from time import sleep
import logging


logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


class Producer:

    def __init__(self, topic: str) -> None:
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        

    def send_message(self, message):
        try:
            self.producer.send(self.topic,value=message)
            self.producer.flush()
            logging.info('Messages sent successfully!!!')
        except Exception as error:
            logging.error(f'{error}')


if __name__ == "__main__":
    producer = Producer('dog')
    producer.send_message('ola')