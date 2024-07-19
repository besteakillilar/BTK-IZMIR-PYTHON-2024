from orm_db import *

Base.metadata.bind = engine   # db bağlantısı
DBSession = sessionmaker(bind=engine)
session = DBSession()  # oturum açtık.


def birimListele():
    birimler = session.query(Birim).all()
    for birim in birimler:
        print(birim.birim_id, birim.birim_adi)
    return birimler  # birim tablosundan sorgu => liste tipinde veri cevap

# orm veritabanından bağımsız.

def birimEkle():
    birimadi = input("Bir birim adı giriniz. : ")
    yeniBirim = Birim(birim_adi=birimadi)
    session.add(yeniBirim)
    session.commit()


def birimGuncelle():
    birimListele()
    birimid = int(input("Güncellemek istediğiniz birimin id'sini giriniz. : "))
    birim = session.query(Birim).filter(Birim.birim_id == birimid).first() # kritere göre
    yeni_birim_adi = input("Yeni birim adını giriniz. : ")
    birim.birim_adi = yeni_birim_adi
    session.commit()
    return birimListele()


def birimSil():
    birimListele()
    birimid = int(input("Silmek istediğiniz birimin id'sini giriniz. : "))
    birim = session.query(Birim).filter(Birim.birim_id == birimid).delete()
    session.commit()
    return birimListele()


birimGuncelle()
birimSil()
# Sorgular ya oturum üzerinden ya da sınıflar üzerinden yapılır.

birimler = session.query(Birim).all()
print(birimler)
birimadi = input("Bir birim adı giriniz. : ")

yeniBirim = Birim(birim_adi=birimadi)
session.add(yeniBirim)  # ekler
session.commit()  # veritabanına yazar
print(birimler)
