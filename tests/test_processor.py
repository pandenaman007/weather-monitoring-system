import unittest
from src.processor import process_weather_data, calculate_daily_summary


class TestProcessor(unittest.TestCase):

    def setUp(self):
        # Weather data sample for one day
        self.weather_data_day = [
            {"name": "Delhi", "main": {"temp": 30}, "weather": [{"main": "Clear"}]},
            {"name": "Mumbai", "main": {"temp": 28}, "weather": [{"main": "Rain"}]},
            {"name": "Delhi", "main": {"temp": 32}, "weather": [{"main": "Clear"}]},
            {"name": "Mumbai", "main": {"temp": 27}, "weather": [{"main": "Rain"}]},
            {"name": "Delhi", "main": {"temp": 31}, "weather": [{"main": "Clear"}]}
        ]

    def test_process_weather_data(self):
        # Test the processing function
        processed_data = process_weather_data(self.weather_data_day)

        # Ensure processed data is not empty
        self.assertTrue(processed_data)

        # Test if it processed the correct number of cities
        self.assertEqual(len(processed_data), 2)  # Delhi and Mumbai

        # Check that the aggregation for Delhi is correct (average, max, min temps)
        delhi_data = processed_data["Delhi"]
        self.assertEqual(delhi_data["average_temp"], 31)  # (30 + 32 + 31) / 3
        self.assertEqual(delhi_data["max_temp"], 32)
        self.assertEqual(delhi_data["min_temp"], 30)
        self.assertEqual(delhi_data["dominant_condition"], "Clear")

    def test_calculate_daily_summary(self):
        # Test the daily summary calculation
        daily_summary = calculate_daily_summary(self.weather_data_day)

        # Ensure daily summary is calculated
        self.assertIn("Delhi", daily_summary)
        self.assertIn("Mumbai", daily_summary)

        # Check daily summary for Delhi
        delhi_summary = daily_summary["Delhi"]
        self.assertEqual(delhi_summary["average_temp"], 31)
        self.assertEqual(delhi_summary["max_temp"], 32)
        self.assertEqual(delhi_summary["min_temp"], 30)
        self.assertEqual(delhi_summary["dominant_condition"], "Clear")

        # Check daily summary for Mumbai
        mumbai_summary = daily_summary["Mumbai"]
        self.assertEqual(mumbai_summary["average_temp"], 27.5)
        self.assertEqual(mumbai_summary["max_temp"], 28)
        self.assertEqual(mumbai_summary["min_temp"], 27)
        self.assertEqual(mumbai_summary["dominant_condition"], "Rain")

    def test_empty_data(self):
        # Edge case: no data
        empty_data = []
        processed_data = process_weather_data(empty_data)
        self.assertEqual(processed_data, {})


if __name__ == '__main__':
    unittest.main()
