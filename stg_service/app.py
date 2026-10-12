import signal
import threading

from app_config import AppConfig
from stg_loader.stg_message_processor_job import StgMessageProcessor


if __name__ == "__main__":
    config = AppConfig()
    producer = config.kafka_producer()
    processor = StgMessageProcessor(producer)

    stop_event = threading.Event()
    signal.signal(signal.SIGTERM, lambda *_: stop_event.set())
    signal.signal(signal.SIGINT, lambda *_: stop_event.set())

    try:
        # Hyperliquid subscriptions are long-lived and should be registered once.
        processor.get_trades()
        stop_event.wait()
    finally:
        processor.info.disconnect_websocket()
