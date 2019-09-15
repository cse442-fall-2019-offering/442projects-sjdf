
import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def setUpBrowser(browser,webdriver):
    print("Run "+browser+" start at: " + str(datetime.datetime.now()))
    print("Chrome envirerment set up")
    print("-------------------------------------")
    webdriver.implicitly_wait(20)
    webdriver.maximize_window()

def tearDownBrowser(browser,webdriver):
    print("-------------------------------------")
    print("Run "+browser+" Completed at :" + str(datetime.datetime.now()))
    webdriver.close()
    webdriver.quit()
# mac test
class seleniumMacsUnitTest(unittest.TestCase):
    def setUp(self):
        self.ChromeBrowser = webdriver.Chrome(executable_path="../Selenium/macsDrivers/chromedriver.exe")
        setUpBrowser("Chrome",self.ChromeBrowser)
        self.SafariBrowser = webdriver.Safari();
        setUpBrowser("Safari", self.SafariBrowser)
        self.FirefoxBrowser = webdriver.Firefox(executable_path="../Selenium/macsDrivers/geckodriver.exe");
        setUpBrowser("FireFox", self.FirefoxBrowser)

    def test_Chrome(self):
        ChromeBrowser = self.ChromeBrowser
        ChromeBrowser.get("http://www.python.org")
        self.assertIn("Python", ChromeBrowser.title)
        elem = ChromeBrowser.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in ChromeBrowser.page_source

    def test_Safari(self):
        SafariBrowser = self.SafariBrowser
        SafariBrowser.get("http://www.python.org")
        self.assertIn("Python", SafariBrowser.title)
        elem = SafariBrowser.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in SafariBrowser.page_source

    def test_Firefox(self):
        FirefoxBrowser = self.FirefoxBrowser
        FirefoxBrowser.get("http://www.python.org")
        self.assertIn("Python", FirefoxBrowser.title)
        elem = FirefoxBrowser.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in FirefoxBrowser.page_source

    def tearDown(self):
        if self.ChromeBrowser!=None:
            tearDownBrowser("chrome",self.ChromeBrowser)
        if self.SafariBrowser!=None:
            tearDownBrowser("safari",self.SafariBrowser)
        if self.FirefoxBrowser!=None:
            tearDownBrowser("firefox",self.FirefoxBrowser)

if __name__ == '__main__':
    unittest.main()