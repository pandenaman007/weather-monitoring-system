# test_alerts.py

import unittest
from src.alerts import check_alerts

class TestAlerts(unittest.TestCase):

    def setUp(self):
        # Common data structure for weather data. It can be reused for multiple tests.
        self.weather_data_normal = [
            {"name": "Delhi", "main": {"temp": 303.15}, "weather": [{"main": "Clear"}]},  # ~30°C
            {"name": "Mumbai", "main": {"temp": 301.15}, "weather": [{"main": "Clear"}]},  # ~28°C
        ]

        self.weather_data_high_temp = [
            {"name": "Delhi", "main": {"temp": 309.15}, "weather": [{"main": "Clear"}]},  # ~36°C
            {"name": "Mumbai", "main": {"temp": 310.15}, "weather": [{"main": "Clear"}]},  # ~37°C
        ]

        self.weather_data_edge_case = [
            {"name": "Delhi", "main": {"temp": 308.15}, "weather": [{"main": "Clear"}]},  # ~35°C
            {"name": "Mumbai", "main": {"temp": 308.15}, "weather": [{"main": "Clear"}]},  # ~35°C
        ]

        self.weather_data_below_threshold = [
            {"name": "Delhi", "main": {"temp": 306.15}, "weather": [{"main": "Clear"}]},  # ~33°C
            {"name": "Mumbai", "main": {"temp": 305.15}, "weather": [{"main": "Clear"}]},  # ~32°C
        ]

    def test_no_alerts_when_below_threshold(self):
        # Assuming the threshold is 35 degrees Celsius
        triggered_alerts = check_alerts(self.weather_data_below_threshold)
        self.assertEqual(triggered_alerts, [])  # Expect no alerts triggered

    def test_alerts_triggered_when_temp_exceeds_threshold(self):
        # Assuming the threshold is 35 degrees Celsius
        triggered_alerts = check_alerts(self.weather_data_high_temp)
        self.assertEqual(len(triggered_alerts), 2)  # Expect alerts for both cities
        self.assertIn('ALERT: High temperature in Delhi!', triggered_alerts)
        self.assertIn('ALERT: High temperature in Mumbai!', triggered_alerts)

    def test_no_alerts_at_threshold(self):
        # Temperature is exactly at the threshold (35 degrees Celsius)
        triggered_alerts = check_alerts(self.weather_data_edge_case)
        self.assertEqual(triggered_alerts, [])  # No alert should be triggered at the exact threshold

    def test_alerts_only_for_high_temp(self):
        # Only temperatures above 35 should trigger alerts
        weather_data_mixed = [
            {"name": "Delhi", "main": {"temp": 309.15}, "weather": [{"main": "Clear"}]},  # Should trigger alert
            {"name": "Mumbai", "main": {"temp": 308.15}, "weather": [{"main": "Clear"}]},  # Should trigger alert
        ]
        triggered_alerts = check_alerts(weather_data_mixed)
        self.assertEqual(len(triggered_alerts), 2)  # Both cities should trigger an alert
        self.assertIn('ALERT: High temperature in Delhi!', triggered_alerts)
        self.assertIn('ALERT: High temperature in Mumbai!', triggered_alerts)

    def test_alerts_triggered_when_temp_exceeds_threshold(self):
        weather_data = [
            {"name": "Delhi", "main": {"temp": 310.15}},  # Exceeds threshold (converted to Celsius)
            {"name": "Mumbai", "main": {"temp": 311.15}}  # Exceeds threshold
        ]
        triggered_alerts = check_alerts(weather_data)

        self.assertEqual(len(triggered_alerts), 2)  # Expect alerts for both cities

if __name__ == '__main__':
    unittest.main()
