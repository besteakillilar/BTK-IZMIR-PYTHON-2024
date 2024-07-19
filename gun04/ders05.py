# Şanslı 7'li

import random

def lucky_seven_game():
    print("=== Şanslı 7'li Oyununa Hoş Geldiniz ===")
    print("Bir sayı tahmini yapın (1 ile 10 arasında)")

    # Rastgele bir sayı seçelim (1 ile 10 arasında)
    lucky_number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Tahmininizi girin: "))
            if guess < 1 or guess > 10:
                print("Lütfen 1 ile 10 arasında bir sayı girin.")
                continue

            if guess == lucky_number:
                print(f"Tebrikler! {lucky_number} sayısını doğru tahmin ettiniz.")
                break
            else:
                print("Malesef, yanlış tahmin ettiniz. Tekrar deneyin.")

        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

    print("Oyun bitti. Tekrar oynamak ister misiniz? (Evet/Hayır)")
    play_again = input().strip().lower()

    if play_again == "evet" or play_again == "e":
        lucky_seven_game()
    else:
        print("Oyunu kapattınız. İyi günler!")


# Oyunu başlat
lucky_seven_game()