import unittest
from test_base import captured_io, captured_output
from io import StringIO
import scheduler


class MyTestCase(unittest.TestCase):
    def test_date(self):
        with captured_io(StringIO('a\naa\n')) as (out, err):
            scheduler.Display()
            output = out.getvalue().strip()
            self.assertEqual("", output)


if __name__ == '__main__':
    unittest.main()
