class Ogrenci():
    bolum = "Bilişim"
    kurs = "BTK Akademi"

    def __init__(self):
        print("Öğrenci Oluşturuldu.")
        self.ad = ""
        self.soyad = ""
        self.tcno = ""


ogr1 = Ogrenci()
print(ogr1.bolum)
print(ogr1.kurs)
ogr1.ad = "Beste"
print(ogr1.ad)

print(vars(ogr1))

ogr2 = Ogrenci()
print(ogr2.bolum)
print(ogr2.kurs)
ogr2.ad = "A"
print(ogr2.ad)

print(vars(ogr2))
