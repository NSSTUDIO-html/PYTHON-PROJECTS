from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
data = np.array([[1, 2], [3, 4], [5, 6]])

# Initialize a StandardScaler
scaler = StandardScaler()

# Fit the scaler to the data and transform it
scaled_data = scaler.fit_transform(data)
print("Original Data:\n", data)
print("Scaled Data:\n", scaled_data)

# You can also transform new data using the fitted scaler
new_data = np.array([[2, 3]])
scaled_new_data = scaler.transform(new_data)
print("Scaled New Data:\n", scaled_new_data)
