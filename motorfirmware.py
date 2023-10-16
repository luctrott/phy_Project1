from gpiozero import PWMOutputDevice
from mqtt import MqttSubscriber
import config

class MotorFirmware:
    def __init__(self,topic,pin,address) -> None:
        self.topic = topic
        self.motor = PWMOutputDevice(pin)
        self.motor.value = 0
        self.mqtt = MqttSubscriber(address)
        self.mqtt.change_callback(self.on_message)
        self.mqtt.subscribe(topic)
    
    def on_message(self, client, userdata, message):
        tmp=float(message.payload.decode("utf-8"))
        if tmp >= 0 and tmp <= 1:
            self.motor.value = tmp
        else:
            print("Value not in range")
    def close(self):
        self.mqtt.close()
        self.motor.close()

if __name__ == "__main__":
    motor = MotorFirmware(config.TOPIC_MOTOR,config.MOTOR_IX_PIN,config.BROKER)
    input("Press Enter to continue...")
    motor.close()