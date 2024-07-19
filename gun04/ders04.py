import random

rastgele = random.randrange(1, 100)
print("Tutulan sayı: ", rastgele)
tahminSayisi = 10
taban = 0
tavan= 100
while tahminSayisi >= 1:
    tahmin = random.randrange(taban, tavan) # bilgisayarın kendi tuttuğu sayı
    tahmin = int(input("sayı giriniz"))
    print(tahmin, end =" ")
    if tahmin == rastgele:
        print("Tebrikler")
        break
    elif tahmin > rastgele:
        print("Daha Küçük")
        tavan = tahmin
    elif tahmin < rastgele:
        print("Daha Büyük")
        tavan = tahmin


