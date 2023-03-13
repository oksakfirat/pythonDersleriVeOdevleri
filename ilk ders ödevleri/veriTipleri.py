#eğitmen ad soyad veri tipi olarak str kullanılmıştır.
egitmenAd="Halit"
egitmenSoyad="kalaycı"

#kategori ve eğitmen kısımında veriler list veri tipi kullanılmış.
kategoriler=["yazılım","programlama","grafik tasarım"]
egitmenler=["Engin demiroğ","Halit kalaycı"]

for kategori in kategoriler:
    print(kategori)

for egitmen in egitmenler:
    print(egitmen)

#kursa kayıtlı değilse kurs içeriği gösterme burda veri tipi olarak bool kullanılmış ve denetleme olarak if else kullanılmış 
kursaKayitOl=False
if kursaKayitOl:
    print("Kurs içeriği")
else:
    print("Kursa kayıt ol")

#Kurs ilerleme durumu numerik veri tipi(int,float) kullanılmış.
kursIlerlemeDurumu=50
