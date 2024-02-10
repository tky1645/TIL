# pytorch
import torch
import torchvision
import torchvision.transforms as transforms
# Utilities
import numpy as np
import matplotlib.pyplost as plt
%matplotlib inline

# Load Iris
import seaborn as sns
iris = sns.load_dataset('iris')
print(type(iris))  # Pandasで読込まれている事の確認
iris.head()

# カテゴリ変数を変換
iris.loc[:, 'species'] = iris.loc[:, 'species'].map({'setosa':0, 'versicolor':1, 'virginica':2})
iris.head()

# Numpy変換の為にvaluesというメソッドを使用
X = torch.FloatTensor(iris.drop("species", axis=1).values)
y = torch.LongTensor(iris["species"].values.astype(np.int64))  # dtypeをint64へ変換してから処理

# Datasetを作成
Dataset = torch.utils.data.TensorDataset(X, y)
