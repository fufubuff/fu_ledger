from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.image as imgplt
from sklearn.metrics import accuracy_score
from sklearn.metrics import normalized_mutual_info_score
from sklearn.metrics import adjusted_rand_score
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'  # 设置为支持中文的字体


image_data = []  # 用列表来存放照片的数据
image_path = []  # 用列表来存放照片的路径
label_true = []  # 用列表存放真实的标签值

image_dir = r'E:\机器学习\data\face_images'
file_list = os.listdir(image_dir)  # 图片所在路径

# 使用for循环遍历所有的图片并得到它们的路径
for label, name in enumerate(file_list):
    image_name = os.listdir(os.path.join(image_dir, name))
    for i in image_name:
        image_path.append(os.path.join(image_dir, name, i))
        label_true.append(label)

# 读取一张照片的数据，并获取其三维的数值
im_data = imgplt.imread(image_path[0])
x, y, z = im_data.shape

# 读取照片数据，保存至image_path，并转化为数组类型
for each in image_path:
    image = imgplt.imread(each)
    image_data.append(image)
photo_data = np.array(image_data)

# 将每张照片的数据设置成为一行存储，降维得到可聚类的二维数据
photo_data_input = photo_data.reshape(-1, x * y * z)

# 聚类算法
clf = KMeans(n_clusters=10)
clf.fit(photo_data_input)
label = clf.labels_
centers = clf.cluster_centers_
result = centers[label]
result = result.astype("int64")
result = result.reshape(photo_data.shape)  # 将结果还原成原始的四维类型

# 展示分类的结果
fig, ax = plt.subplots(nrows=10, ncols=20, sharex="all", sharey="all", figsize=[15, 8], dpi=80)
plt.subplots_adjust(wspace=0, hspace=0)

num = 0
for i in range(10):
    for j in range(20):
        ax[i, j].imshow(result[num])
        num += 1

plt.xticks([])
plt.yticks([])
#plt.title('来自10人的200张图像')
plt.savefig("7")

# 调用库函数进行聚类性能评估
nmi = normalized_mutual_info_score(label_true, label)
ari = adjusted_rand_score(label_true, label)

# 打印两个主要参数值
print('NMI={:.4f}'.format(nmi))
print('ARI={:.4f}'.format(ari))
