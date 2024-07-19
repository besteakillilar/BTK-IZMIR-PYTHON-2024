#kullanıcıdan başlangıç bitiş ve artış sayılarını alın ve sayıları toplayı çarpın.


baslangic = int(input("Bir başlangıç değeri giriniz:"))
bitis =int(input("Bir bitis giriniz:"))
artis = int(input("Bir artış değeri giriniz:"))
toplam, carpim =0,1
for i in range(baslangic, bitis, artis):
    print(i)
    toplam += i
    carpim *= i
metin = "Sayılarınızın Toplamı {}, Çarpımı {}"
print(metin.format(toplam, carpim))


