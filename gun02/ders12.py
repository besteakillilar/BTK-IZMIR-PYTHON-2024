# gün değerine göre haftanın gün sayısı

gun = input("Gün değerini giriniz: ")
match gun:
    case "Pazartesi":
        print("Birinci gün.")
    case "Salı":
        print("İkinci gün.")
    case "Çarşamba":
        print("Üçüncü gün.")
    case "Perşembe":
        print("Dördüncü gün.")
    case "Cuma":
        print("Beşinci gün.")
    case _:
        print("Tanımsız gün girdiniz !")

 #######################################

gun = int(input("Gün değerini giriniz: "))
match gun:
    case 1:
        print("Pazartesi.")
    case 2:
        print("Salı.")
    case 3:
        print("Çarşamba.")
    case 4:
        print("Perşembe.")
    case 5:
        print("Cuma.")
    case _:
        print("Tanımsız gün girdiniz !")