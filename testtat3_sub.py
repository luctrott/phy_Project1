from mqtt import MqttPublisher, MqttSubscriber
import time

if __name__ == "__main__":
    subscriber = MqttSubscriber("192.168.130.12")
    subscriber.subscribe("sensor/time")
    subscriber.subscribe("sensor/status")
    input("Press Enter to exit\n")
