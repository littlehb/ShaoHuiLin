# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  ipython
# http://blog.csdn.net/u012587561/article/details/50900781
# http://blog.csdn.net/liangzuojiayi/article/details/78183783?locationNum=8&fps=1

# Matplotlib图表不能在Pycharm中显示的问题
# http://blog.csdn.net/xinluqishi123/article/details/63523531
import matplotlib.pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()

# 下面我们将输出四张数字码（0、1、2、3）的8x8点阵图，
# 点阵图的数据从datasets读取并存储在digits中，
# 我们可以通过matplotlib所提供的方法显示这些点阵图，
# 请点击运行按钮查看效果。

images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)
    plt.show()