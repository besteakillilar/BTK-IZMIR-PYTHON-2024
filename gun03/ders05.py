# Çok boyutlu / iç içe listeler

sebze = ['domates', 'biber']
meyve = ['üzüm', 'çilek', 'kivi']
sarkuteri = ["peynir", "helva", "bal"]
yesillik = ["marul", "maydonoz", "roka"]

pazar_listesi = sebze + meyve + sarkuteri + yesillik  # extend benzeri
print(pazar_listesi)
print(len(pazar_listesi))  # 11

pazar_listesi = [sebze, meyve, sarkuteri, yesillik, "baklava"]  # iç içe liste
print(pazar_listesi)
print(len(pazar_listesi))  # 4
print(pazar_listesi[0])
print(pazar_listesi[0][0])
print(pazar_listesi[2][1])

for kategori in pazar_listesi:
    print(kategori)
    if type(kategori) == list:  # if type(kategori) != list continue

        for urun in kategori:
            print(urun)
