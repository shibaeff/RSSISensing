import numpy as np
class Detector():
    def __init__(self, window_sz=5):
        self._window_sz = window_sz

    @classmethod
    def is_radical(cls, v1, v2):
        change = (v1/v2) if v1 >= v2 else (v2/v1)
        return change >= 1.5

    @classmethod
    def predict(cls, dots):
        return Detector.is_radical(np.mean(dots[1:]), np.mean(dots[:-1])) and Detector.is_radical(np.std(dots[1:]),
                                                                                                  np.std(dots[:-1]))

    def detect(self, inp):
        out = []
        for i in range(self._window_sz, len(inp), 1):
            out.append(Detector.predict(out[i - self._window_sz: i]))
