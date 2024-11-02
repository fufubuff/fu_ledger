from sklearn.cluster import KMeans
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

X2, y2 = make_moons(n_samples=400, noise=0.1)

fig = plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original')
plt.scatter(X2[:, 0], X2[:, 1], c=y2)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

kms = KMeans(n_clusters=2, max_iter=400, random_state=0)
y2_sample = kms.fit_predict(X2)
centroids = kms.cluster_centers_

plt.subplot(1, 2, 2)
plt.title('K-means')
plt.scatter(X2[:, 0], X2[:, 1], c=y2_sample, cmap='viridis', edgecolor='k')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='b', s=200, label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()

plt.tight_layout()
plt.savefig("2.png")  # 指定文件扩展名

