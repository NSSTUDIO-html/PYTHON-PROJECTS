# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 2: Create Dataset
data = {
    'Age': [22, 25, 47, 52, 46, 56, 24, 28],
    'Salary': [25000, 32000, 47000, 58000, 52000, 61000, 27000, 35000],
    'Buys': [0, 0, 1, 1, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

# Step 3: Split Features and Target
X = df[['Age', 'Salary']]
y = df['Buys']

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Train the Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Predict
y_pred = model.predict(X_test)

# Step 7: Evaluate
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 8: Predict New Sample
new_sample = [[30, 40000]]  # Age: 30, Salary: 40k
prediction = model.predict(new_sample)
print("Buys?", "Yes" if prediction[0] == 1 else "No")