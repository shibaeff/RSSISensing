import unittest
from wiener_kolmogorov import WienerKolmogorov as WK


class MyTestCase(unittest.TestCase):
    def test_fit(self):
        f = WK()
        arr = [1,2,4]
        f.fit(arr)


    def test_transform(self):
        f = WK()
        arr = [1, 2, 4]
        f.fit(arr)
        arr2 = [1, 2, 4, 8]
        f.transform(arr)
        # f.transform(arr2)


if __name__ == '__main__':
    unittest.main()
