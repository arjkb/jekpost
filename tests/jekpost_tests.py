import unittest
import jekpost_create as jek

from datetime import date

class JekpostTests(unittest.TestCase):
    def test_date_gets_formatted(self):
        """
        Check
            31-DEC-2016 (2016-12-31)
            1-NOV-2015  (2015-11-01)
            11-JAN-2015 (2015-01-11)
        """
        sample_dates = [    (date(2016, 12, 31), '2016-12-31'),
                            (date(2015, 11, 1), '2015-11-01'),
                            (date(2015, 1, 11), '2015-01-11')
                       ]
                       
        for date_object, expected_date in sample_dates:
            with self.subTest(i=date_object):
                formatted_date = jek.get_date_formatted(date_object)
                self.assertEqual(formatted_date, expected_date)

if __name__ == '__main__':
    unittest.main()
