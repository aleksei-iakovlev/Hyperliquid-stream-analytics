# Воспользуемся официальным образом для запуска python.
FROM python:3.10

ARG KAFKA_HOST
ARG KAFKA_PORT
ARG KAFKA_CONSUMER_USERNAME
ARG KAFKA_CONSUMER_PASSWORD
ARG KAFKA_CONSUMER_GROUP
ARG KAFKA_SOURCE_TOPIC
ARG KAFKA_DESTINATION_TOPIC

ARG PG_WAREHOUSE_HOST
ARG PG_WAREHOUSE_PORT
ARG PG_WAREHOUSE_DBNAME
ARG PG_WAREHOUSE_USER
ARG PG_WAREHOUSE_PASSWORD

# Обновим компоненты в контейнере.
RUN apt-get update -y

# Копируем все файлы в контейнер.
COPY . .

# Запускаем установку зависимостей.
RUN pip install -r requirements.txt

# Переходим в директорию src
WORKDIR /src

# Говорим, что запускать будем python.
ENTRYPOINT ["python"]

# А именно, файл app.py в директории src.
CMD ["app.py"]