# yemek sipraiş uygulaması

yemek = input("Seçtiğiniz yemeği belirtiniz :")
if yemek == "pide":
    içecek = input("Seçtiğiniz içeçeği belirtiniz :")
    if içecek == "ayran":
        print("Siparişiniz doğru!")
    else:
        print("Yemek doğru fakat içeçeğiniz yanlış.")
else:
     print("Üzgünüz, siparişiniz yanlış.")
