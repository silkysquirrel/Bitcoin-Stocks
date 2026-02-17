import unittest
import pandas as pd
import tempfile
import os

from ingestion import load_btc_data


class TestLoadBTCData(unittest.TestCase):

    def setUp(self):
        """
        Create a temporary CSV file for testing.
        """
        self.temp_file = tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
            suffix=".csv"
        )

        self.temp_file.write(
            "Start,End,Open,High,Low,Close,Volume,Market Cap\n"
            "2025-11-28,2025-11-29,91198.17,92937.17,90251.89,90954.11,65821286647.53658,1822350172123.8293\n"
            "2025-11-27,2025-11-28,90418,91832.04,90179.01,91293.26,94344388864.4007,1820918030980.3484\n"
            "2025-11-26,2025-11-27,87557.77,90575.95,86422.99,90512.74,82579085781.71777,1757398305728.4321\n"
            "2025-12-02,2025-12-03,86317.59,92253.9,86220.03,91279.88,90800618533.38327,1769154636427.965\n"
            "2025-12-01,2025-12-02,89918.97,89918.97,83930.25,86277.99,89677237431.18816,1718476658749.9373\n"

        )
        self.temp_file.flush()
        self.temp_file.close()

    def tearDown(self):
        """
        Remove the temporary CSV file.
        """
        os.unlink(self.temp_file.name)

    def test_load_btc_data_basic_properties(self):
        with open(self.temp_file.name, "r") as f:
            print(f.read())

        df = load_btc_data(self.temp_file.name)

        # 1. Index should be DatetimeIndex
        self.assertIsInstance(df.index, pd.DatetimeIndex)

        # 2. Data should be sorted by date
        self.assertTrue(df.index.is_monotonic_increasing)

        # 4. Data types should be float64
        numeric_columns = {"Open", "High", "Low",
                           "Close", "Volume", "Market Cap"}
        for col in numeric_columns:
            self.assertEqual(df[col].dtype, "float64")

        # 5. Row count should match input
        self.assertEqual(len(df), 5)

        # 6. Spot check a value
        self.assertEqual(df.iloc[0]["Close"], 90512.74)


if __name__ == "__main__":
    unittest.main()
