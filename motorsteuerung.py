from mqtt import MqttPublisher
import config

class Controler:
    def __init__(self,address:str) -> None:
        self.mqtt = MqttPublisher(address)
    def set_motor_ix(self,value:float):
        self.mqtt.publish(config.TOPIC_MOTOR,str(value))
    def close(self):
        self.mqtt.close()

if __name__ == '__main__':
    c=Controler(config.BROKER)
    while True:
        try:
            tmp=float(input("Enter value: "))
            c.set_motor_ix(tmp)
        except ValueError:
            print("Value not a valide")
        except KeyboardInterrupt:
            break
    c.close()