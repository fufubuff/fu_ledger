import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.cluster import KMeans

# 生成示例数据
X1, y1 = make_circles(n_samples=400, factor=0.5, noise=0.1)

# 创建一个图形
fig = plt.figure(figsize=(12, 6))

# 原始数据
plt.subplot(1, 2, 1)
plt.title('Original Data')
plt.scatter(X1[:, 0], X1[:, 1], c=y1, cmap='viridis', edgecolor='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# 执行 KMeans 聚类
kms = KMeans(n_clusters=2, max_iter=400, random_state=0)  # 设定簇的数量和最大迭代次数
y1_sample = kms.fit_predict(X1)  # 计算并预测样本类别
centroids = kms.cluster_centers_

# 聚类结果
plt.subplot(1, 2, 2)
plt.title('K-means Clustering')
plt.scatter(X1[:, 0], X1[:, 1], c=y1_sample, cmap='viridis', edgecolor='k')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='red', s=200, label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()

# 显示图形
plt.tight_layout()
plt.savefig("1")
