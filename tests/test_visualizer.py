import unittest
from src.visualizer import plot_daily_summary


class TestVisualizer(unittest.TestCase):

    def test_plot_daily_summary(self):
        # Simulate daily summary data
        daily_summary = {
            "Delhi": {
                "average_temp": 31,
                "max_temp": 32,
                "min_temp": 30,
                "dominant_condition": "Clear"
            }
        }

        # Test if the plot function runs without errors
        try:
            plot_daily_summary(daily_summary)
            result = True
        except Exception as e:
            print(f"Error: {e}")
            result = False

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
