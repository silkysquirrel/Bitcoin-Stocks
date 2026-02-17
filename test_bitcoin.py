import unittest
from ingestion import load_btc_data


class TestBitcoin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass


if __name__ == "__main__":
    df = load_btc_data("data/bitcoinprices.csv")

    # print(df.head())
    print(df.to_string())
    print(len(df))
