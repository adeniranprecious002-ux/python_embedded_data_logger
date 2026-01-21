import csv  # handle CSV file operations
import matplotlib.pyplot as plt  # plotting library

times = []  # list to store timestamps
temps = []  # list to store temperature readings

with open('data/sensor_log.csv', mode='r') as file:  # open CSV file in read-only mode
    reader = csv.reader(file)  # iterate through each row in the CSV file
    for row in reader:
        # timestamp column is converted to float and added to the list
        times.append(float(row[0]))
        # temperature column is converted to float and added to the list
        temps.append(float(row[1]))

plt.plot(times, temps)  # plot temperature vs. time
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
plt.title('Temperature over Time')
plt.show()
