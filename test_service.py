import unittest
from mock import Mock, patch
from service import Service

def test_tester():
    if 1 == 1:
        print("working")

class TestService(unittest.TestCase):

    @patch("test_service.Service.bad_random")
    def test_bad_random(self, mock_service):
        mock_service.return_value = 10
        assert Service.bad_random() == 10
        return

    @patch("test_service.Service.bad_random")
    def test_divide(self, mock_service):
        mock_service.return_value = 10
        assert Service().divide(2) == 5
        return


    def test_abs_plus(self):
        assert Service.abs_plus(self, 1) == 2
        return

    @patch('service.Service.bad_random')
    def test_complicated_function(self, bad_random):
        mock_service.bad_random.return_value = 0
        mock_service.divide.return_value = 10
        final = Service_divide(0), Service.bad_random()
        assert final[0] == 0
        assert final[1] == 10

TestService()
