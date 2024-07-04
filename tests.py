import unittest
import demoblaze as run

class DemoblazePositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_demoblaze():
        run.setUp()
        run.sign_up()
        run.log_in()
        run.checkout_cart()
        run.log_out()
        run.tearDown()

if __name__ == '__main__':
    unittest.main()

