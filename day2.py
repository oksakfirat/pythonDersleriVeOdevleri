for i in range(4):
    print(i)
krediler =["Taşıt kredisi","İhtiyaç kredisi","Konut kredisi"]
for kredi in krediler:
    print(kredi)

krediler.append("x kredisi")#listenin sonuna eleman ekler.
krediler.extend(["y kredisi","z kredisi"])#listenin içine birden fazla eleman eklemek için kullanılır.
krediler.pop(1)# indis numarasına göre listeden eleman siler.
krediler.remove("y kredisi")#listenin içinde bulunan y kredi isimli elemanı siler.
print(krediler)
i=0
while i<len(krediler):
    print(krediler[i])
    i+=1
i=0
while i<=5:
    print(i)
    i+=1
while True:
    print("x")
    break
krediler =["Taşıt kredisi","İhtiyaç kredisi","Konut kredisi"]

#definition define
def calculate():#fonksiyon tanımlaması bu şekilde yapılır def key wordu kullanılır.
    print(100-20)
calculate()

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)
calculateWithParams(50,5)

def calculateAndReturn(price,discount):
    return price-discount
yeniFiyat=calculateAndReturn(100,45)
print(yeniFiyat)


