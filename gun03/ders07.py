#Boyutu aynı olan iki ayrı liste

kizlar = ["ayşe","hatma","hayriye"]
erkekler = ["ali","veli","can"]
liste1 = [kizlar,erkekler]

for dd in liste1:
    for kisi in dd:
        print(dd, kisi)

for kiz,erkek in zip(kizlar,erkekler): # iki listeyi karşılıklı eşleştirme
    print(kiz,erkek)
