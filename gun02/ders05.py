# kullanıcıdan doğum yılını alıp ehliyet alıp alamayacağına bakalım.

yil = int(input("Doğum yılınızı giriniz :"))
yas = 2024 - yil
if yas < 18:
    print("Ehliyet alamazsın.")
    print(f"Ehliyet alamazsın,{yas} yaşındasınız.")
    print(f"{18-yas} yıl kadar daha beklemeniz gerekmektedir.")  #f string kullanımı

else:
    print("Ehliyet alabilirsin.")
