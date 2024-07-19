class Calisan():
    sirket = "btkIzmırPython"

    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.fEpostaOlustur()

    def fEpostaOlustur(self):
        return self.ad + self.soyad + "@btk.com"

    @classmethod  # class bellekte yer tutmaz.
    def fSirketDegis(cls):
        cls.sirket = input("Yeni Şirket Adını Giriniz")
        return cls.sirket

    def __str__(self):
        return self.ad + self.soyad


print(Calisan.sirket)
calisan1 = Calisan("hamza", "can", "20001")
print(calisan1)
print(calisan1.eposta)
print(calisan1.sirket)
calisan1.sirket = "IBM"
calisan1.maas *= 33
Calisan.fSirketDegis()
print(calisan1.sirket)
calisan2 = Calisan("şakir", "candar", "82364o")
print(calisan2.sirket)
