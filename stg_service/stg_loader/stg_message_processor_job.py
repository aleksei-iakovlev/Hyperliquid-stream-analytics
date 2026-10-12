from hyperliquid.info import Info
from hyperliquid.utils import constants
import json


class StgMessageProcessor:
    def __init__(self, producer) -> None:
        self._producer = producer
        self.info = Info(constants.MAINNET_API_URL, skip_ws=False)
        self.subscription = {"type": "trades", "coin": "BTC"}

    # функция, которая будет вызываться по расписанию.
    def callback(self, message):
        data = message["data"]
        for item in data:
            trades = {"px": item["px"], "sz": item["sz"], "time": item["time"], "tid": item["tid"]}

            with open("data/trades.json", "a", encoding="utf-8") as f:
                json.dump(trades, f, indent=1, ensure_ascii=True)

            self._producer.produce(trades)

    def get_trades(self):
        self.info.subscribe(self.subscription, self.callback)
