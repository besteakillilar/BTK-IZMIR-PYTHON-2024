# CREATE A DATABASE
# ORM :
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *  # tablolar arası ilişki kurmak için
from sqlalchemy import *

Base = declarative_base()

#Base = declarative_base()  =>  class Birim(Base): KALITIM
class Birim(Base):
    __tablename__ = 'birim'

    birim_id = Column(Integer, primary_key=True, autoincrement=True)
    birim_adi = Column(String(100), nullable=False, default="Birimsiz")

    def __repr__(self):
        return self.birim_adi  # birimin isim bilgisi bize geri dönsün diye.


engine = create_engine('sqlite:///deneme.sqlite')  # bağlantı için
Base.metadata.create_all(engine)  # oluşan db'i kendi tanımlamamıza eklemek için / base'den türüyenleri alıp tanımlamak

#MVC (Model View Controller) :