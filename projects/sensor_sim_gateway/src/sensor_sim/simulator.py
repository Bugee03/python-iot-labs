import random
import time
import json

#here will be data from microcontroller (stm32,msp430,esp32...)
def generate_data():

    return{
        "temperature": round(random.uniform(20, 40), 2),
        "current": round(random.uniform(0.5, 2.5), 2),
        "vibration": round(random.uniform(0.0, 1.0), 3)
    }

if __name__ == "__main__":

    while True:
        data = generate_data()
        print(json.dumps(data))
        time.sleep(1)               #1Hz

        

