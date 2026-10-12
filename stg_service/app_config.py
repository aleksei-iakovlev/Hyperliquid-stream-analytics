import os
from lib.kafka_connect import KafkaProducer
from dotenv import load_dotenv


class AppConfig:

    def __init__(self) -> None:
        load_dotenv()
        self.kafka_host = os.getenv("KAFKA_HOST", "localhost")
        self.kafka_port = int(os.getenv("KAFKA_PORT", "9092"))
        self.kafka_producer_topic = os.getenv(
            "KAFKA_STG_SERVICE_TOPIC", "stg-service-topic"
        )

    def kafka_producer(self):
        return KafkaProducer(
            self.kafka_host,
            self.kafka_port,
            self.kafka_producer_topic
        )
