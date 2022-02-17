import pandas as pd


class Parser:
    @classmethod
    def parse_line(cls, s: str) -> (float, int):
        i, j = s.split(",")
        return float(i), int(j)

    @classmethod
    def read(cls, file: str) -> pd.DataFrame:
        with open(file, "r") as f:
            values = [Parser.parse_line(l) for l in f.readlines()]
            res = pd.DataFrame(values).rename(columns={0: "time", 1: "rssi"})
            res["rssi"] = res["rssi"].astype("float64")
            return res


