import serial
import numpy as np     
import matplotlib.pyplot as plt 


ser = serial.Serial('COM5', 115200)
ser.flushInput()

x =[]
y1=[]
y2=[]

len = 10001

for i in range (len):  
   
    while (ser.inWaiting() == 0):   
        pass                       
        
    #arduino = ser.readline()
    ser_bytes = ser.readline()
    arduinoString = float(ser_bytes.decode('cp1252'))
    
    
    #arduinoString = arduino.decode('cp1252')
  
    
    y_1 = np.append(y_1,arduinoString)
    print(x)
    

  

    

        
    