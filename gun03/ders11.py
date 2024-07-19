# Kullanıcıdan 10 tane sayı isteyip sayıların en büyüğü ve en küçüğünü bulun fakat aynı sayıların olmamasını sağlayın

sayi = int(input("sayi giriniz:"))
eb = sayi
ek = sayi
sayilar = {sayi}
while len(sayilar) < 10:
    sayilar.add(int(input("bir syaı giriniz")))
for ksayi in sayilar:
    if eb < ksayi:
        eb = ksayi
    if ek > ksayi:
       ek = ksayi
print("en büyük", eb)
print("en küçük", ek)
