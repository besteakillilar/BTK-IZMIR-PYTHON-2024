#for döngüsü kaç kere çalışacak olduğu belli olan döngüdür
print(list(range(1,11)))
print(list(range(5)))
print(list(range(1,11,2)))

for dd in range(5):
    print("Merhaba")

for dd in range(0,5):
    print(dd,"Merhaba")

for harf in "beste":
    print(harf)

isim = "beste"
for harf in isim:
    print(harf)

for dilim in range(5):
    print(dilim, ". pizzanız.")

for dilim in range(1,6):
    print(dilim, ". pizzanız.")

for dilim in range(5):
    print(dilim+1, ". pizzanız.")

for dilim in range(1,6,2):
    print(dilim, ". pizzanız.")