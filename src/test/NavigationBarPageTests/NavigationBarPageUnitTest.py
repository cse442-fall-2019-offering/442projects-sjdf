import unittest
from src.core.navbar import navbar


class TestNavBar(unittest.TestCase):
    def test_valid_date(self):
        navBar = navbar.NavBar()
        self.assertLess(navBar.getDates()[0], navBar.getDates()[1], "Starting date can't come after End date")


    def test_valid_currency_format(self):
        navBar = navbar.NavBar()
        self.assertTrue((type(navBar.getMoneyAmount()) is int) or (type(navBar.getMoneyAmount() is float)),"Money is not a number")
        self.assertNotEqual(0, navBar.getMoneyAmount(), "Money amount is zero")
        self.assertLess(0, navBar.getMoneyAmount(), "Money amount is negative")


if __name__ == '__main__':
    unittest.main()