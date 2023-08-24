from sklearn.datasets import load_boston
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV

# Load the dataset
boston = load_boston()
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df['Price'] = boston.target

# Analyze the data
# You can plot distributions and relationships here using Seaborn and Matplotlib
# For example:
sns.pairplot(boston_df, x_vars=boston.feature_names, y_vars='Price')
plt.show()

# You can preprocess the data here based on observations (e.g., handle outliers, scaling, etc.)
# For example, dealing with outliers in the 'Price' column:
boston_df = boston_df[boston_df['Price'] < 50]

# Splitting the data into train and test sets
X = boston_df.drop('Price', axis=1)
y = boston_df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)

# Train Ridge Regression
ridge = Ridge()
ridge.fit(X_train, y_train)

# Train Lasso Regression
lasso = Lasso()
lasso.fit(X_train, y_train)

# Predictions using the trained models
linear_reg_preds = linear_reg.predict(X_test)
ridge_preds = ridge.predict(X_test)
lasso_preds = lasso.predict(X_test)

# Calculate Mean Absolute Error (MAE)
linear_reg_mae = mean_absolute_error(y_test, linear_reg_preds)
ridge_mae = mean_absolute_error(y_test, ridge_preds)
lasso_mae = mean_absolute_error(y_test, lasso_preds)

print("Linear Regression MAE:", linear_reg_mae)
print("Ridge Regression MAE:", ridge_mae)
print("Lasso Regression MAE:", lasso_mae)

# Define alpha values for Ridge and Lasso
alpha_values = [0.01, 0.1, 1, 10, 100]

# Create parameter grid for GridSearch
param_grid = {'alpha': alpha_values}

# Perform GridSearch with Cross-validation for Ridge and Lasso
ridge_grid = GridSearchCV(estimator=ridge, param_grid=param_grid, cv=5, scoring='neg_mean_absolute_error')
lasso_grid = GridSearchCV(estimator=lasso, param_grid=param_grid, cv=5, scoring='neg_mean_absolute_error')

# Fit the models
ridge_grid.fit(X_train, y_train)
lasso_grid.fit(X_train, y_train)

# Get best alpha values and MAE
best_ridge_alpha = ridge_grid.best_params_['alpha']
best_ridge_mae = -ridge_grid.best_score_
best_lasso_alpha = lasso_grid.best_params_['alpha']
best_lasso_mae = -lasso_grid.best_score_

print("Best Ridge Alpha:", best_ridge_alpha)
print("Best Ridge MAE:", best_ridge_mae)
print("Best Lasso Alpha:", best_lasso_alpha)
print("Best Lasso MAE:", best_lasso_mae)

