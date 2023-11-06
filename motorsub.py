from mqtt import MqttSubscriber
import config
import sqlite3
import time

class MotorSub:
    def __init__(self, broker:str, topic:str, db:str)->None:
        self.client = MqttSubscriber(broker)
        self.db = db
        self.conn = sqlite3.connect(self.db, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.client.change_callback(self.on_message)
        self.client.subscribe(topic)

        

    def on_message(self, client, userdata, message):
        data = message.payload.decode()
        print(f"received message {data}")
        self.add_to_db(data)
        for i in self.get():
            print(i)
    

    def add_to_db(self, data):
        self.cur.execute("INSERT INTO nachricht (zeitstempel, nachricht,motor_id) VALUES (?,?,?)", (time.time(), data, config.MOTOR_IX_ID))
        self.conn.commit()

    def get (self):
        self.conn.commit()
        self.cur.execute("SELECT * FROM nachricht")
        return self.cur.fetchall()
    
    
    
if __name__ == "__main__":
    motor = MotorSub(config.BROKER, config.TOPIC_MOTOR, config.DB_NAME)
    input("Press Enter to continue...")