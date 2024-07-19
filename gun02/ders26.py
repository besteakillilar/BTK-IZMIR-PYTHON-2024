if True:
    pass
print("hello")

for dd in range(20):
    if dd == 15:
        break
    print(dd)
#break döngünün bitirlmesini sağlar
for dd in range(20):
    ad = input("Adınızı giriniz")
    if dd == "Beste":
        print("Beste bulundu")
        break
    print(dd)

for dd in range(20):
    ad = input("Adınızı giriniz")
    if dd == "Beste":
        print("Beste kayıt yapılamaz")
        continue
    soyad = input("Soyadınızı giriniz.")
    print(ad,soyad,"kayıt tamamlandı")

