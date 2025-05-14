print("Assalomu aleykum! ")
print('"Qolganini olamiz" o\'yiniga Xush kelibsiz!')


buyumlar=["Avtomobil", "Televizor", "Mebellar to'plami", "Telefon", "Planshet", "Klaviatura", "Komputer","Ikki xonali uy", "Elektron kitoblar to'plami", "Dazmol"]

for son in range(1, 10):
    print(f"\nOchmoqchi bo'lgan buyumingizning raqamini kiriting:\
(Siz 0 dan {10-son} gacha bo'lgan sonni tanlashingiz mumkin!!!!)")
    savol = int(input("Raqam kiriting: "))

    print(f"Siz o'yindan {buyumlar[savol]} ni chiqarib yubordingiz!")

    del buyumlar[savol]
    
    print(f"Sizda {len(buyumlar)} ta buyum qoldi: ", end=" ")
    for buyum in buyumlar:
        print(buyum, end=", ")



print(f"\nSiz yutub oldingiz : ",end="")
for m in buyumlar:
    print(m)

 #  savollar va javoblar

# nimaga range() ni ishlatdik chunki bizga 10ta qaqam kerak edi
# nimaga qavs ichiga son yozmadik chunki foydalanuvchi kiritgan son bu savol
#  nimaga end=" dan foydalandik chunki u qavsssiz qilib chiqarib beradi
#  nimaga len()dan foydalandik chunki sanab beradi 
#  nimaga \n dan foydalandik chunki u bo'lmasa ptint()dagilar end="" ga ulanib qoladi
    
    
    


















