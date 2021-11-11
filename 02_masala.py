hafta_kunlari=["Yomon","Qoniqarsiz","Qoniqarli","Yaxshi","A'lo"]
n=int(input("1 dan 5 gacha son kiriting: n => "))
if 1<=n<6:
    print(hafta_kunlari[n-1])
else:
    print("Diqqatli bo'ling! 1 dan 5 gacha son kiriting...") 