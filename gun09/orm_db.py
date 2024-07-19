from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from sqlalchemy import *

Base = declarative_base()


class User(Base):  # sınıf tablonun olmusmasını saglayacak.
    __tablename__ = 'user'
    user_adi = Column(String(100), nullable=False)
    user_id = Column(Integer, primary_key=True, autoincrement=True)  # primary key
    user_sifre = Column(String(100), nullable=False)

    def __repr__(self):
        return f'{self.user_id}-{self.user_adi}'

    # bire çok eşleşme

class Kitaplik(Base):
        __tablename__ = 'kitaplik'
        kitap_id = Column(Integer, primary_key=True, autoincrement=True)
        kitap_adi = Column(String(100), nullable=False)
        kitap_sayfa_sayisi = Column(Integer, nullable=False)
        kitap_user = Column(Integer, ForeignKey('user.user_id'))

    # kitaplik.sqlite oluşturmak ve tanımlanan tabloları oluşturulan veritabanına eklemek için aşağıdaki kodları yazıyoruz.

engine = create_engine('sqlite:///kitaplik.sqlite')
Base.metadata.create_all(engine)
