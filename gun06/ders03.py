# PYTHON INHERITANCE

class Ogrenci():
    def __init__(self, ad, soyad):  #The __init__() function is called automatically every time the class is being used to create a new object.
        self.ad = ad
        self.soyad = soyad


class FOgrenci(Ogrenci):
    def __init__(self, ad, soyad, fakulte):
        Ogrenci.__init__(self, ad, soyad)   #super().__init__(self,ad,soyad)  // super() function that will make the child class inherit all the methods and properties from its parent
        self.fakulte = fakulte


class BOgrenci(FOgrenci):
    def __init__(self, ad, soyad, fakulte, bolum):
        FOgrenci.__init__(self, ad, soyad, fakulte)
        self.bolum = bolum


ogr = Ogrenci("BESTE", "AKILLIAR")
Fogr = FOgrenci("XX","YY","ZZ")
Bogr = BOgrenci("MM","NN","BB", "WW")

print(vars(ogr))
print(vars(Fogr))
print(vars(Bogr))