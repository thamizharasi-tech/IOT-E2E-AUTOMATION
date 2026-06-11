from confluent_kafka import Consumer, KafkaException, Producer
import json
import time

from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel
from openpyxl import load_workbook

class Test:

    def test_kafka_consumer(self):

        # Read api test data from excel sheet
        dict = read_api_data_from_excel(self, "KAFKA", "Composite_API_vehicleAlertCount")
        base_url = str(dict["Base Url"])
        endpoint = str(dict["Endpoint"])
        headers = str(dict["Headers"]).replace('\n', '')
        payload = str(dict["Payload"]).replace('\n', '')

        conf = {
            'bootstrap.servers': '34.102.32.103:9094',
            'security.protocol': 'SASL_SSL',
            'sasl.mechanism': 'SCRAM-SHA-512',
            'sasl.username': 'c2c-qc-usw2-qa-reg-kafka-username-secret',
            'sasl.password': 'pKMrEiLnQyIBLGXXeM28C7BzNIeh1ST7',
            'group.id': 'python-secure-consumer',
            'auto.offset.reset': 'earliest',
            'ssl.ca.location': r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\KAFKA\GCP_QA_REG\ca.crt'
        }

        consumer = Consumer(conf)
        topic = 'c2c-qc-usw2-qa-reg-notification-common-out-topic'
        consumer.subscribe([topic])

        print(f"Connecting to topic: {topic}")

        try:
            for i in range(5):  # only try 5 times
                msg = consumer.poll(3.0)  # wait 3s each time
                if msg is None:
                    print(f"Attempt {i + 1}: No message received")
                    continue
                if msg.error():
                    print(f"Kafka error: {msg.error()}")
                else:
                    print(f"Message received: {msg.value().decode('utf-8')}")
                    break
        finally:
            consumer.close()
            print("Consumer closed")

    def test_kafka_producer(self):

        conf = {
            'bootstrap.servers': '34.102.32.103:9094',
            'security.protocol': 'SASL_SSL',
            'sasl.mechanism': 'SCRAM-SHA-512',
            'sasl.username': 'c2c-qc-usw2-qa-reg-kafka-username-secret',
            'sasl.password': 'pKMrEiLnQyIBLGXXeM28C7BzNIeh1ST7',
            'ssl.ca.location': r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\KAFKA\GCP_QA_REG\ca.crt'
        }

        producer = Producer(conf)
        topic = 'c2c-qc-usw2-qa-reg-notification-common-in-topic'

        def delivery_report(err, msg):
            """Called once for each message produced to indicate delivery result."""
            if err is not None:
                print(f"Delivery failed: {err}")
            else:
                print(f"Message delivered to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}")

        # Example message payload (dict -> JSON string)
        data = {
            "meta": {
                "trip_id": "test-trip-123",
                "packet_status": "LIVE"
            },
            "device_id": "QA11182025",
            "system_id": "7641",
            "sub_system_id": "1",
            "sequence": 1
        }

        # Convert to JSON and send
        producer.produce(
            topic,
            key="test-key",
            value=json.dumps(data),
            callback=delivery_report
        )

        # Wait for all messages to be delivered
        producer.flush()



class Test_kafka_ProCon:

    def test_kafka_msg(self):

        # Common Kafka config
        conf = {
            'bootstrap.servers': '34.102.32.103:9094',
            'security.protocol': 'SASL_SSL',
            'sasl.mechanism': 'SCRAM-SHA-512',
            'sasl.username': 'c2c-qc-usw2-qa-reg-kafka-username-secret',
            'sasl.password': 'pKMrEiLnQyIBLGXXeM28C7BzNIeh1ST7',
            'ssl.ca.location': r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\KAFKA\GCP_QA_REG\ca.crt'
        }

        topic = 'c2c-qc-usw2-qa-reg-kafka-navigation-out-topic'

        # ---------------- Producer ----------------
        producer = Producer(conf)

        def delivery_report(err, msg):
            if err is not None:
                print(f"❌ Delivery failed: {err}")
            else:
                print(f"✅ Message delivered to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}")

        # Example message
        data = {
            "meta": {"trip_id": "test-trip-123", "packet_status": "LIVE"},
            "device_id": "QA11182025",
            "system_id": "7641",
            "sub_system_id": "1",
            "sequence": 1
        }

        print("🚀 Producing message...")
        producer.produce(topic, key="test-key", value=json.dumps(data), callback=delivery_report)
        producer.flush()  # make sure it's sent

        # Small wait to ensure message is committed
        time.sleep(2)

        # ---------------- Consumer ----------------
        consumer_conf = conf.copy()
        consumer_conf.update({
            'group.id': 'python-secure-consumer',
            'auto.offset.reset': 'earliest'
        })

        consumer = Consumer(consumer_conf)
        consumer.subscribe([topic])

        print("👂 Listening for the test message...")

        try:
            for _ in range(10):  # try up to 10 polls (≈20s)
                msg = consumer.poll(2.0)
                if msg is None:
                    continue
                if msg.error():
                    print(f"❌ Kafka error: {msg.error()}")
                    continue
                print(f"📩 Consumed: {msg.value().decode('utf-8')}")
                break
        finally:
            consumer.close()
            print("🔒 Consumer closed")


# -----------------------------
# STEP 1: Read Env Name from Excel
# -----------------------------
def get_env_name(file_path, sheet_name="API_Common_Data"):
    wb = load_workbook(file_path)
    sheet = wb[sheet_name]

    for row in sheet.iter_rows(min_row=2, values_only=True):
        attribute, flag, value, *_ = row
        if attribute and attribute.strip().lower() == "test env name":
            return value.strip() if value else None

    raise ValueError("❌ Test Env Name not found in API_Common_Data")

# -----------------------------
# STEP 2: Read Kafka Config & Topic from Excel
# -----------------------------
def get_kafka_conf(file_path, env_name, sheet_name="KAFKA", topic_key="telemetry_navigation_out_topic"):
    wb = load_workbook(file_path)
    sheet = wb[sheet_name]

    kafka_conf = {}
    topic = None

    for row in sheet.iter_rows(min_row=2, values_only=True):
        env, key, value = row
        if env and env.strip().lower() == env_name.strip().lower():
            if key and key.strip().lower() == topic_key.lower():
                topic = value.strip() if value else None
            elif key:
                kafka_conf[key.strip()] = value

    if not kafka_conf:
        raise ValueError(f"No Kafka config found for env '{env_name}'")
    if not topic:
        raise ValueError(f"No topic found for key '{topic_key}' in env '{env_name}'")

    return kafka_conf, topic

# -----------------------------
# STEP 3: Consume Messages from Kafka
# -----------------------------
def consume_kafka(file_path, env_name, max_messages=5, timeout_sec=10):
    topic_key = "telemetry_navigation_out_topic"
    kafka_conf, topic = get_kafka_conf(file_path, env_name, topic_key=topic_key)

    print(f"🔗 Connecting to Kafka: {kafka_conf.get('bootstrap.servers')}")
    print(f"📌 Consuming from Topic: {topic}")

    consumer_conf = {
        'bootstrap.servers': kafka_conf.get("bootstrap.servers"),
        'security.protocol': kafka_conf.get("security.protocol"),
        'sasl.mechanism': kafka_conf.get("sasl.mechanism"),
        'sasl.username': kafka_conf.get("sasl.username"),
        'sasl.password': kafka_conf.get("sasl.password"),
        'ssl.ca.location': kafka_conf.get("ssl.ca.location"),
        'group.id': f"python-secure-consumer",
        'auto.offset.reset': "latest"
    }

    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])

    # Wait for partition assignment
    for _ in range(10):
        time.sleep(1)
        partitions = consumer.assignment()
        if partitions:
            print(f"🧭 Assigned Partitions: {partitions}")
            break
    else:
        print("⚠️ No partitions assigned. Check topic configuration, ACLs, or message activity.")
        consumer.close()
        return

    count = 0
    start_time = time.time()

    try:
        while count < max_messages and (time.time() - start_time) < timeout_sec:
            msg = consumer.poll(0.5)
            if msg is None:
                continue
            if msg.error():
                print(f"❌ Kafka error: {msg.error()}")
                continue

            try:
                payload = json.loads(msg.value().decode("utf-8"))
                print(f"✅ Message {count + 1}: {payload}")
            except Exception as e:
                print(f"⚠️ Decode Error: {e}")
                print(f"⚠️ Raw Message: {msg.value()}")

            count += 1

        if count == 0:
            print(f"⏳ No messages received in {timeout_sec} seconds.")

    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
    finally:
        consumer.close()
        print("🔒 Consumer closed")

# -----------------------------
# Test Class
# -----------------------------
class Test_try3:

    def test_try3(self):

        file_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\API_testData.xlsx"
        dict = read_api_data_from_excel(self, "API_Common_Data", "Test Env Name")
        env_name = str(dict["Value"])
        consume_kafka(file_path, env_name, max_messages=5, timeout_sec=10)
