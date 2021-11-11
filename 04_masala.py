n=int(input("yilning istalgan oy raqamini kiriting: n => "))
if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("Ushbu oyda 31 kun bor.")
elif n==4 or n==6 or n==9 or n==11:
    print("Ushbu oyda 30 kun bor.")
elif n==2:
    print("Ushbu oyda 28 kun bor.")
else:
    print("Diqqatli bo'ling! Oy raqamlari [1;12] oralig'ida yotadi.")