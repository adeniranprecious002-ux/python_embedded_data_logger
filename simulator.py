import time  # control timing (delays)
import random  # generate random sensor data

while True:
    # simulate temperature sensor by generating random float number between 20.0 and 25.0
    temperature = random.uniform(20.0, 25.0)
    # simulate light sensor by generating random integer between 100 and 800
    light = random.randint(100, 800)
    # simulate sound sensor by generating random integer between 20 and 90
    sound = random.randint(20, 90)

    # output simulated sensor data to console, temperature formatted to 2 decimal places, light and sound as integers
    print(
        f"Temperature: {temperature:.2f} C, Light: {light} lx, Sound: {sound} dB")
    time.sleep(1)  # delay of 1 second before generating next set of sensor data
