from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
import pandas as pd

# Sample numerical data
numerical_data = np.array([[10, 2], [20, 4], [30, 1]])
scaler = StandardScaler()
scaled_numerical_data = scaler.fit_transform(numerical_data)
print("Scaled Numerical Data:\n", scaled_numerical_data)

# Sample categorical data
categorical_data = [['red'], ['blue'], ['green'], ['red']]
encoder = OneHotEncoder()
encoded_categorical_data = encoder.fit_transform(categorical_data).toarray()
print("Encoded Categorical Data:\n", encoded_categorical_data)

# Using Pandas DataFrame for clarity
df = pd.DataFrame({'color': ['red', 'blue', 'green', 'red'], 'size': ['small', 'medium', 'large', 'small']})
encoder_df = pd.get_dummies(df, columns=['color', 'size'])
print("Pandas One-Hot Encoding:\n", encoder_df)
