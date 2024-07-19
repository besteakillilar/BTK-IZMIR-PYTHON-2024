####

print("Adınız nedir ?")
ad = input()  # program çalıştığında kullanıcıdan giriş bekliyor
print(type(ad))
print("Memnun oldum", ad)
print("Yaşın kaç ?")
yas = int(input())  # cevap bekliyor int çünkü kullanıcadan gelen her veri stringtir
print(type(yas))
print("Ehliyet alacak yaşta mısın ?", yas >= 18)
print("Boyun kaç ?")
boy = float(input())
print("Maşallah")
print("BTK Akademiyi sevdin mi ?")
cevap = bool(input())
print("bize olan sevgi durumun", cevap)
print("Geldiğin için teşekürler.")
