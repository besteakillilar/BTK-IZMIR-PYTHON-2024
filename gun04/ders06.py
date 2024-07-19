# PYTHON TIME

import time

print("Hello World")
time.sleep(5)
print("Goodbye World")

# PYTHON DATE TIME

import datetime  # from datetime import datetime

a = input("Birinci Giriş : ")
giris = datetime.datetime.now()
print(giris)
b = input("İkinci Giriş :")
giris2 = datetime.datetime.now()
fark = giris2 - giris
print(fark)
print(fark.total_seconds())
