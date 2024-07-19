# pazar list kullanıcıdan alacağı malzeme bilgisini isteyerek liste oluşturma
# verse 1 for loop

adet = int(input("Kaç farklı malzeme alacaksınız ?"))
malzeme = []
for i in range(1, adet + 1):
    urun = input(f"{i}. ürün bilgisini giriniz :")
    malzeme.append(urun)

for urun in malzeme:
    print(urun, end="\t")

# verse 2 while loop

mesaj = """Pazar Listesi Oluşturma Programına Hoşgeldiniz !
           Programdan çıkmak için lütfen X'e basınız."""  # 3 tırnak kullanıldığında str enterı algılar
print(mesaj)
malzeme = []
while True:
    urun = input("Ürün girişi yapınız.")
    if urun.lower() == "x":
        print("Pazar Listeniz", malzeme)
        break
    elif urun.lower() == "":
        continue
    else:
        malzeme.append(urun)
