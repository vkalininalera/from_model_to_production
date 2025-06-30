import requests
import random
import time

url = "http://127.0.0.1:5000/predict"


def generate_sensor_data():
    if random.random() < 0.9:
        temperature = round(random.uniform(-10, 40), 2)
        inertial_humidity = round(random.uniform(45, 50), 2)
        sound = round(random.uniform(35, 45), 2)
    else:
        temperature = round(random.choice([random.uniform(-40, -11), random.uniform(41, 70)]), 2)
        inertial_humidity = round(random.choice([random.uniform(0, 44), random.uniform(51, 100)]), 2)
        sound = round(random.choice([random.uniform(0, 34), random.uniform(46, 100)]), 2)

    return {
        "temperature": temperature,
        "inertial_humidity": inertial_humidity,
        "sound": sound
    }


while True:
    sample = generate_sensor_data()
    response = requests.post(url, json=sample)
    print(f"Sent: {sample} → Response: {response.json()}")
    time.sleep(1)
