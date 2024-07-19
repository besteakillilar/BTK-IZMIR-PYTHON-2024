# Python Tuples
#listten farklı olarak değiştirilemez
demet = (24,8,2.5,True)
print(demet)
print(type(demet))
print(demet.index(2.5))
print(demet.count(2.5))
for eleman in demet:
    print(eleman)

#değiştirilemz fakat demeti listeye çevirip işlem yapılabilir.
dlist = list(demet)
dlist[1] = "AAA"
demet = tuple(dlist)
print(demet)


demet1 = (24,8,2.5,True,"beste",["beste","akıllılar"])
print(demet1)

pazar = ["elma","armut","salatalık"]
pazarDemeti = tuple(pazar)
print(pazarDemeti)
print(pazarDemeti[0])
print(pazarDemeti[::-1]) # terten yazıyor


