import numpy as np
from scipy.signal import correlate


class WienerKolmogorov:
    def __init__(self):
        self._noise = None
        self._mean = None
        self._var = None

    def fit(self, arr):
        arr = np.array(arr)
        sz = np.size(arr)
        self._mean = correlate(arr, np.ones(sz), 'same') / np.prod(sz, axis=0)
        self._var = (correlate(arr ** 2, np.ones(sz), 'same') / np.prod(sz, axis=0) - self._mean ** 2)
        self._noise = 0.55 * np.mean(np.ravel(self._var), axis=0)
        # print(self._mean)

    def transform(self, arr) -> np.array:
        res = arr - self._mean
        res *= 1 - self._noise / self._var
        res += self._mean
        return np.where(self._var < self._noise, self._mean, res)
