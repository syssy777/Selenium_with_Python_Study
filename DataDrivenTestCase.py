import xlsUtilsModule
from selenium import webdriver

myBrowser = webdriver.Chrome(executable_path="C:/Users/Ntokozo/Downloads/chromedriver.exe")
myBrowser.get('http://newtours.demoaut.com/')
myBrowser.maximize_window()
path = 'loginTest.xlsx'
rows = xlsUtilsModule.GetRowCount(path,'Sheet1')
for r in range(2,rows+1):
    username = xlsUtilsModule.ReadData(path,'Sheet1',r,2)
    password = xlsUtilsModule.ReadData(path, 'Sheet1', r, 2)
    myBrowser.find_element_by_name('userName').send_keys(username)
    myBrowser.find_element_by_name('password').send_keys(password)
    login = myBrowser.find_element_by_name('login').click()

    if myBrowser.title == 'Find a Flight: Mercury Tours:':
        print('Test Passed')
        xlsUtilsModule.WriteData(path,'Sheet1',r, 3, 'Test Passed')
    else:
        print('Test Failed')
        xlsUtilsModule.WriteData(path, 'Sheet1', r, 3, 'Test Failed')
    myBrowser.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a').click()
