import unittest
from unittest.mock import patch, MagicMock
from scripts.two import func1 
class Testfunc1(unittest.TestCase):

    def setUp(self):
        print("Set up...")
        #self.value = 1

    def tearDown(self):
        print("Tear down...")
        #self.value = None
    @patch("scripts.two.bigquery")
    def test_func1(self,mock_bigquery):
        bc = MagicMock()
        bc.insert_rows_json.return_value = []
        mock_bigquery.Client.return_value = bc
        print("Testing func1 Mocking BigQuery")
        
        self.assertIn('New', func1())      


if __name__ == "__main__":
    unittest.main()