import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
from scipy.stats import skew

vehicle_accidents_data = pd.read_csv('vehicle_accidents_dataset.csv')

print(vehicle_accidents_data.head())

vehicle_accidents_data = vehicle_accidents_data.drop(columns=["IsWeekend"])

vehicle_accidents_data = vehicle_accidents_data.rename(columns={
    "DriverExperience": "driver_experience",
    "VehicleType": "vehicle_type",
    "RoadType": "road_type",
    "Weather": "weather",
    "Accident": "accident",
    "Speed": "speed"
})

print(vehicle_accidents_data.head())

vehicle_accidents_data.isna().sum()

imputer_median = SimpleImputer(missing_values=np.nan, strategy="mean")
vehicle_accidents_data[['speed']] = imputer_median.fit_transform(vehicle_accidents_data[['speed']])

# For weather, driver_experience (categorical)
imputer_mode = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
vehicle_accidents_data[['weather', 'driver_experience']] = imputer_mode.fit_transform(vehicle_accidents_data[['weather', 'driver_experience']])

vehicle_accidents_data.isna().sum()

features = vehicle_accidents_data.iloc[:, :-1].values
label = vehicle_accidents_data.iloc[:, -1].values

print('features:',features)
print('label:',label)

categorical_cols = [0, 1, 2, 3]

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), categorical_cols)], remainder='passthrough')
features = np.array(ct.fit_transform(features))

print(features[0:10])

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.3, random_state=42)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

scaler = MinMaxScaler()
X_train[:, -1:] = scaler.fit_transform(X_train[:, -1:])
X_test[:, -1:] = scaler.transform(X_test[:, -1:])

print(X_train)
print(X_test)

# --- Naive Bayes Classifier Training ---
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

# --- Prediction ---
nb_y_pred = nb_classifier.predict(X_test)
result_df = pd.DataFrame({'Predicted': nb_y_pred, 'Test': y_test})
print(result_df)

# --- Confusion Matrix & Accuracy ---
nb_cm = confusion_matrix(y_test, nb_y_pred)
print(nb_cm)
nb_accuracy = accuracy_score(y_test, nb_y_pred)
print(f'Accuracy: {nb_accuracy * 100:.2f}%')

# --- Plot Confusion Matrix ---
ax = sns.heatmap(nb_cm, annot=True, fmt='d', cmap='viridis')
ax.set_title('NB Confusion Matrix')
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')

ax.xaxis.set_ticklabels(['No Accident', 'Accident'])
ax.yaxis.set_ticklabels(['No Accident', 'Accident'])

plt.show()

# --- KNN Classifier Training ---
knn_classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
knn_classifier.fit(X_train, y_train)

# --- Prediction ---
knn_y_pred = knn_classifier.predict(X_test)
result_df = pd.DataFrame({'Predicted': knn_y_pred, 'Test': y_test})
print(result_df)

# --- Confusion Matrix & Accuracy ---
knn_cm = confusion_matrix(y_test, knn_y_pred)
print(knn_cm)
knn_accuracy = accuracy_score(y_test, knn_y_pred)
print(f'Accuracy: {knn_accuracy * 100:.2f}%')

# --- Plot Confusion Matrix ---
ax = sns.heatmap(knn_cm, annot=True, fmt='d', cmap='viridis')
ax.set_title('KNN Confusion Matrix')
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')

ax.xaxis.set_ticklabels(['No Accident', 'Accident'])
ax.yaxis.set_ticklabels(['No Accident', 'Accident'])

plt.show()
