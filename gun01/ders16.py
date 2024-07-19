# ESCAPE CHARACTERS

ad = input("Adınız nedir ? \t:")  # program çalıştığında kullanıcıdan giriş bekliyor
print(type(ad))
print("Memnun oldum", ad)
yas = int(input("Yaşın kaç ? \t:"))  # cevap bekliyor int çünkü kullanıcadan gelen her veri stringtir
print(type(yas))
print("Ehliyet alacak yaşta mısın ?", yas >= 18)
boy = float(input("Boyun kaç ? \t:"))
print("Maşallah")
cevap = bool(input("BTK Akademiyi sevdin mi ?\t:"))
print("bize olan sevgi durumun", cevap)
print("Geldiğin için teşekürler.")


