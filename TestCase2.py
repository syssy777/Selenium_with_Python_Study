import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def SetUp(self):
        self.myBrowser = webdriver.chrome(executable_path="C:/Users/Ntokozo/Downloads/chromedriver.exe")
        self.myBrowser.maximise_window()

    def Test_Search_In_Python_Org(self):

        self.myBrowser.get("https://fred.stlouisfed.org/")
        print(self.myBrowser.title)
        self.assertIn("Real Gross Domestic Product (GDPC1)",self.myBrowser.title)
        elem = self.myBrowser.find_element_by_name("ltr").clear()
        elem.send_keys('gross gdp')
        elem.send_keys(Keys.RETURN)
        assert "no result found." not in self.myBrowser.page_source


    def Tear_Down(self):
        self.myBrowser.close()


'''class SearchEngine(unittest.TestCase):
    def test_GoogleSearch(self):
        self.myBrowser = webdriver.Chrome(executable_path="C:/Users/Ntokozo/Downloads/chromedriver.exe")
        self.myBrowser.get('https://www.google.com/')
        print("TITLE = ", self.myBrowser.title)
        self.myBrowser.close()

    def test_BingSearch(self):
        self.myBrowser = webdriver.Chrome(executable_path="C:/Users/Ntokozo/Downloads/chromedriver.exe")
        self.myBrowser.get('https://www.bing.com/')
        print("TITLE = ", self.myBrowser.title)
        self.myBrowser.close()'''



if __name__ == "__main__":       # running the entire methods as a module
    unittest.main()
