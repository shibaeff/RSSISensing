from typing import List


class Parser:
    @classmethod
    def read(cls, file: str) -> List[int]:
        with open(file, "r") as f:
            values = list(map(int, f.readlines()))
            return values

