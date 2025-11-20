from datetime import datetime
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from mock import GPIO
from mock.SDL_DS3231 import SDL_DS3231
from src.parking_garage import ParkingGarage
from src.parking_garage import ParkingGarageError

class TestParkingGarage(TestCase):

    @patch.object(GPIO, "input")
    def test_check_occupancy_true(self, distance_sensor : Mock):
        distance_sensor.return_value = True
        # This is an example of test where I want to mock the GPIO.input() function
        garage = ParkingGarage()
        outcome = garage.check_occupancy(garage.INFRARED_PIN2)
        self.assertTrue(outcome)


