dosya_adi = "deneme.txt"
with open(dosya_adi) as dosya:
    print(dosya.readline())
    print(dosya.readline())

with open(dosya_adi) as dosya:
    metin = dosya.read()
    satirlar = metin.split("\n")
    print(satir for satir in satirlar)
    for i in satirlar: print(i)
