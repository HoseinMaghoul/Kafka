import json
import time
import uuid
import logging
import faker
import random
from datetime import datetime
from kafka import KafkaProducer



logging.basicConfig(level=logging.INFO)


#create kakfa tipic
ORDER_KAFKA_TOPIC = "order-detailes"
ORDER_LIMIT = 15 



producer = KafkaProducer(bootstrap_server="kafka-local.orders-microservice.svc.cluster.local:9092")

def create_orders():
    fakerr = faker.Faker()

    orders = dict(
        order_id = str(uuid.uuid4()),
        username = fakerr.user_name(),
        first_name = fakerr.first_name(),
        last_name = fakerr.last_name(),
        email = fakerr.email(),
        quantity = int(random.randint(1, 999)),
        price = round(float(random.uniform(10.5, 100.99)), 2),
        date_created = str(datetime.utcnow()),
    )

    return orders




if __name__ == "__main__":
    logging.info("Generating Orders....")
    for order in range(ORDER_LIMIT):
        data = create_orders()
        # Send orders to kafka topic
        producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode('utf-8'))
        logging.info(f"Done creating order... {order} - {data}")
        time.sleep(1)
