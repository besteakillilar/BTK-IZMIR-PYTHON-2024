# Python Sets
#çoklu veri olamaz ve sırasızdır,değiştirilebilir
# tekil veri ise random kullanmak yerine sete çevirip yapılabilir.

ogrenciler ={"Ali","Veli","Can","Kaan","Kadir"}
print(ogrenciler)  #her run yapıldığında küme içindeki yer değişir.

print(ogrenciler.pop()) #sildiği veriyi gösterir

for ogrenci in ogrenciler:
    print(ogrenci)

if "Ali" in ogrenciler:
    ogrenciler.remove("Ali")
    print(ogrenciler)

