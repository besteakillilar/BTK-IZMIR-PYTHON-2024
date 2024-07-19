class Fatura():
    baslik = "Beste Pazarlama"
    odeme = True

    def __init__(self, m_adi, v_no, tarih):
        self.m_adi = m_adi
        self.v_no = v_no
        self.tarih = tarih
        self.tutar = 0
        self.icerik = {}

    def urunEkle(self):
        urun_ad = input("Ürün bilgisi giriniz.")
        urun_fiyati = int(input(f"{urun_ad} fiyatını giriniz."))
        urun_adet = int(input(f"{urun_ad} adetini giriniz."))
        urun_tutar = urun_adet * urun_fiyati
        self.tutar += urun_tutar
        self.icerik[urun_ad] = [urun_ad, urun_fiyati, urun_adet, urun_tutar]
        print(self.icerik[urun_ad], "ürün sepete eklendi.")
        return self.tutar

    def urunCikar(self):
        urun_ad = input("Çıkarılacak ürünün bilgisi giriniz.")
        urun_tutar = self.icerik[urun_ad][3]  # urun_ad, urun_fiyati, urun_adet, urun_tutar(3.index)
        self.tutar -= urun_tutar
        print(self.icerik[urun_ad], "ürün sepetten çıkarıldı.")
        self.icerik.pop(urun_ad)  #remove / del / pop
        return self.tutar

    def faturaTutari(self):
        print("Güncel fatura tutarı : " , self.tutar)
        return self.tutar

    def __str__(self):
        return self.m_adi + " adlı müşterinin faturası."


musteri = Fatura("beste", "2000", "bugün")


while True:
    cevap = int(input("urun ekle 1 \t  çıkart: 2\t,  Göster : 3\t"))
    if cevap == 1:
        musteri.urunEkle()
    elif cevap == 2:
        musteri.urunCikar()
    elif cevap == 3:
        musteri.faturaTutari()
    else:
        print("hatalı işlem girişi")


