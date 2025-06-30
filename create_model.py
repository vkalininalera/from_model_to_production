from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pandas as pd
import random

data = []
for _ in range(100):
    if random.random() < 0.5:  # 50% normal
        temperature = random.uniform(-10, 40)
        inertial_humidity = random.uniform(45, 50)
        sound = random.uniform(35, 45)
        label = 0
    else:  # anomaly
        temperature = random.choice([random.uniform(-40, -11), random.uniform(41, 70)])
        inertial_humidity = random.choice([random.uniform(0, 45), random.uniform(50, 100)])
        sound = random.choice([random.uniform(0, 34), random.uniform(46, 100)])
        label = 1
    data.append([temperature, inertial_humidity, sound, label])

df = pd.DataFrame(data, columns=['temperature', 'inertial_humidity', 'sound', 'label'])

X = df[['temperature', 'inertial_humidity', 'sound']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Make predictions on the test set
y_predict = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_predict)

print("Model Accuracy:", round(accuracy * 100, 2), "%")
print(confusion_matrix(y_test, y_predict))

with open('anomaly_model.pkl', 'wb') as file:
    pickle.dump(clf, file)
