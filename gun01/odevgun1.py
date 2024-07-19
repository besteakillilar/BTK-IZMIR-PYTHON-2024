# Dairenin alanını ve çevresini hesaplayan bir program yazınız. Pi değerini ve yarı çap değerini kullanıcıdan alınız.

yaricap = float(input("Dairenin yarı çapını girin: "))
pi = float(input("Pi değerini girin: "))
alan = pi * yaricap ** 2  # Dairenin alanını hesapla pirkare
cevre = 2 * pi * yaricap  # Dairenin çevresini hesapla 2pir
print("Dairenin alanı: ", alan)
print("Dairenin çevresi:", cevre)
# print(r,"alanı:",alan,"çevresi:",çevre)

# Kullanıcının adını yaşı kadar yazdıran programı yazalım.
ad = input("Adınızı Giriniz :")
yas = int(input("Yaşınızı Giriniz:\t"))
cikti = ad * yas
print(cikti)
print(yas * ad)
