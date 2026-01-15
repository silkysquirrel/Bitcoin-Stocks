import pandas as pd

pd.options.display.max_rows = 80

df = pd.read_csv('bitcoinprices.csv')

# print(df.to_string())

print(pd.options.display.max_rows)


class Bitcoin:

    def __init__(self, start, end, open, high, low, close, volume, marketcap):
        self.start = start
        self.end = end
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.marketcap = marketcap
