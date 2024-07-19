# PYTHON FILE HANDLING

dosya = open("deneme.txt")
print(dosya.read())
print(dosya.read(1))
print(dosya.readline())

satirlar = dosya.readlines()
print(satirlar)
for satir in satirlar:
    print(satir, end="")

okuma1 = dosya.read()
print(okuma1)
okuma2 = dosya.read()
print(okuma2)  # Dosyayı 1 kere okuyabiliyor,sona geldiği için
dosya.close()  # Dosyayı kapatır.

# Bir dosya içinde birden fazla işlem yapacaksan eğer bellekte sorun olmaması için işlmei yap ve kaydet.
