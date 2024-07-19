# Python DICTIONARY

treng = {"araba":"car","kalem":"pencil","cam":"glass" }
print(treng)
print(treng.keys())
print(treng.values())
print(treng.items()) #veriyi tuple olarak verdi
print(treng.get("araba"))  #print(treng["araba"])

for k in treng:
    print(k, end="\t")
    print(treng[k])

for key,value in treng.items():
    print(key, value, sep="=")

for dd in treng:
    print(dd,treng[dd])
    print(dd, "*",treng.get(dd))