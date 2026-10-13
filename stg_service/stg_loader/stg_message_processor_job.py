from hyperliquid.info import Info
from hyperliquid.utils import constants
import json


class StgMessageProcessor:
    def __init__(self, producer) -> None:
        self._producer = producer
        self.info = Info(constants.MAINNET_API_URL, skip_ws=False)
        self.subscription = {"type": "trades", "coin": "BTC"}

    def callback(self, message):
        data = message.get("data", [])
        with open("data/trades.jsonl", "a", encoding="utf-8") as f:
            for item in data:
                trades = {"object_id": item["tid"],  "recieved_at": datetime.now(timezone.utc), "object_value": {"px": item["px"], "sz": item["sz"], "time": item["time"], "tid": item["tid"]}}
                f.write(json.dumps(trade) + "\n")
                self._producer.produce(trades)

    def get_trades(self):
        self.info.subscribe(self.subscription, self.callback)
