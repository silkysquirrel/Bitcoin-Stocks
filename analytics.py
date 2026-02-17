import pandas as pd
from ingestion import load_btc_data

import matplotlib.pyplot as plt


# simple moving average

def simple_moving_average(df: pd.DataFrame, window: int, price_col: str = "Close",) -> pd.Series:
    if window <= 0:
        raise ValueError("Window must be positive")

    return df[price_col].rolling(window=window).mean()

# exponential moving average


def exponential_moving_average(df: pd.DataFrame, span: int, price_col: str = "Close"):
    return df[price_col].ewm(span=span, adjust=False).mean()


def simple_returns(df: pd.DataFrame, price_col="Close"):
    return df[price_col].pct_change()


if __name__ == "__main__":
    df = load_btc_data("data/bitcoinprices.csv")
    # df["sma_20"] = simple_moving_average(df, window=20)
    # sma_3 = simple_moving_average(df, window=3)
    # print(sma_3)

    # df["sma_20"] = simple_moving_average(df, 20)

    # df[["Close", "sma_20"]].plot(title="BTC Price & 20-Day SMA")
    # plt.show()

    # df["ema_20"] = exponential_moving_average(df, 20)

    # df[["Close", "ema_20"]].plot(title="BTC Close vs EMA(20)")
    # plt.show()
    returns = simple_returns(df)

    print(returns.head())
