carpim = 1
while True:
    sayi = int(input("Bir sayı giriniz"))
    if sayi == 0:
        print("Girilen sayıların çarpımı ", carpim)
        break
    carpim *= sayi


