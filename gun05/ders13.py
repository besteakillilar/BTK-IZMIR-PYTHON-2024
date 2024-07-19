class Kedi():
    pati = 4
    kuyruk = True

    def __init__(self, ad, adim):
        self.ad = ad
        self.adim = adim

    def yurume(self):
        print(self.ad, self.adim, "adım attı.")

    @classmethod
    def miyav(cls):
        print("miyav dedi")


tekir = Kedi("Tekir", 4)

print(tekir.ad)
print(tekir.adim)
tekir.yurume()

#tekir.miyav() == kedi.miyav()
