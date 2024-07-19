def ogrenciKarti(a,b,c,d=8,*args,**kwargs):  # tek * tuple ** yıldız dictionary tipi için kullanılır.
    print(a,b,c,d)
    print(args)
    print(kwargs)
    o_bilgileri = {**kwargs}
    print(o_bilgileri)
    pass


ogrenciKarti(1,2,3,4, 56,53,oAdi="beste", oSoyadi="akıllılar", oBolum="mekatronik")
