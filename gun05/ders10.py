#Kullanıcıdan kitap girişi isteyerek yazdıralım.

class Kitap():
    ad = ""
    yazar = ""
    basim = ""


kitap_listesi = []

for i in range(5):
    kitap = Kitap()
    kitap.ad = input(f"{i+1}.Kitap adını giriniz: ")
    kitap_listesi.append(kitap)

