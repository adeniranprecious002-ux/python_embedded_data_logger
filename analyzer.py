import csv

temps = []  # list to store temperature readings

with open('data/sensor_log.csv', mode='r') as file:  # open CSV file in read-only mode
    reader = csv.reader(file)  # iterate through each row in the CSV file
    for row in reader:
        # temperature column is converted to float and added to the list
        temps.append(float(row[1]))

# calculate and print average temperature in 2 decimal places
print(f"Average temperature: {sum(temps) / len(temps):.2f} C")
# calculate and print maximum temperature in 2 decimal places
print(f"Max temperature: {max(temps):.2f} C")
# calculate and print minimum temperature in 2 decimal places
print(f"Min temperature: {min(temps):.2f} C")
