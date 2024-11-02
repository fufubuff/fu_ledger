import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X3, y3 = make_blobs(n_samples=1000, random_state=9)  #
fig = plt.figure(figsize=(12, 6))


plt.subplot(1,2,1)
plt.title('original3')
plt.scatter(X3[:, 0], X3[:, 1], c=y3,cmap='viridis', edgecolor='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

kms = KMeans(n_clusters=3, max_iter=1000,random_state=0)
y3_sample = kms.fit_predict(X3)
centroids = kms.cluster_centers_

plt.subplot(1,2,2)
plt.title('K-means3')
plt.scatter(X3[:, 0], X3[:, 1], c=y3_sample,cmap='viridis', edgecolor='k')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='b', s=200, label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()

plt.tight_layout()
plt.savefig("3")
