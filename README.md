# 环境配置
Python 3.5
安装以下库：
- scipy
- numpy
- matplotlib
- pandas
- sklearn

还包括以下插件：
- flak8
- autopep8
- pylint

如果安装`scipy`失败的话，从[此处](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy)上下载相应的包进行安装。如果需要`mkl`的话，从新从上述URL中下载`numpy + mkl`包安装。

# 步骤
整体步骤：
- Installing the Python and SciPy platform.
- Loading the dataset.
- Summarizing the dataset.（使用统计算法）
- Visualizing the dataset.（使用plot）
- Evaluating some algorithms.
- Making some predictions.

## Evaluating some algorithms
步骤：
1. Separate out a validation dataset.
2. Set-up the test harness to use 10-fold cross validation.
3. Build 5 different models to predict species from flower 4. 4. measurements
5. Select the best model.

模型：
 - 逻辑回归（Logistic Regression (LR)）
 - 线性判别分析（Linear Discriminant Analysis (LDA)）
 - K近邻（K-Nearest Neighbors (KNN)）
 - 分类与回归树（Classification and Regression Trees (CART)）
 - 高斯朴素贝叶斯（Gaussian Naive Bayes (NB)）
 - 支持向量机（Support Vector Machines (SVM)）

 LR和LDA属于线性算法，其他的属于非线性算法。