# Name of the motor
MOTOR_NAME = "motorix"
# Settings for connecting the client to the broker
# Change this to your pi after setting up the broker
BROKER = "192.168.130.12"
# topic for controlling the motor
TOPIC_MOTOR = f'motors/{MOTOR_NAME}/control'
# pin config for the motor
MOTOR_IX_PIN = 17
 