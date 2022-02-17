import numpy as np


class Detector():
    def __init__(self, window_sz=5, thresh=1.5):
        self._window_sz = window_sz
        self._thresh = thresh

    def is_radical(self, v1, v2):
        change = (v1 / v2) if v1 >= v2 else (v2 / v1)
        return change >= self._thresh

    def predict(self, dots):
        return self.is_radical(np.mean(dots[1:]), np.mean(dots[:-1]))
    #
    # and self.is_radical(np.std(dots[1:]),
    #                     np.std(dots[:-1]))

    def detect(self, inp):
        out = []
        for i in range(self._window_sz, len(inp), 1):
            out.append(self.predict(inp[i - self._window_sz: i]))
        return out
