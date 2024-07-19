# iç içe döngü kullanımı

sebze = ['domates', 'biber']
meyve = ['üzüm', 'çilek', 'kivi']
sarkuteri = ["peynir", "helva", "bal"]
yesillik = ["marul", "maydonoz", "roka"]

pazar_listesi = [sebze, meyve, sarkuteri, yesillik, "baklava"]  # iç içe liste

for x in range(len(pazar_listesi)):
    print(pazar_listesi[x])

for x in range(len(pazar_listesi)):
    print(x+1, ".kategorisi:",pazar_listesi[x])

for index, urun in enumerate(pazar_listesi[x]):
    print(index + 1, urun)
