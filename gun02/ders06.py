# otobanda 132 hız sınırını aşınca ceza alacağını belirten uygulama örneği

yol = float(input("Kaç km ilerlediğinizi giriniz."))
zaman = float(input("Kaç saat yol gittiğinizi giriniz."))
orthiz = yol / zaman
if orthiz > 132:
    print(f"{orthiz - 132} km kadar hız sınırını aştınız.")
    print("Hız sınırını aştığınız için ceza yediniz.")
else:
    print("Kurallara uyduğunuz için teşekkür ederiz.")
