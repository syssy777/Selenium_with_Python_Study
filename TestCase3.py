import unittest
from selenium import webdriver


class AppTesting(unittest.TestCase):
    @classmethod
    def test_SetUpClass(cls):  # Executes once the class is intitiated
        print('open Application')

    @classmethod
    def test_SetUp(self):  # Executes before every method in the class
        print("login test")

    def test_Search(self):
        print('search test')

    @unittest.SkipTest  # this will completely skip this particular test method
    def test_AdvancedSearch(self):
        print('Advanced Search test')

    def test_twitterSearch(self):
        print('twitter Search test')

    @unittest.skipIf('artist' != '#5', 'Not the main artist')
    def test_ArtistSearch(self):
        print(' Artist Search test')

    @unittest.skip('Skipping bcoz it\'s not ready')  # this will temporally skip this particular test method with reason
    def test_ForexSearch(self):
        print('Forex Search test')

    @classmethod
    def tear_Down(self):  # Executes after every method in the class
        print("logout")

    @classmethod
    def tear_DownClass(cls):  # Executes once the class is completed
        print('close Application')


'''# ASSERTIONS ==============================================================================================
class SearchEngine(unittest.TestCase):
    def test_GoogleSearch(self):
        self.myBrowser = webdriver.Chrome(executable_path="C:/Users/Ntokozo/Downloads/chromedriver.exe")
        self.myBrowser.get('https://www.google.com/')
        webPageTitle = self.myBrowser.title
        print("TITLE = ", webPageTitle)

        # you can also use assertTrue, assertFalse to verify the test below
        #self.assertEqual('Google',webPageTitle,msg='Webpage Titles Not Matched')  # if titles are the same.test passed
        #self.assertNotEqual('Google147', webPageTitle, msg='Webpage Titles Matched')  # if different titles.test passed



        #self.myBrowser = None
        #self.assertIsNone(self.myBrowser)  # verifies any variable
        #self.assertIsNot(self.myBrowser)


    def search_list(self):
        list = ['peter','james','python']
        #self.assertIn('python',list)  # if present, the test will pass.
        self.assertIn('fifi', list)   # if not present, the test will fail.



        self.myBrowser.close()
'''






if __name__ == '__main__':
    unittest.main()
