import unittest,sys
from unittest.mock import patch
import schedule
from src.main import job
sys.path.append('C:\Users\deepa\PycharmProjects\weather-monitoring-system\src\api_client.py')



class TestScheduler(unittest.TestCase):

    @patch('src.main.job')
    def test_schedule_job(self, mock_job):
        # Schedule the job to run every minute
        schedule.every(1).minutes.do(job)

        # Run scheduled tasks
        schedule.run_pending()

        # Verify that the job function is called
        mock_job.assert_called_once()


if __name__ == '__main__':
    unittest.main()
