import pandas as pd


def load_btc_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    df["Start"] = pd.to_datetime(df["Start"])
    df["End"] = pd.to_datetime(df["End"])

    # always manually sort, the data can be sorted improperly
    df = df.sort_values("Start")

    df = df.set_index("Start")

    df = df.astype({
        "Open": "float64",
        "High": "float64",
        "Low": "float64",
        "Close": "float64",
        "Volume": "float64",
        "Market Cap": "float64"
    })

    df = df.dropna()
    df = df[~df.index.duplicated(keep="last")]

    return df
