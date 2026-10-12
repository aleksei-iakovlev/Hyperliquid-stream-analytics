import json
from typing import Dict

from confluent_kafka import Producer


def error_callback(err):
    print('Something went wrong: {}'.format(err))


class KafkaProducer:
    def __init__(self, host: str, port: int, topic: str) -> None:
        params = {
            'bootstrap.servers': f'{host}:{port}',
            'error_cb': error_callback,
        }

        self.topic = topic
        self.p = Producer(params)

    def produce(self, payload: Dict) -> None:
        self.p.produce(self.topic, json.dumps(payload))
        self.p.flush(10)
