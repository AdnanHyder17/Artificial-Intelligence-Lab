# Implement k-means to mall customers dataset.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv('mall_customers.csv')

# Extract relevant features
features = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Handle missing values (if any) - here we'll just drop them
features = features.dropna()

# Normalize features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Define the number of clusters
k = 5

# Apply K-Means clustering
kmeans = KMeans(n_clusters=k, random_state=0)
clusters = kmeans.fit_predict(features_scaled)

# Add the cluster labels to the original DataFrame
data['Cluster'] = clusters

# Plot clusters
plt.figure(figsize=(10, 7))
plt.scatter(features_scaled[:, 0], features_scaled[:, 1], c=clusters, cmap='viridis', marker='o', edgecolor='k', s=50)

# Plot the cluster centers
centers = kmeans.cluster_centers_
centers = scaler.inverse_transform(centers)  # Transform back to original scale

plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=200, alpha=1.0, label='Centroids')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('K-Means Clustering of Mall Customers')
plt.legend()
plt.grid(True)
plt.show()
