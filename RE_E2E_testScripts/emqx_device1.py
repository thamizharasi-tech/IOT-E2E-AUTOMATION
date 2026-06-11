import random
from paho.mqtt import client as mqtt_client
import ssl

#broker = 'i7e1598e.ala.dedicated.gcp.emqxcloud.com'
#broker = 'a3ca7e6f.ala.dedicated.gcp.emqxcloud.com'
broker = 'q46bbf98.ala.dedicated.gcp.emqxcloud.com'
port = 443
topic = "reg_v2/20ad2b40d37cef5ab987b493e16399cdc042f3875aa7d4d95b708e4f46f75bfa/testdevice/out"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'cbp2admin'
password = 'cbp@admin'


def connect_mqtt() -> mqtt_client:
    client = mqtt_client.Client()
    client.tls_set(ca_certs=r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re_replica2_default_certs\cacert.pem.crt',
                   certfile=r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re_replica2_default_certs\clientcert.pem.crt',
                   keyfile=r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\re_replica2_default_certs\private.pem.key',
                   tls_version=ssl.PROTOCOL_TLSv1_2)
    #client.tls_insecure_set(True)
    client.username_pw_set(username, password)

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe(topic)  # Subscribe here upon connection
        else:
            print(f"Failed to connect, return code {rc}")

    client.on_connect = on_connect
    client.on_message = on_message  # Set the message callback

    client.connect(broker, port)
    return client


def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")


def run():
    client = connect_mqtt()
    client.loop_forever()


if __name__ == '__main__':
    run()
