from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Test_Sauce:  
    
    def emptyLogin(self):
       chromeDriver=webdriver.Chrome()
       chromeDriver.get("https://saucedemo.com")
       loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
       loginButton.click()
       sleep(2)
       errorName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
       sleep(2)
       resultlogin=errorName.text=="Epic sadface: Username is required"
       print(resultlogin)

    def emptyPassword(self):
        chromeDriver=webdriver.Chrome()
        chromeDriver.get("https://saucedemo.com")
        inputName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
        inputName.send_keys("firat")
        sleep(2)
        loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        errorPassword=chromeDriver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        resultPassword=errorPassword.text=="Epic sadface: Password is required"
        print(resultPassword)
    
    def userLocked(self):
        chromeDriver=webdriver.Chrome()
        chromeDriver.get("https://saucedemo.com")
        inputName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
        inputPassword=chromeDriver.find_element(By.ID,"password")
        loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        inputName.send_keys("locked_out_user")
        inputPassword.send_keys("secret_sauce")
        loginButton.click()
        errorLocked=chromeDriver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorLocked.text=="Epic sadface: Sorry, this user has been locked out.")
    
    def x_IconClose(self):
        chromeDriver=webdriver.Chrome()
        chromeDriver.get("https://saucedemo.com")
        loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        sleep(3)
        xIconClose=chromeDriver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        xIconClose.click()
   
    def successLogin(self):
        chromeDriver=webdriver.Chrome()
        chromeDriver.get("https://saucedemo.com")
        inputName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
        inputPassword=chromeDriver.find_element(By.ID,"password")
        loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        inputName.send_keys("standard_user")
        inputPassword.send_keys("secret_sauce")
        loginButton.click()
    
    def productCount(self):
        chromeDriver=webdriver.Chrome()
        chromeDriver.get("https://saucedemo.com")
        inputName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
        inputPassword=chromeDriver.find_element(By.ID,"password")
        loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        inputName.send_keys("standard_user")
        inputPassword.send_keys("secret_sauce")
        loginButton.click()
        sleep(3)
        productCount=chromeDriver.find_elements(By.CLASS_NAME,"inventory_item")
        sleep(2)
        print(f"sitede {len(productCount)} tane ürün bulunmaktadır.")




testSauce=Test_Sauce()
testSauce.emptyLogin()
testSauce.emptyPassword()
testSauce.userLocked()
testSauce.x_IconClose()
testSauce.successLogin()
testSauce.productCount()

while True:
    continue

