import os

from src.lib.kafka_connect import KafkaProducer
from src.lib.pg import PgConnect
from dotenv import load_dotenv


class AppConfig:
    CERTIFICATE_PATH = ''
    DEFAULT_JOB_INTERVAL = 25
    load_dotenv()

    def __init__(self) -> None:

        self.kafka_host = str(os.getenv('KAFKA_HOST') or "")
        self.kafka_port = int(os.getenv('KAFKA_PORT') or 0)
        self.kafka_producer_username = str(os.getenv('KAFKA_USERNAME') or "")
        self.kafka_producer_password = str(os.getenv('KAFKA_PASSWORD') or "")
        self.kafka_producer_topic = str(os.getenv('KAFKA_STG_SERVICE_TOPIC') or "")

        self.pg_warehouse_host = str(os.getenv('PG_WAREHOUSE_HOST') or "")
        self.pg_warehouse_port = int(os.getenv('PG_WAREHOUSE_PORT') or 0)
        self.pg_warehouse_dbname = str(os.getenv('PG_WAREHOUSE_DBNAME') or "")
        self.pg_warehouse_user = str(os.getenv('PG_WAREHOUSE_USER') or "")
        self.pg_warehouse_password = str(os.getenv('PG_WAREHOUSE_PASSWORD') or "")

    def kafka_producer(self):
        return KafkaProducer(
            self.kafka_host,
            self.kafka_port,
            self.kafka_producer_username,
            self.kafka_producer_password,
            self.kafka_producer_topic,
            self.CERTIFICATE_PATH
        )

    def pg_warehouse_db(self):
        return PgConnect(
            self.pg_warehouse_host,
            self.pg_warehouse_port,
            self.pg_warehouse_dbname,
            self.pg_warehouse_user,
            self.pg_warehouse_password
        )
