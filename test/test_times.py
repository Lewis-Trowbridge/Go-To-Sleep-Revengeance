import unittest
import source.gotosleep.times as times

class TestTimes(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def test_get_seconds_24_hours_returns_correctly(self):
        test_timestring = "10:00"
        expected_seconds = 36000

        real_seconds = times.get_seconds(test_timestring)

        self.assertEqual(expected_seconds, real_seconds)

    def test_get_seconds_12_hours_AM_returns_correctly(self):
        test_timestring = "10:00 AM"
        expected_seconds = 36000

        real_seconds = times.get_seconds(test_timestring)

        self.assertEqual(expected_seconds, real_seconds)

    def test_get_seconds_12_hours_PM_returns_correctly(self):
        test_timestring = "1:00PM"
        expected_seconds = 46800

        real_seconds = times.get_seconds(test_timestring)

        self.assertEqual(expected_seconds, real_seconds)

    def test_get_seconds_24_hours_half_hour_returns_correctly(self):
        test_timestring = "22:30"
        expected_seconds = 81000

        real_seconds = times.get_seconds(test_timestring)

        self.assertEqual(expected_seconds, real_seconds)

    def test_get_seconds_12_hours_half_hour_returns_correctly(self):
        test_timestring = "5:30PM"
        expected_seconds = 63000

        real_seconds = times.get_seconds(test_timestring)

        self.assertEqual(expected_seconds, real_seconds)
    
    def test_get_seconds_12_hours_with_space_returns_correctly(self):
        test_timestring = "1:00 PM"
        expected_seconds = 46800

        real_seconds = times.get_seconds(test_timestring)

        self.assertEqual(expected_seconds, real_seconds)

    def test_get_seconds_midnight_returns_zero(self):
        test_timestring = "0:00"
        expected_seconds = 0

        real_seconds = times.get_seconds(test_timestring)

        self.assertEqual(expected_seconds, real_seconds)

    def test_get_seconds_random_string_throws_valueerror(self):
        test_timestring = "RIEJORIEJOIFNOIN"
        self.assertRaises(ValueError, times.get_seconds, test_timestring)

    def test_get_seconds_24_hours_missing_hour_throws_valueerror(self):
        test_timestring = ":00"
        self.assertRaises(ValueError, times.get_seconds, test_timestring)

    def test_get_seconds_12_hours_missing_minutes_throws_valueerror(self):
        test_timestring = "1:"
        self.assertRaises(ValueError, times.get_seconds, test_timestring)
    
    def test_get_seconds_strings_in_24_format_throws_valueerror(self):
        test_timestring = "FA:IL"
        self.assertRaises(ValueError, times.get_seconds, test_timestring)

    def test_get_seconds_strings_in_12_format_throws_valueerror(self):
        test_timestring = "FA:IL AM"
        self.assertRaises(ValueError, times.get_seconds, test_timestring)

    def test_get_seconds_hours_outside_24_range_throws_valueerror(self):
        test_timestring = "25:00"
        self.assertRaises(ValueError, times.get_seconds, test_timestring)

    def test_get_seconds_minutes_outside_60_range_throws_valueerror(self):
        test_timestring = "10:70"
        self.assertRaises(ValueError, times.get_seconds, test_timestring)

    def test_get_seconds_hours_outside_12_range_throws_valueerror(self):
        test_timestring = "13:00AM"
        self.assertRaises(ValueError, times.get_seconds, test_timestring)
    
    def test_get_seconds_minutes_outside_12_range_throws_valueerror(self):
        test_timestring = "12:63AM"
        self.assertRaises(ValueError, times.get_seconds, test_timestring)

if __name__ == '__main__':
    unittest.main()