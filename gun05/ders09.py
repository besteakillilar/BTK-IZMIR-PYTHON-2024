class Kitap():
    ad = ""
    yazar = ""
    yayin_evi = ""
    tur = ""
    sayfa = ""
    basim_yili = ""


kitap1 = Kitap()
kitap1.ad = "Bestenin kitabı"
kitap1.yazar = "Beste Akıllılar"
kitap1.yayin_evi = "BTK Yayınları"
kitap1.sayfa = 352
kitap1.basim_yili = 2024

print(kitap1.ad)

kitap_bilgiler = vars(kitap1)
print(kitap_bilgiler)

kitaplik_bilgileri = vars(Kitap)
print(kitaplik_bilgileri)
