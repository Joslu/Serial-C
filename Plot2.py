import serial
import numpy as np     
import matplotlib.pyplot as plt 

ser = serial.Serial('COM5', 115200)
ser.flushInput()

len = 10001


while True:

    try:
        ##ser_bytes = ser.readline()
        arduino = ser.readline()
        arduinoString = arduino.decode('cp1252')
        print(arduinoString)
        
    
    except KeyboardInterrupt:
        print("Keyboard Interrupt D:")
        break

