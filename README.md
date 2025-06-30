# From Model to Production – DLBDSMTP01

## 📡 Anomaly Detection in an IoT Setting (Stream Processing)

This project demonstrates a simple implementation of a machine learning model served as a service (**MaaS**).  
The main focus is on deploying the model into a usable production setup, rather than on the complexity of the model itself.  
Simulated data is created to train the model, and random data generation is used to mimic a live data stream — similar to how real-time data might be provided by a future stakeholder.

---

## ⚙️ Setup Instructions

To run this project, make sure you have **Python 3.9** installed.  
You can download it here:  
👉 [Download Python 3.9](https://www.python.org/downloads/release/python-390/)

---

### 🐍 Install `pip` (Python Package Installer)

If `pip` is not already installed, follow the instructions below:

#### On Windows:
1. Download [`get-pip.py`](https://bootstrap.pypa.io/get-pip.py)
2. Open Command Prompt in the folder where the file is downloaded.
3. Run:
```bash
   python get-pip.py
````
#### On Ubuntu/Debian:
```bash
    sudo apt update
    sudo apt install python3-pip
 ```

#### On macOS (with Homebrew)
```bash
brew install python
```

### Project Files

- 'create_model.py' - creates model
- 'app.py' - flask API that loads the model and provides /predict endpoint
- 'stream_simulation.py' - simulates real-time data and sends it to the API as if from sensors
- 'requirements.txt' - list all dependencies to run the project

### 📦 Install Required Python Packages

```bash
pip install -r requirements.txt
```

### Usage

1. Run
```bash
  python main.py
```
It starts the Flask API, which can then receive data for predictions.

2. Run
```bash
  python stream_simulation.py
```
### If this process has to be stop

close the terminal this will terminate the streaming

### To test the functionality using Postman or any other service, rerun main.py to restart the system.