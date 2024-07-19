# Karne alma uygulaması

puan = int(input("Karne notunuzu giriniz: "))
if puan < 70:
    print("Belge alamazsınız.")
elif puan < 85:  # else + if = alif
    print("Tebrikler teşekkür almaya hak kazandınız.")
elif puan <= 100:
    print("Tebrikler takdir almaya hak kazandınız.")
else:
    print("Geçerli bir not girmediniz.")
