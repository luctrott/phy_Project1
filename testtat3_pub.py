from mqtt import MqttPublisher, MqttSubscriber
import time

if __name__ == "__main__":
    publisher = MqttPublisher("192.168.130.12")
    while True:
        publisher.publish("sensor/time",time.time())
        publisher.publish("sensor/status","OK")
        time.sleep(2)