class Urun():
    def __init__(self):
        self.urun_ad = input("Ürün bilgisi giriniz")
        self.urun_fiyati = int(input(f"{self.urun_ad} fiyatını giriniz"))
        self.urun_adet = int(input(f"{self.urun_ad} adetini giriniz"))
        self.urun_tutar = self.urun_adet * self.urun_fiyati

    def adetArttir(self):
        pass

    def adetAzalt(self):
        pass

    def __str__(self):
        return (self.urun_ad, self.urun_tutar)


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
        urun_ad = input("Ürün bilgisi giriniz")
        urun_fiyati = int(input(f"{urun_ad} fiyatını giriniz"))
        urun_adet = int(input(f"{urun_ad} adetini giriniz"))
        urun_tutar = urun_adet * urun_fiyati
        self.tutar += urun_tutar
        self.icerik[urun_ad] = [urun_ad, urun_adet, urun_fiyati, urun_tutar]
        print(self.icerik[urun_ad], " Ürün sepete eklendi")
        return self.tutar

    def urunCikar(self):
        urun_ad = input("Çıkarılacak ürünün bilgisini giriniz")
        # urun_adet = int(input(f"{urun_ad} adet bilgisi"))
        urun_tutar = self.icerik[urun_ad][3]
        self.tutar -= urun_tutar
        print(self.icerik[urun_ad], " ürün sepetten çıkartıldı")
        self.icerik.pop(urun_ad)
        return self.tutar

    def faturaTutari(self):
        print("Güncel fatura tutarı", self.tutar)
        return self.tutar

    def __str__(self):
        return self.m_adi + " adlı müşterinin faturası."


musteri = Fatura("beste", "2000", "bugün")

while True:
    cevap = int(input("Ürün ekle 1 \t  Ürün çıkar: 2\t,  Göster : 3\t"))
    if cevap == 1:
        musteri.urunEkle()
    elif cevap == 2:
        musteri.urunCikar()
    elif cevap == 3:
        musteri.faturaTutari()
    else:
        print("hatalı işlem girişi yapıldı.")
