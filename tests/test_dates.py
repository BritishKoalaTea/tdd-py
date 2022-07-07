import unittest
import dates


class TestDates(unittest.TestCase):

    def test_first_day_of_month(self):
        result = dates.day_of_the_week_month_start(2020, 1)
        print("1/1/2020 is a " + result)
        self.assertEqual("Wednesday", result)

        result2 = dates.day_of_the_week_month_start(2000, 1)
        print("1/1/2000 is a " + result2)
        self.assertEqual("Saturday", result2)

    def test_day_of_week(self):
        result = dates.day_of_the_week(1969, 10, 31)
        print("10/31/1969 is a " + result)
        self.assertEqual("Friday", result)

        result2 = dates.day_of_the_week(2017, 10, 12)
        print("10/12/2017 is a " + result2)
        self.assertEqual("Thursday", result2)

    def test_day_name_locale(self):
        english = dates.day_of_week_in_locale(2021, 3, 30, 'en_GB')
        print("UK locale is: " + english)
        self.assertEqual("Tuesday", english)

        french = dates.day_of_week_in_locale(2021, 3, 30, 'fr_FR')
        print("French locale is: " + french)
        self.assertEqual("mardi", french)

        german = dates.day_of_week_in_locale(2021, 3, 30, 'de_DE')
        print("German locale is: " + german)
        self.assertEqual("Dienstag", german)

    def test_friday_thirteenth(self):
        self.assertTrue(dates.has_friday_thirteenth(2020, 11))
        self.assertFalse(dates.has_friday_thirteenth(2020, 12))

    def test_friday_thirteenths_this_year(self):
        self.assertEqual(1, dates.friday_thirteenths_this_year(2016))
        self.assertEqual(2, dates.friday_thirteenths_this_year(2020))
        self.assertEqual(3, dates.friday_thirteenths_this_year(2015))
