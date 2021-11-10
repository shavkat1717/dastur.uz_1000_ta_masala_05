hafta_kunlari=["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba"]
n=int(input("1 dan 7 gacha son kiriting: n => "))
if 1<=n<8:
    print(hafta_kunlari[n-1])
else:
    print("Diqqatli bo'ling! 1 dan 7 gacha son kiriting...")