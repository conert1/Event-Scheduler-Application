import unittest
from test_base import captured_io, captured_output
from io import StringIO
import scheduler


class MyTestCase(unittest.TestCase):
    def test_display(self):
        with captured_io(StringIO('a\naa\n')) as (out, err):
            scheduler.Display()
            output = out.getvalue().strip()
            self.assertEqual("", output)

    def test_time(self):
        with captured_io(StringIO('a\naa\n11:11')) as (out, err):
            scheduler.time()
            output = out.getvalue().strip()
            self.assertEqual("Enter the time\nplease Enter a valid time HH:MM\nplease Enter a valid time HH:MM", output)


    def test_date(self):
        with captured_io(StringIO('136-65-55\n2024-01-01')) as (out, err):
            scheduler.date()
            output = out.getvalue().strip()
            self.assertEqual("enter the date\nSorry invalid date please enter date in the format YYYY-MM-DD", output)

if __name__ == '__main__':
    unittest.main()
