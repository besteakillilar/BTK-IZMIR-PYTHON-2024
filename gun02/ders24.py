cevap = input("Pizza ister misiniz ?")
while cevap == "evet":
    print("Afiyet olsun")
    cevap = input("Bir pizza daha ister misiniz ?")
    if cevap == "hayır":
        print("Afiyet olsun ! Bizi tercih ettiğin için teşekkür ederiz.")