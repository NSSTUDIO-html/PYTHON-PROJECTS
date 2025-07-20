# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target variable (0: Iris-Setosa, 1: Iris-Versicolor, 2: Iris-Virginica)
feature_names = iris.feature_names
target_names = iris.target_names

print("Loaded Iris Dataset:")
print("Features:", feature_names)
print("Target classes:", target_names)
print("Shape of features (X):", X.shape)
print("Shape of target (y):", y.shape)
print("-" * 30)

# 2. Split the data into training and testing sets
# We'll use 80% for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Data split into training and testing sets:")
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_test:", y_test.shape)
print("-" * 30)

# 3. Choose a model
# We'll use Logistic Regression, a simple and effective classifier
model = LogisticRegression(max_iter=1000)  # Increase max_iter for convergence

print("Model chosen: Logistic Regression")
print("-" * 30)

# 4. Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")
print("-" * 30)

# 5. Make predictions on the test set
y_pred = model.predict(X_test)

print("Predictions on the test set:")
print(y_pred)
print("Actual labels of the test set:")
print(y_test)
print("-" * 30)

# 6. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the model: {accuracy:.2f}")
print("-" * 30)

# Optional: Make a single prediction
# Let's take the first sample from the test set
sample_prediction = model.predict(X_test[0].reshape(1, -1))
print("Single sample prediction:")
print("Features of the sample:", X_test[0])
print("Predicted class:", target_names[sample_prediction[0]])
print("Actual class:", target_names[y_test[0]])
