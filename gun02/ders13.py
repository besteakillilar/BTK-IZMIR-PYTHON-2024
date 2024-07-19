# temel string / karakter dizisi  işlemleri

ad = ("besteakıllılar")
print(len(ad))  # len alınan verinin kaç elemanlı olduğunu gösterir.
print(ad[0])  # isimin 0 indeksli değeri = b
print(ad[-1])  # soldan sağa doğru 0,1,2,...sağdan sola -1,-2,-3...
print(ad[-2], ad[4])
print(ad[0:5])  # ad[bas,bitiş]
print(ad[:5])
print(ad[-9:])
print(ad[:])
print(ad[::])
print(ad[::2])  # ad[bas,bitiş,artış]
print(ad[::-1])
print(ad[3:8:2])  # 3. indeksten 8e 2şer artarak
print(ad[-8:-3:2])
print("b" in ad)
print("b" in ad[::-1])
print("b" in ad[::2])
