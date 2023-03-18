from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test_Sauce:
    def test_invalid_login(self):
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.get("https:saucedemo.com")
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        login=driver.find_element(By.ID,"login-button")
        sleep(2)
        userNameInput.send_keys("firat")
        passwordInput.send_keys("12344")
        sleep(2)
        login.click()
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testSonucu=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(testSonucu)
        

testClass=Test_Sauce()
testClass.test_invalid_login()
sleep(20)
while True:
    continue