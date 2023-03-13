
def ogrenciEkle():
    ogrenciListesi=[]
    for i in range(3):
        ogrenciAdiSoyadi=input("Öğrenci adı soyadını giriniz")
        ogrenciListesi.append(ogrenciAdiSoyadi)
    for ogrenci in ogrenciListesi:
        print(ogrenci)

def kayitSil():
    ogrenciListesi=["Fırat okşak","Engin Demiroğ","Halit kalaycı"]
    kayitSil=input("silmek istediğin öğrenci ad soyad giriniz")
    for ogrenci in ogrenciListesi:
        if kayitSil==ogrenci:
            ogrenciListesi.remove(kayitSil)
            print("Kayıt silindi")

def cokluKayitSil():
    ogrenciListesi=["Fırat okşak","Engin Demiroğ","Halit kalaycı"]
    print(ogrenciListesi)
    kayitSilmeSayisi=int(input("Kaç öğrenci silmek istersiniz"))
   
    if len(ogrenciListesi)>kayitSilmeSayisi or len(ogrenciListesi)==kayitSilmeSayisi:
        i=0
        while i<kayitSilmeSayisi:
            kayitSil=input("silmek istediğin öğrenci ad soyad giriniz")
            for ogrenci in ogrenciListesi:
                if ogrenci==kayitSil:
                    print("kayıt silindi" + ogrenci)
                    ogrenciListesi.remove(ogrenci)
                    
            i+=1
    else:
        print("Girdiğiniz Sayıda listede öğrenci bulunmamaktadır.")
    print(ogrenciListesi)

def ogrenciNumara():
    ogrenciListesi=["Fırat okşak","Engin Demiroğ","Halit kalaycı"]
    i=0
    while i<len(ogrenciListesi):
        print(ogrenciListesi[i] +" "+ f"öğrenci numrası {i}")
        i+=1

cokluKayitSil()