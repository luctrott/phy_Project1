from gpiozero import DigitalOutputDevice
motor=DigitalOutputDevice(4)

motor.blink()
input("Press Enter to Exit")
motor.off()
motor.close()