from mqtt import MqttSubscriber
import config
import sqlite3
import time

class MotorSub(MqttSubscriber):
    def __init__(self, broker:str, topic:str, db:str)->None:
        super().__init__(broker, topic)
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()
        self.subscribe(topic)

        

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
    
    def run(self):
        self.client.loop_forever()
    
    def __del__(self):
        self.conn.close()
        self.client.disconnect()

if __name__ == "__main__":
    motor = MotorSub(config.BROKER, config.TOPIC_MOTOR, config.DB_NAME)
    motor.run()