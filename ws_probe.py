import json
import time

from hyperliquid.info import Info
from hyperliquid.utils import constants

COIN = "BTC"
MAX_MESSAGES = 10

info = Info(constants.MAINNET_API_URL, skip_ws=False)
subscription = {"type": "trades", "coin": COIN}


def callback(message):
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


def get_trades(subscription, duration=5):
    subscription_id = info.subscribe(subscription, callback)
    time.sleep(duration)
    info.unsubscribe(subscription, subscription_id)
    info.ws_manager.stop()


if __name__ == '__main__':
    stream = get_trades(subscription, 10)
