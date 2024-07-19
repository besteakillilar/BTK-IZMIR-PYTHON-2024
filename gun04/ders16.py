# Default parametreli fonksiyonlar

def kare(a):
    return a * a


print(kare(10))


#######
def kare2(a=5):
    return a * a


print(kare2())


########################################3

def daireAlan(r, pi):
    alan = pi * r * r
    return alan


print(daireAlan(6, 2))


######
def daireAlan2(r, pi=3.14):  # Eğer senin değer verdiğin varsa solda, kullanıcıdan alman gerekenler sağda olmalı.
    alan = pi * r * r
    return alan


print(daireAlan2(1))
