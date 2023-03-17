import matematik as matematikmodul#as ile takma ad verilir.alias takma ad
import random
from matematik import bol as bolmeIslemi #burda da istediğimiz fonksiyonları import edebiliriz.
from day3 import Human #farklı bir moduldeki sınıfı import ettik.
from selenium import webdriver #selenium import edildi

print(bolmeIslemi(12,4))
print(random.randint(0,100))


human=Human("Fırat")
human.talk("hello")

#packages
chromeDrive=webdriver.Chrome()