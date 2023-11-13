# Name of the motor
MOTOR_NAME = "motorix"
# Settings for connecting the client to the broker
# Change this to your pi after setting up the broker
BROKER = "10.1.48.108"
# topic for controlling the motor
TOPIC_MOTOR = f'motors/{MOTOR_NAME}/control'
# pin config for the motor
MOTOR_IX_PIN = 17
MOTOR_IX_ID = 1
MOTOR_IX_FREQ = 100

DB_NAME = "db.db"
 