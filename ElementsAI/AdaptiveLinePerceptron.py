import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from ElementsAI.learningWithoutTeacher import plot_decision_regions

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(url, header=None)
print('Данные об ирисах')
print(df.to_string())

y = df.iloc[0:100, 4].values
print(y)

y = np.where(y == "Iris-setosa", -1, 1)
print(y)

X = df.iloc[0:100, [0, 2]].values
print(X)
print('end x')

plt.scatter(X[0:50, 0], X[0:50, 1], color='red', marker='o', label='щетинситый')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='разноцветный')
plt.xlabel('Длина чашелистника')
plt.ylabel('Длина лепестка')
plt.legend(loc='upper left')
plt.show()


class AdaptiveLinearNeuron(object):
    def __init__(self, rate=0.01, niter=10):
        self.rate = rate
        self.niter = niter

    def fit(self, X, y):
        self.weight = np.zeros(1 + X.shape[1])
        self.cost = []
        for i in range(self.niter):
            output = self.net_input(X)
            errors = y - output
            self.weight[1:] += self.rate * X.T.dot(errors)
            self.weight[0] += self.rate * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.weight[1:]) + self.weight[0]

    def activated(self, X):
        return self.net_input(X)

    def predict(self, X):
        return np.where(self.activated(X) >= 0.0, 1, -1)


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

aln1 = AdaptiveLinearNeuron(0.01, 10).fit(X, y)

ax[0].plot(range(1, len(aln1.cost) + 1), np.log10(aln1.cost), marker='o')
ax[0].set_xlabel('Эпохи')
ax[0].set_ylabel('log(Сумма квадратичных ошибок)')
ax[0].set_title('Adaptive Neuron. Темп обучения 0.01')

aln2 = AdaptiveLinearNeuron(0.01, 10).fit(X, y)

ax[1].plot(range(1, len(aln2.cost) + 1), aln2.cost, marker='o')
ax[1].set_xlabel('Эпохи')
ax[1].set_ylabel('log(Сумма квадратичных ошибок)')
ax[1].set_title('Adaptive Neuron. Темп обучения 0.0001')

X_std = np.copy(X)
X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()

aln = AdaptiveLinearNeuron(0.01, 10)
aln.fit(X_std, y)

plot_decision_regions(X_std, y, classifier=aln)
plt.title('Adaptive Neuron')
plt.xlabel('Длина чашелистника')
plt.ylabel('Длина лепестка')
plt.legend(loc='upper left')
plt.show()

plt.plot(range(1, len(aln.cost)+1), aln.cost, marker="o")
plt.xlabel('Эпохи')
plt.ylabel('Сумма квадратичных ошибок')
plt.show()