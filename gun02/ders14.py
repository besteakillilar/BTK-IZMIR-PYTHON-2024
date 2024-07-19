ad1 = "Mehmet"
ad2 = "Irmak"
ad3 = "Umut"
print(ad1+ad2+ad3)
print(f"{ad1}+{ad2}+{ad3}")

metin = "Merhaba sayın {} kursumuza hoş geldiniz !"
#print[f"Merhaba sayın {ad1} kursumuza hoş geldiniz !")
print(metin.format(ad1))
print(metin.format(ad2))
print(metin.format(ad3))

metin2 = "Yarışmamızın başarı sıralaması şu şekildedir :  {} {} {}"
print(metin2.format(ad1,ad2,ad3))

metin3 = "{K1},{K2} {K3}".format(K1=ad1,K2=ad2,K3=ad3)
print(metin3)