import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import GridSearchCV

# Load the dataset
url = "https://raw.githubusercontent.com/xtreemtg/csv_files/master/features_churn_matrix_ex1.csv"
df = pd.read_csv(url)

# Brief analysis
# You can explore the data and plot distributions or relationships here
# For instance:
plt.hist(df['TotalCharges'], bins=20)
plt.xlabel('Total Charges')
plt.ylabel('Frequency')
plt.title('Distribution of Total Charges')
plt.show()

# Splitting the data
X = df.drop('Churn', axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Decision Tree
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

# Predict the data using the test set
y_pred = tree.predict(X_test)

# Calculate classification metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:")
print(conf_matrix)

# Define hyperparameters and their possible values
param_grid = {
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'max_features': ['auto', 'sqrt', 'log2']
}

# Perform GridSearch with Cross-validation
grid_search = GridSearchCV(estimator=tree, param_grid=param_grid, cv=5, scoring='f1')
grid_search.fit(X_train, y_train)

# Plotting the results
param_names = list(param_grid.keys())
results = grid_search.cv_results_
for param_name in param_names:
    plt.figure()
    plt.plot(param_grid[param_name], results[f'mean_test_score'], marker='o')
    plt.xlabel(param_name)
    plt.ylabel('F1 Score')
    plt.title(f'Grid Search: {param_name}')
    plt.grid()
    plt.show()

# Get the best model from GridSearch
best_tree = grid_search.best_estimator_
