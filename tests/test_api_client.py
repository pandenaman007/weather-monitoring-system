import unittest
from unittest.mock import patch
from src.api_client import get_weather_data


class TestAPIClient(unittest.TestCase):

    @patch('src.api_client.requests.get')  # Mock requests.get call
    def test_get_weather_data_success(self, mock_get):
        # Mocking a successful response from the API
        mock_response = {
            "main": {"temp": 300.15, "feels_like": 303.15},
            "weather": [{"main": "Clear"}],
            "dt": 1605182400,
            "name": "Mumbai"
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        data = get_weather_data()

        # Ensure that data is retrieved
        self.assertEqual(len(data), 1)  # Only one city's data should be fetched (as per the mock)
        self.assertEqual(data[0]["name"], "Mumbai")
        self.assertEqual(data[0]["main"]["temp"], 300.15)

    @patch('src.api_client.requests.get')  # Mock requests.get call
    def test_get_weather_data_failure(self, mock_get):
        # Simulate an API failure (wrong API key or other issues)
        mock_get.return_value.status_code = 401

        data = get_weather_data()

        # Ensure no data is returned when the API fails
        self.assertEqual(len(data), 0)

    @patch('src.api_client.CITIES', [])  # Mock CITIES to be an empty list
    @patch('src.api_client.requests.get')  # Mock requests.get call
    def test_get_weather_data_no_city(self, mock_get):
        # Even though requests.get is mocked, it won't be called because CITIES is empty.
        mock_response = {}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        data = get_weather_data()

        # Since CITIES is mocked as an empty list, no data should be fetched
        self.assertEqual(len(data), 0)


if __name__ == '__main__':
    unittest.main()
