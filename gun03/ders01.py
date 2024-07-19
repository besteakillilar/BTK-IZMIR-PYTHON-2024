# List Items - Data Types

ogrenci_adi = "Beste"
ogrenci_soyadi = "Akıllılar"
ogrenci_yas = 23
ogrenci_boy = 1.63
ogrenci_cinsiyet = True

ogrenci_bilgisi = [ogrenci_adi,ogrenci_soyadi,ogrenci_yas,ogrenci_boy,ogrenci_cinsiyet]
print(ogrenci_bilgisi)
print(ogrenci_bilgisi[0])
print(ogrenci_bilgisi[-1])
print(ogrenci_bilgisi[:2])
print(len(ogrenci_bilgisi))   # List Length
print(ogrenci_bilgisi[-1:])   # type()

print(type(ogrenci_bilgisi))

for bilgi in ogrenci_bilgisi:
    print(bilgi)
