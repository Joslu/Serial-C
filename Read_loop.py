import serial
ser = serial.Serial('COM5')
ser.flushInput()

while True:

    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
    
    except KeyboardInterrupt:
        print("Keyboard Interrupt D:")
        break

        
