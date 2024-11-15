import unittest
from datetime import datetime

def valid_symbol(symbol):
    if len(symbol) < 2 or len(symbol) > 7:
        return False
    
    for char in symbol:
        if not ('A' <= char <= 'Z'):
            return False

    return True

def valid_chart_type(chart_type):
    return chart_type in ["1", "2"]

def valid_time_series(time_series):
    return time_series in ["1", "2", "3", "4"]

def valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestStockVisualizerInputs(unittest.TestCase):

    def test_symbol(self):
        self.assertTrue(valid_symbol("AAPL"))
        self.assertTrue(valid_symbol("GOOGL"))
        self.assertFalse(valid_symbol("apple"))
        self.assertFalse(valid_symbol("AAPL123"))
        self.assertFalse(valid_symbol("A"))

    def test_chart_type(self):
        self.assertTrue(valid_chart_type("1"))
        self.assertTrue(valid_chart_type("2"))
        self.assertFalse(valid_chart_type("3"))
        self.assertFalse(valid_chart_type("a"))

    def test_time_series(self):
        self.assertTrue(valid_time_series("1"))
        self.assertTrue(valid_time_series("2"))
        self.assertTrue(valid_time_series("3"))
        self.assertTrue(valid_time_series("4"))
        self.assertFalse(valid_time_series("5"))
        self.assertFalse(valid_time_series("0"))

    def test_start_date(self):
        self.assertTrue(valid_date("2024-01-01"))
        self.assertFalse(valid_date("01-01-2024"))
        self.assertFalse(valid_date("2024/01/01"))
        self.assertFalse(valid_date("2024-13-01")) 

    def test_end_date(self):
        self.assertTrue(valid_date("2024-12-31"))
        self.assertFalse(valid_date("31-12-2024"))
        self.assertFalse(valid_date("2024-02-30"))  
        self.assertFalse(valid_date("2024-00-01"))  

if __name__ == "__main__":
    unittest.main()
