# Implement linear regression using least square from scratch (Refer
# to Kaggle for house price dataset).


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data_frame = pd.read_csv('train.csv')

# Extract features and target variable
features = data_frame[['GrLivArea']].values
target = data_frame['SalePrice'].values.reshape(-1, 1)

# Replace NaN values with zero
features = np.nan_to_num(features)
target = np.nan_to_num(target)

# Add a bias term (intercept)
features_bias = np.c_[np.ones((len(features), 1)), features]

# Calculate the parameters using the normal equation
parameters_best = np.linalg.inv(features_bias.T.dot(features_bias)).dot(features_bias.T).dot(target)

# Output the parameters
print("Intercept:", parameters_best[0][0])
print("Slope:", parameters_best[1][0])

# Make predictions for new feature values
new_features = np.array([[500], [2500]])
new_features_bias = np.c_[np.ones((len(new_features), 1)), new_features]
predictions = new_features_bias.dot(parameters_best)

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(features, target, s=10, alpha=0.5, label='Data Points')
plt.plot(new_features, predictions, color='red', linestyle='-', linewidth=2, label='Regression Line')
plt.xlabel("GrLivArea")
plt.ylabel("SalePrice")
plt.title("Linear Regression using Least Squares")
plt.legend()
plt.grid(True)
plt.show()
