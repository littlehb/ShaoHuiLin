from sklearn import datasets, svm
# 读取数据
digits = datasets.load_digits()
# 建立SVM分类器
clf = svm.SVC(gamma=0.001, C=100.)
# 使用训练数据对分类器进行训练，它将会返回分类器的某些参数设置
print(clf.fit(digits.data[:-1], digits.target[:-1]))