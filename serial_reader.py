import csv # handle CSV file operations
import time # for timestamping (delays)
import sys # read incoming data stream

filename = 'data/sensor_log.csv' # CSV file to log sensor data

with open(filename, mode='a', newline="") as file:
    writer = csv.writer(file) # create CSV writer object in append mode

    while True: # continue reading from incoming data stream
        try:
            line = sys.stdin.readline().strip() # read a line from standard input
            if line:
                temp, light, sound = line.split(',') # parse incoming data
                writer.writerow([time.time(), temp, light, sound]) # log data with timestamp
                print(f"Logged: Temp={temp}, Light={light}, Sound={sound}") # confirm logging
        except KeyboardInterrupt:
            print("Logging stopped")
            break