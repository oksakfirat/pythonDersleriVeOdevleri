#sınıflar =>classlar
#modules
#paket yönetimi
#self=>this diğer programlama dilerinde kullanılır.
class Human:
    #built-in
    #initialize
    def __init__(self,name):#constroctor böyle oluşturulmaktadır.
        self.name=name
        print("Human instance oluşturuldu")

    def talk(self,sentence):
        print(f"{self.name}:{sentence}")
    def walk(self):
        print(f"{self.name} is walk...")

#instance=>örnek oluşturma
human1=Human("cem")
human1.talk("Merhaba")
human1.walk()

human2=Human("fırat")
human2.talk("Selam")
human2.walk()
