
import serial
import time
def IMU_data():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    time.sleep(2)

    # Read and record the data
    data =[]                       # empty list to store the data
    for i in range(1000000):
        b = ser.readline()         # read a byte string
        string_n = b.decode()  # decode byte string into Unicode  
        string = string_n.rstrip() # remove \n and \r
        #flt = float(string)        # convert string to float
        print(string)
        data.append(string)           # add to the end of data list
        time.sleep(0.1)            # wait (sleep) 0.1 seconds

    ser.close()

# show the data

#for line in data:
    #print(line)
