# PYTHON TYPE CONVERSION

sayi = 15
ssayi = str(sayi)
print(sayi, ssayi)  # ilki 15 ikincisi bir beş
print(sayi * 2, ssayi * 2)

# bir x değerini stringe dönüştürmek istersek str() methodu kullanılır.

numara = "782"
inumara = int(numara)
print(inumara, numara)
print(inumara * 2, numara * 2)

ondalikli = "12.5"
osayi = float(ondalikli)
print(osayi, ondalikli)
print(osayi * 2, ondalikli * 2)

iosayi = int(osayi)
ossayi = float(sayi)
print(ossayi, ossayi)

mantik = "False"  # çift tırnağın içinde ne olursa olsun true çıkacak eğer boş olursa false
smantik = bool(mantik)
print(smantik)

mantik = 5  # 0 olursa false     #int to bool
imantik = bool(mantik)
print(imantik)

bifade = False  # hersey stringe dönüşür    #bool to str
bmetin = str(bifade)
print(bmetin)

bsayi = False  # bool to int
isayi = int(bsayi)
print(isayi)

bsayi = True  # bool to int
isayi = int(bsayi)
print(isayi)
