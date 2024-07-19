# Karne alma uygulaması

puan = int(input("Karne notunuzu giriniz: "))
if puan < 70:
    print("Belge alamazsınız.")
else:
    if puan < 85:
        print("Tebrikler teşekkür almaya hak kazandınız.")
    else:
        if puan <= 100:
            print("Tebrikler takdir almaya hak kazandınız.")
        else:
            print("Geçerli bir not girmediniz.")
