from scipy.cluster.vq import *
from pylab import *
from PIL import Image
# 添加中文字体支持
from matplotlib.font_manager import FontProperties

# font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)   # 新宋字体 大小14

def clusterpixels(infile, k, steps):
    im = array(Image.open(infile))
    dx = im.shape[0] / steps
    dy = im.shape[1] / steps
    # compute color features for each region
    features = []

    for x in range(steps):   # RGB三色通道
        for y in range(steps):
            R = mean(im[int(x * dx):int((x + 1) * dx), int(y * dy):int((y + 1) * dy), 0])
            G = mean(im[int(x * dx):int((x + 1) * dx), int(y * dy):int((y + 1) * dy), 1])
            B = mean(im[int(x * dx):int((x + 1) * dx), int(y * dy):int((y + 1) * dy), 2])
            features.append([R, G, B])
    features = array(features, 'f')  # make into array
    # 聚类， k是聚类数目
    centroids, variance = kmeans(features, k)
    code, distance = vq(features, centroids)
    # create image with cluster labels
    codeim = code.reshape(steps, steps)
    # codeim = imresize(codeim, im.shape[:2], 'nearest')
    codeim = np.array(Image.fromarray(codeim).resize((im.shape[1], im.shape[0])))
    return codeim


# k = 5
infile_MayDay = '2.jpg'
im_MayDay = array(Image.open(infile_MayDay))
steps = (50, 100)  # image is divided in steps*steps region
# print(steps[0], steps[-1])

# 显示原图MayDay.jpg
figure()
subplot(231)
title('original')
# title(u'原图', fontproperties=font)
axis('off')
imshow(im_MayDay)

# # 用50*50的块对empire.jpg的像素进行聚类
# codeim = clusterpixels(infile_empire, k, steps[0])
# ax1 = subplot(232)
# title(u'k=6,steps=50', fontproperties=font)
# # ax1.set_title('Image')
# axis('off')
# imshow(codeim)

# 用100*100的块对MayDay.jpg的像素进行聚类 效果要比50*50好不少
codeim = clusterpixels(infile_MayDay, 2, steps[-1])
subplot(232)
title('K=2')
# title(u'k=6,steps=100', fontproperties=font)
# ax1.set_title('Image')
axis('off')
imshow(codeim)

codeim = clusterpixels(infile_MayDay, 3, steps[-1])
subplot(233)
title('K=3')
axis('off')
imshow(codeim)

codeim = clusterpixels(infile_MayDay, 4, steps[-1])
subplot(234)
title('K=4')
axis('off')
imshow(codeim)

codeim = clusterpixels(infile_MayDay, 5, steps[-1])
subplot(235)
title('K=5')
axis('off')
imshow(codeim)

codeim = clusterpixels(infile_MayDay, 6, steps[-1])
subplot(236)
title('K=6')
axis('off')
imshow(codeim)

savefig("5")