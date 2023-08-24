import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# Generate data for clustering
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.5, random_state=42)

# Plot the generated data
plt.scatter(X[:, 0], X[:, 1], c='black', marker='o', s=25)
plt.title("Generated Data for Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Train KMeans model with 4 clusters
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)

# Predict cluster labels for the data
predicted_labels = kmeans.predict(X)

# Plot the data separated into predicted clusters
plt.scatter(X[:, 0], X[:, 1], c=predicted_labels, cmap='rainbow', marker='o', s=25)
plt.title("Clusters Separated by KMeans")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Load the Iris dataset
iris = load_iris()
iris_data = iris.data

# Select only 'petal_length' and 'petal_width' columns for clustering
X_iris = iris_data[:, [2, 3]]

# Choose different values of K for KMeans
k_values = [2, 3, 4, 5]

# Plot the clusters for different values of K
plt.figure(figsize=(12, 8))
for i, k in enumerate(k_values, start=1):
    kmeans_iris = KMeans(n_clusters=k, random_state=42)
    predicted_labels_iris = kmeans_iris.fit_predict(X_iris)
    
    plt.subplot(2, 2, i)
    plt.scatter(X_iris[:, 0], X_iris[:, 1], c=predicted_labels_iris, cmap='rainbow', marker='o', s=25)
    plt.title(f"Clusters for K = {k}")
    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")

plt.tight_layout()
plt.show()
