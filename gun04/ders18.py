def ogrenciKarti(**kwargs):
    print(kwargs)
    o_bilgileri = {**kwargs}
    print(o_bilgileri)
    pass


ogrenciKarti(oAdi="beste", oSoyadi="akıllılar", oBolum="mekatronik")
