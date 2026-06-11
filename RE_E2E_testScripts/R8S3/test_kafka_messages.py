import sys
import time
import json
from kafka import KafkaConsumer
#from C2CModules.primary_IVI_device_modules import *


def kafka_message(cloudEnv, systemId, count, target):
    # Kafka configuration
    TOPIC = 'cp-re-usw3-rp6-reg-navigation-out-topic'
    BROKER = '34.53.89.1:9094'
    USERNAME = 'cp-re-usw1-dm-reg-kafka-username-secret'
    PASSWORD = 'ClIJYPhsARPCpxEgF0cTEVG17FJ6Nu8v'
    SSL_CAFILE = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\kafka\gcp_qa5_reg_ca_file\ca-cert.pem'

    # Consumer setup
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BROKER,
        security_protocol="SASL_SSL",
        sasl_mechanism="SCRAM-SHA-512",
        sasl_plain_username=USERNAME,
        sasl_plain_password=PASSWORD,
        ssl_cafile=SSL_CAFILE,
        auto_offset_reset='earliest',
        consumer_timeout_ms=2000  # stop iteration after timeout if no messages
    )

    status = ""
    try:
        for msg in consumer:
            # Decode message
            message = msg.value.decode('utf-8', errors='replace')
            json_obj = json.loads(message)

            # Extract fields
            system_id = json_obj['meta']['system_id']
            trip_id = json_obj['meta']['trip_id']
            packet_status = json_obj['meta']['packet_status']
            event_type = json_obj['telemetry'][0]['event_type']

            # Print details
            print('system_id:', system_id)
            print('event_type:', event_type)

            count += 1
            print("Message Count:", count)

            # Check conditions
            if count <= target and systemId == system_id:
                print(
                    f"partition={msg.partition} offset={msg.offset} "
                    f"key={(msg.key.decode('utf-8') if msg.key else None)} "
                    f"value={message}"
                )
                status = "Pass"
                break
            elif count >= target:
                print("No Kafka message found for system Id:", systemId)
                status = "Fail"
                break

        # Final status
        if status == "Pass":
            print("Kafka message is published on desired kafka topic")
        elif status == "Fail":
            print("Kafka message is not published on desired kafka topic")
        else:
            print("Something went wrong while checking kafka message on desired topic")

    finally:
        consumer.close()

    return message, status


class Test_Kafka:

    def test_kafka_message(self):
        # Parameters
        count = 0
        target = 100000
        systemId = "-zZLvtmQ5oEgE4D7OO1Lk"
        cloudEnv = "GCP-QA5"

        message, status = kafka_message(cloudEnv, systemId, count, target)