# SAYI TAHMİN OYUNU

# Vers.1
sayi = 35
tahmin = int(input("Lütfen bir sayı giriniz: "))
if tahmin == sayi:
    print("Tahmin Başarılı !")
else:
    print("Tahmin Başarısız.")

# Vers.2
sayi = 35
tahmin = int(input("Lütfen bir sayı giriniz: "))
if tahmin == sayi:
    print("Tahmin Başarılı !")
elif tahmin > sayi:
    print("Tahmin Başarısız :( keşke küçük bir sayı girseydiniz.")
elif tahmin < sayi:
    print("Tahmin Başarısız :( keşke büyük bir sayı girseydiniz.")

# Vers.3
sayi = 35
taban = 0
tavan = 100
print(f"Tahmin edeceğiniz sayı {taban}- {tavan} aralığındadir.")
tahmin = int(input("Lütfen bir sayı giriniz: "))
while True:
    if taban <= tahmin <= tavan:
        print(f"Tahmin geçerli aralıktadır.")
        break
    else:
        print(f"Tahmin aralık dışındadır.")
        print(f"Tahmin edeceğiniz sayı {taban}- {tavan} aralığındadir.")
        tahmin = int(input("Lütfen bir sayı giriniz: "))
if tahmin == sayi:
    print("Tahmin Başarılı !")
elif tahmin > sayi:
    print("Tahmin Başarısız :( keşke küçük bir sayı girseydiniz.")
elif tahmin < sayi:
    print("Tahmin Başarısız :( keşke büyük bir sayı girseydiniz.")

# Vers.4
sayi = 35
taban = 0
tavan = 100
print(f"Tahmin edeceğiniz sayı {taban}- {tavan} aralığındadir.")
tahmin = int(input("Lütfen bir sayı giriniz: "))
while True:
    if taban <= tahmin <= tavan:
        print(f"Tahmin geçerli aralıktadır.")
        break
    else:
        print(f"Tahmin aralık dışındadır.")
        print(f"Tahmin edeceğiniz sayı {taban}- {tavan} aralığındadir.")
        tahmin = int(input("Lütfen bir sayı giriniz: "))
while True:
    if tahmin == sayi:
        print("Tahmin Başarılı !")
        break
    elif tahmin > sayi:
        print("Tahmin Başarısız :( keşke küçük bir sayı girseydiniz.")
    elif tahmin < sayi:
        print("Tahmin Başarısız :( keşke büyük bir sayı girseydiniz.")
        print(f"Tahmin edeceğiniz sayı {taban}- {tavan} aralığındadir.")
        tahmin = int(input("Lütfen yeni bir sayı giriniz: "))

# Vers.5
sayi = 35
taban = 0
tavan = 100
print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
tahmin = int(input("Bir sayı giriniz"))
while True:
    if taban <= tahmin <= tavan:
        print(f"Tahmin geçerli aralıkta")
        break
    else:
        print(f"Tahmin aralığı dışında geçersiz tahmin")
        print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
        tahmin = int(input("Bir sayı giriniz"))
while tahmin != sayi:
    if tahmin > sayi:
        print("Tahmin Başarısız Keşke küçük bir sayı söyleseydin")
        tavan = tahmin
    elif tahmin < sayi:
        print("Tahmin Başarısız Keşke büyük bir sayı söyleseydin")
        taban = tahmin
    while True:
        if taban < tahmin < tavan:
            print(f"Tahmin geçerli aralıkta")
            break
        else:
            print(f"Tahmin aralığı dışında geçersiz tahmin")
            print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
            tahmin = int(input("Bir sayı giriniz"))
else:
    print("Tahmin Başarılı tebrikler")

# Vers.6
sayi = 35
taban = 0
tavan = 100
gecerli = []
gecersiz = []
tahminler = {"gecerli": gecerli, "gecersiz": gecersiz}
print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
tahmin = int(input("Bir sayı giriniz"))
while True:
    if taban <= tahmin <= tavan:
        print(f"Tahmin geçerli aralıkta")
        gecerli.append(tahmin)
        break
    else:
        print(f"Tahmin aralığı dışında geçersiz tahmin")
        print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
        gecersiz.append(tahmin)
        tahmin = int(input("Bir sayı giriniz"))
while tahmin != sayi:
    if tahmin > sayi:
        print("Tahmin Başarısız Keşke küçük bir sayı söyleseydin")
        tavan = tahmin
    elif tahmin < sayi:
        print("Tahmin Başarısız Keşke büyük bir sayı söyleseydin")
        taban = tahmin
    while True:
        if taban < tahmin < tavan:
            print(f"Tahmin geçerli aralıkta")
            gecerli.append(tahmin)
            break
        else:
            print(f"Tahmin aralığı dışında geçersiz tahmin")
            print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
            gecersiz.append(tahmin)
            tahmin = int(input("Bir sayı giriniz"))
else:
    print("Tahmin Başarılı tebrikler")
print(tahminler)
print(len(gecerli + gecersiz), " kerede bildiniz")
