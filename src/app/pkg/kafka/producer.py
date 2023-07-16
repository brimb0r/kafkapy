import logging
import json
import random

import kafka
from faker import Faker
from confluent_kafka import *

fake = Faker()
logger = logging.getLogger('root')


class Kafka:

    @staticmethod
    def NewProducer():
        kafkaConfig = {
            'bootstrap.servers': 'localhost:9092'
        }
        p = Producer(kafkaConfig)
        logger.info("Kafka Producer Client Init Successfully")
        return p

    @staticmethod
    async def Produce(p: kafka.KafkaProducer):
        for i in range(100):
            data = {
                'user_id': fake.random_int(min=20000, max=100000),
                'user_name': fake.name(),
                'user_address': fake.street_address() + ' | ' + fake.city() + ' | ' + fake.country_code(),
                'platform': random.choice(['Mobile', 'Laptop', 'Tablet']),
                'signup_at': str(fake.date_time_this_month())
            }
            m = json.dumps(data)
            p.produce('user-tracker', m.encode('utf-8'), callback=receipt)
        p.flush()


def receipt(err, msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
