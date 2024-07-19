# Hesap makinesi programı

def topla(a, b):
    return a + b


def cikar(a, b):
    return a - b


def carp(a, b):
    return a * b


def karsilama():
    islem = input("Hesap makine programına hoşgeldiniz ! "
                  "Lütfen yapmak istediğiniz işlemi seçiniz : +, -, *")
    sayi1 = int(input("Birinci sayıyı giriniz : "))
    sayi2 = int(input("İkinci sayıyı giriniz : "))
    match islem:
        case "+":
            print(topla(sayi1, sayi2))
        case "-":
            print(cikar(sayi1, sayi2))
        case "*":
            print(carp(sayi1, sayi2))
        case _:
            print("Hatalı işlem yaptınız.")


if __name__ == "__main__":  # Programı baslatmak icin.
    karsilama()
