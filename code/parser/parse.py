# from typing import List
import pandas as pd

class Parser:
    @classmethod
    def parse_line(s: str) -> (float, int):
        i, j = s.split(",")
        return float(i), int(j)

    @classmethod
    def read(cls, file: str) -> pd.DataFrame:
        with open(file, "r") as f:
            values = list(map(Parser.parse_line, f.readlines()))
            return pd.DataFrame(values)

