import sys
import time
from kafka import KafkaConsumer
import json
import logging
logging.basicConfig(level=logging.DEBUG)

# BROKER = "localhost:9092"     # change to your broker(s)
TOPIC = 'cp-re-usw3-rp6-reg-navigation-out-topic'
# GROUP_ID = "first-10-reader-" + str(int(time.time()))

consumer = KafkaConsumer(
    'cp-re-usw3-rp6-reg-navigation-out-topic',
    bootstrap_servers='34.53.89.1:9094',
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-512",  # could also be GSSAPI or SCRAM-SHA-256 depending on your Kafka setup
    sasl_plain_username='cp-re-usw1-dm-reg-kafka-username-secret',
    sasl_plain_password='ClIJYPhsARPCpxEgF0cTEVG17FJ6Nu8v',
    ssl_cafile=r'C:\Users\slua_2bdaff993902\PycharmProjects\Car2CloudE2ETesting\RE_E2E_testScripts\R8S3\ca-cert.pem',  # From your truststore or exported from the .jks
    auto_offset_reset='earliest',
    consumer_timeout_ms=2000,  # stop iteration after timeout if no messages
)

count = 0
target = 1000

systemId = "ghtvw3-GuYC5rfmqjqqei"
status = ""

try:
    for msg in consumer:
        # msg is a ConsumerRecord
        # print(f"{msg.partition}:{msg.offset} v={msg.value}")
        message = msg.value.decode('utf-8', errors='replace')
        json_obj = json.loads(message)
        system_id = json_obj['meta']['system_id']
        trip_id = json_obj['meta']['trip_id']
        packet_status = json_obj['meta']['packet_status']
        event_type = json_obj['telemetry'][0]['event_type']
        print('system_id : ', system_id)
        print('event_type : ', event_type)
        count += 1
        print("Message Count : ", count)
        if count <= target and systemId == system_id:
            print(
                f"partition={msg.partition} offset={msg.offset} "
                f"key={(msg.key.decode('utf-8') if msg.key else None)} "
                f"value={msg.value.decode('utf-8', errors='replace')}"
            )
            status = "Pass"
            break
        elif count >= target:
            print("No Kafka message is found for system Id : ",systemId)
            status = "Fail"
            break

    if status == "Pass":
        print("Kafka message is published on desired kafka topic")
    elif status == "Fail":
        print("Kafka message is not published on desired kafka topic")
    else:
        print("Something went wrong while checking kafka message on desired topic")

finally:
    consumer.close()

