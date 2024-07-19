# Bir sayının, tüm basamaklarındaki rakamların sayının basamak katına toplamı kendisine eşit olan sayılara Armstrong sayısı denir.
# 1000'e kadar olan Armstrong sayılarını yazdırınız.
# kullanıcıya 10 hak vererek Armstrong sayısını oluşturup oluşturamadığını test ediniz.

# Vers.1

sayi = int(input("Bir sayı giriniz: "))
ssayi = str(sayi)
toplam = 0
for rakam in ssayi:
    kup = int(rakam) ** len(ssayi)
    toplam += kup
    print(rakam, kup, toplam)
if toplam == 1:
    print(sayi, "sayisi bir armstrong sayısıdır.")

# Vers.2
for i in range(100000):
    sayi = i
    ssayi = str(sayi)
    toplam = 0
    for rakam in ssayi:
        kup = int(rakam) ** len(ssayi)
        toplam += kup
        # print(rakam, kup, toplam)
    if toplam == sayi:
        print(sayi, "sayisi bir armstrong sayısıdır")
