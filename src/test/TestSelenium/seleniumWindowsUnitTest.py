
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
# windows selinium webtests
class seleniumWindowsUnitTest(unittest.TestCase):
    def setUp(self):
        self.ChromeBrowser = webdriver.Chrome(executable_path="../Selenium/windowsDrivers/chromedriver.exe")
        setUpBrowser("Chrome",self.ChromeBrowser)
        self.EdgeBrowser = webdriver.Edge(executable_path="../Selenium/windowsDrivers/MicrosoftWebDriver.exe");
        setUpBrowser("Edge", self.EdgeBrowser)
        self.FirefoxBrowser = webdriver.Firefox(executable_path="../Selenium/windowsDrivers/geckodriver.exe");
        setUpBrowser("FireFox", self.FirefoxBrowser)

    def test_Chrome(self):
        ChromeBrowser = self.ChromeBrowser
        ChromeBrowser.get("http://www.python.org")
        self.assertIn("Python", ChromeBrowser.title)
        elem = ChromeBrowser.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in ChromeBrowser.page_source

    def test_Edge(self):
        EdgeBrowser = self.EdgeBrowser
        EdgeBrowser.get("http://www.python.org")
        self.assertIn("Python", EdgeBrowser.title)
        elem = EdgeBrowser.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in EdgeBrowser.page_source

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
        if self.EdgeBrowser!=None:
            tearDownBrowser("edge",self.EdgeBrowser)
        if self.FirefoxBrowser!=None:
            tearDownBrowser("firefox",self.FirefoxBrowser)

if __name__ == '__main__':
    unittest.main()
