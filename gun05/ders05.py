#Localde global değişken tanımlama

def fonksiyon():
    global a
    a = 50
    def icinde():
        global b
        b = 100
    icinde()

fonksiyon()
print(a)
print(b)