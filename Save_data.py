import serial
import time 
import csv

ser = serial.Serial('COM3')
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        
        with open("test.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.strftime("%H : %M : %S"),decoded_bytes])
    
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        break
