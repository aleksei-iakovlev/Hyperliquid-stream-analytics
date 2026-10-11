import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from src.app_config import AppConfig
from src.stg_loader.stg_message_processor_job import StgMessageProcessor
from src.stg_loader.repository.stg_repository import StgRepository

app = Flask(__name__)


# Заводим endpoint для проверки, поднялся ли сервис.
# Обратиться к нему можно будет GET-запросом по адресу localhost:5000/health.
# Если в ответе будет healthy - сервис поднялся и работает.
@app.get('/health')
def health():
    return 'healthy'


if __name__ == '__main__':
    # Устанавливаем уровень логгирования в Debug, чтобы иметь возможность просматривать отладочные логи.
    app.logger.setLevel(logging.DEBUG)

    # Инициализируем конфиг. Для удобства, вынесли логику получения значений переменных окружения в отдельный класс.
    config = AppConfig()
    # producer = config.kafka_producer()
    repository = StgRepository(config.pg_warehouse_db())

    # Инициализируем процессор сообщений.
    proc = StgMessageProcessor(repository, app.logger)

    # Запускаем процессор в бэкграунде.
    # BackgroundScheduler будет по расписанию вызывать функцию run нашего обработчика.
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=proc.get_trades)
    scheduler.start()

    # стартуем Flask-приложение.
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
