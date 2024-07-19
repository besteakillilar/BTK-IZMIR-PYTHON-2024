# Kullanıcıdan alınan sayıları küçükten büyüğe sıralayalım.

def for_dongusu(baslangic, bitis=0, artis=1):
    for_listesi = []

    def sirala(baslangic, bitis,
               artis=artis):  # ilk artıs kodu sıralamak için bir değisken olarak tanımlar, artis=artis dışardan değer atar.
        if baslangic <= bitis:
            for_listesi.append(baslangic)
            baslangic += artis
            return sirala(baslangic, bitis)
        return for_listesi

    if baslangic > bitis:
        return sirala(bitis, baslangic)
    else:
        return sirala(baslangic, bitis)


print(for_dongusu(5, 20, 2))
