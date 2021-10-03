import sys
import pandas as pd
from io import StringIO


def main():
    # CSV Format
    # A B C (column headers)
    # 1 2 3 (values)
    # 4 5 6 (values)
    # is made as: "A,B,C \n 1,2,3 \n 4,5,6"
    # or
    # "A,B,C (\n is hidden)
    #  1,2,3
    #  4,5,6"

    a = ""

    for line in sys.stdin:
        a += line

    df = pd.read_csv(StringIO(a))
    print(a)
    print(df)
