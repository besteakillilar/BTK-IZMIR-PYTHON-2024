# kullanıcıdan başlangıç bitiş ve artış sayılarını alın ve sayıları toplayı çarpın.

baslangic = int(input("Bir başlangıç değeri giriniz:"))
bitis = int(input("Bir bitis giriniz:"))
artis = int(input("Bir artış değeri giriniz:"))
if baslangic > bitis:
    baslangic, bitis = bitis, baslangic
toplam, carpim = 0, 1
while baslangic <= bitis:
    toplam += baslangic
    carpim *= baslangic
    baslangic += artis

metin = "Sayılarınızın Toplamı {}, Çarpımı {}"
print(metin.format(toplam, carpim))
