# PYTHON SCOPE & NAMESPACE

a = 1


def ustFonksiyon():
    print(a)
    b = 2

    def altFonksiyon():
        print(a)
        print(b)
        c = 3

        altFonksiyon()
        # print(c)

ustFonksiyon()
#print(b)