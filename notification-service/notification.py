import json 
import logging
from kafka import KafkaConsumer


logging.basicConfig(level=logging.INFO)

ORDER_PROCESSED_KAFKA_TOPIC = "order-processed"
BOOT_STRAP_SERVER = "kafka-local.orders-microservice.svc.cluster.local:9092"


# consumer 
consumer = KafkaConsumer(
    ORDER_PROCESSED_KAFKA_TOPIC,
    bootstrap_servers = BOOT_STRAP_SERVER

)



if __name__ == "__main__":
    email_sent = set()
    logging.info("started Sendding out email....")
    while True:
        for message in consumer:
            consumed_message = json.loads(message.value.decode("utf-8"))
            customer_email = consumed_message["email"]
            logging.info(f"Sending email to: {customer_email}")
            email_sent.add(customer_email)
            logging.info(f"Number of email sent to far: {len(email_sent)}")

