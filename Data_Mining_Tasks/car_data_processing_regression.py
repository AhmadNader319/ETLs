import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

car_data = pd.read_csv('car_price_dataset.csv')

car_data.columns

print("car_data:")
print(car_data.head())

car_data = car_data.rename(columns={
    "millage": "miles",
    "automatic": "is_automatic",
    "car_price": "target_price"
})

print("\ncar_data after renaming:")
print(car_data.head())

print("\ncar_data.isna().sum():")
print(car_data.isna().sum().head()) # Print head of isnull sum

imputer_median = SimpleImputer(missing_values=np.nan, strategy="median")
car_data[['miles']] = imputer_median.fit_transform(car_data[['miles']])

# Mode for categorical-like or actual categorical columns
imputer_mode = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
car_data[['no_seats', 'is_automatic', 'car_type', 'car_age']] = imputer_mode.fit_transform(car_data[['no_seats', 'is_automatic', 'car_type', 'car_age']])

print("\ncar_data.isna().sum() after imputation:")
print(car_data.isna().sum().head())

label_encoder = LabelEncoder()
car_data['is_automatic'] = label_encoder.fit_transform(car_data['is_automatic'])

features = car_data.iloc[:, :-1].values
label = car_data.iloc[:, -1].values

print('\nfeatures (head):')
print(features[0:5])
print('\nlabel (head):')
print(label[0:5])

categorical_cols = [0, 4]

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), categorical_cols)], remainder='passthrough')
features = np.array(ct.fit_transform(features))

print("\nfeatures after ColumnTransformer:")
print(features[0:4])

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=42)


print(X_train[0:4])
print(X_test[0:4])
print(y_train[0:4])
print(y_test[0:4])

scaler = MinMaxScaler()
X_train[:, 6:8] = scaler.fit_transform(X_train[:, 6:8])
X_test[:, 6:8] = scaler.transform(X_test[:, 6:8])

print("\nX_train after scaling:")
print(X_train[0:4])
print("\nX_test after scaling:")
print(X_test[0:4])














# linear regression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
# predict the new prices (y_pred) based on the dependent values (X__test



y_pred = regressor.predict(X_test)
# compare the original prices/ independent/ features (y_test) and the new set of prices (y_pred)
result_df = pd.DataFrame({'Before_prediction': y_test, 'After_prediction': y_pred})
print("\nPrediction result:")
print(result_df.head())

# coefficient of determination -> how well the model fits
r2 = r2_score(y_test, y_pred)
print(f'\nR-squared score: {r2:.4f}')

mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae:.4f}')

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'Root Mean Squared Error: {rmse:.4f}')







# --- Visualization with Metrics ---
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs. Predicted Prices (Linear Regression)")

# Add text for metrics
text_x = min(y_test)  # Position the text in the lower-left
text_y = max(y_pred) * 0.9  # Adjust vertical position as needed
plt.text(text_x, text_y, f"R-squared: {r2:.2f}\nMAE: {mae:.2f}\nRMSE: {rmse:.2f}", fontsize=12)

plt.show()
