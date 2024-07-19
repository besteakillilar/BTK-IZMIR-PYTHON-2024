# kullanıcıdan 10 adet sayı alarak girdiği sayıların en büyük ve en küçük değerini ve sırasını yazdıran prrogram örneği.

sayilar = []
for i in range(10):
    sayi = int(input(f"{i + 1}. sayıyı giriniz: "))
    sayilar.append(sayi)
print(sayilar)

# verse 1
sayilar2 = sayilar.copy()
sayilar.sort()
eb = sayilar[-1]
ek = sayilar[0]
print(sayilar2, eb, ek)

# verse 2
eb = max(sayilar)
ek = min(sayilar)
print(sayilar, eb, ek)

# verse 3
eb = ek = sayilar[0]
for sayi in sayilar:
    if sayi > eb:
        eb = sayi
    if sayi < ek:
        ek = sayi
metin1 = "{} en küçük sayı, {} en küçük sırası".format(ek, sayilar.index(ek) + 1)
metin2 = "{} en büyük sayı, {} en büyük sırası".format(eb, sayilar.index(eb) + 1)
print(sayilar, metin1, metin2, sep="\n")
