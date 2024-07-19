# Bir birini çağıran fonksiyonlar

def birinci():
    print("Birinci fonksiyon calıstı")
    return ikinci()


def ikinci():
    print("Ikinci fonksiyon calıstı")
    return ucuncu()


def ucuncu():
    print("Ucuncu fonksiyon")
    return 3


if __name__ == '__main__':
    print("Hello world")
    a = birinci()
    print(a)
