import unittest
import parse


class TestParse(unittest.TestCase):
    def test_read(self):
        res = parse.Parser.read("../../runs/1/pre.txt")
        self.assertTrue(len(res) > 0)

if __name__ == '__main__':
    unittest.main()