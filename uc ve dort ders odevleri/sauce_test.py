from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Test_Sauce_Otomasyonu:
    chromeDriver=webdriver.Chrome()
    chromeDriver.get("https://saucedemo.com")
    inputName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
    inputPassword=chromeDriver.find_element(By.ID,"password")
    loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
    def emptyLogin(self):
       loginButton=self.chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
       loginButton.click()
       sleep(2)
       errorName=self.chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
       resultlogin=errorName.text=="Epic sadface: Username is required"
       print(resultlogin)

    def emptyPassword(self):
        inputName=self.chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
        inputName.send_keys("firat")
        loginButton=self.chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        errorPassword=self.chromeDriver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        resultPassword=errorPassword.text=="Epic sadface: Password is required"
        print(resultPassword)
    
    def userLocked(self):
        inputName=self.chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
        inputName.send_keys("locked_out_user")
        inputPassword=self.chromeDriver.find_element(By.ID,"password")
        inputPassword.send_keys("secret_sauce")
        loginButton=self.chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        errorLocked=self.chromeDriver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorLocked.text=="Epic sadface: Sorry, this user has been locked out.")
    def x_IconClose(self):
        loginButton=self.chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        sleep(2)
        xIconClose=self.chromeDriver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        xIconClose.click()
    def successLogin(self):
        self.inputName.send_keys("standard_user")
        self.inputPassword.send_keys("secret_sauce")
        self.loginButton.click()
        productCount=self.chromeDriver.find_elements(By.CLASS_NAME,"inventory_item")
        sleep(2)
        print(f"sitede {len(productCount)} tane ürün bulunmaktadır.")





       

testSauce=Test_Sauce_Otomasyonu()
testSauce.emptyLogin()
testSauce.emptyPassword()
testSauce.userLocked()
testSauce.x_IconClose()
testSauce.successLogin()

while True:
    continue

