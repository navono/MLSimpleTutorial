# Load libraries
import pandas
# from pandas.tools.plotting import scatter_matrix
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVM

#  Load dataset
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv('./iris.txt', names=names)


# Summarizing the dataset

# Dimensions of the dataset.
# print(dataset.shape)

# Peek at the data itself.
# print(dataset.head(20))

# Statistical summary of all attributes.
# print(dataset.describe())

# Breakdown of the data by the class variable
# print(dataset.groupby('class').size())


# Visualizing the dataset

# 单变量图形
# box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
# plt.show()

# histograms
# dataset.hist()
# plt.show()

# 多变量图形
# scatter plot matrix
# scatter_matrix(dataset)
# plt.show()


# Evaluating some algorithms

# Split-out validation dataset
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(
    X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVM()))


# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(
        model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)


# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()


# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
knn_predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, knn_predictions))
print(confusion_matrix(Y_validation, knn_predictions))
print(classification_report(Y_validation, knn_predictions))

svm = SVM()
svm.fit(X_train, Y_train)
svm_predictions = svm.predict(X_validation)
print(accuracy_score(Y_validation, svm_predictions))
print(confusion_matrix(Y_validation, svm_predictions))
print(classification_report(Y_validation, svm_predictions))