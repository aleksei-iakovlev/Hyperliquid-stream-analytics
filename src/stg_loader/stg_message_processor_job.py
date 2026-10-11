import time
from logging import Logger
from src.lib.kafka_connect import KafkaProducer
from src.stg_loader.repository.stg_repository import StgRepository
from hyperliquid.info import Info
from hyperliquid.utils import constants


class StgMessageProcessor:
    def __init__(self,
                 repository: StgRepository,
                 logger: Logger) -> None:
        # self._producer = producer
        self._repository = repository
        self._logger = logger
        self.info = Info(constants.MAINNET_API_URL, skip_ws=False)
        self.subscription = {"type": "trades", "coin": "BTC"}

    # функция, которая будет вызываться по расписанию.
    def callback(self, message):
        # trades = json.dumps(message, ensure_ascii=False)
        data = message["data"]
        for item in data:
            result = {
                "px": item["px"],
                "sz": item["sz"],
                "time": item["time"],
                "tid": item["tid"]
            }
            print(result)
            # self._producer.produce(result)

    def get_trades(self):
        self.info.subscribe(self.subscription, self.callback)

