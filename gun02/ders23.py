# while döngüsü koşul geçerli olduğu sürece tekrar eder

adet = int(input("Kaç dilim pizza istersiniz ?"))
dilim = adet
# yöntem1
while adet > 0:
    print("Pizzanız hazır, afiyet olsun !")
    adet -= 1
# yöntem2
i = 1
while dilim >= i:
    print(i, ".pizzanız hazır, afiyet olsun !")
    i += 1
