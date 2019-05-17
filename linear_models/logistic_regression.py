import numpy as np
from functional import sigmoid
from base import BaseModel, ClassifierMixin


class LogisticRegression(BaseModel, ClassifierMixin):


    def __init__(self, C: np.float=1.0, lr: np.float=0.02,
                 max_epochs: np.int=1000, eps: np.float=1e-8) -> None:
        self.W = None
        self.C = C
        self.lr = lr
        self.max_epochs = max_epochs
        self.eps = eps


    def fit(self, X: np.array, y: np.array) -> None:
        self.W = np.zeros(X.shape[1])
        n_train = X.shape[0]
        for e in range(self.max_epochs):
            prev_W = self.W.copy()
            scores = sigmoid(X.dot(self.W))
            self.W -= self.lr / n_train * X.T.dot(scores - y)
            if np.linalg.norm(self.W - prev_W) < self.eps:
                break


    def raw_predict(self, X: np.array) -> np.array:
        scores = sigmoid(X.dot(self.W))
        return scores
