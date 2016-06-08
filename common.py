import serial
import const

def on():
    ser.write("run")
def off():
    ser.write("off")
def status():
    ser.write("sta")
    return ser.readline().strip()

ser = serial.Serial(const.serial_port, const.serial_speed, timeout=5)
