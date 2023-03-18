from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()#açılan chrome penceresinin tam ekran şekilde açılmasını sağlar.
driver.get("https://www.google.com")#verdiğimiz url açmamızı sağlar.
sleep(5)
input=driver.find_element(By.NAME,"q")#googledeki inputa name q olanı getir.
input.send_keys("kodlamaio")#inputa yazı yazmamızı sağlar.
searchButton=driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()#butona tıklamamızı sağlar.
firstResult=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a")#arama sonucunda çıkan kodlama.io sitesinin html içindek yolunu aldık.
firstResult.click()
listOfCourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"kodalma io sitesinde şuanda {len(listOfCourses)} sayıda kurs var.")

while True:
    continue

#sleep(10)#tarayıcının 10 saniye beklemesini sağlar.
