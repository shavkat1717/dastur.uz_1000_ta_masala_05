n=int(input("yilning istalgan oy raqamini kiriting: n => "))
q="Qish"
b="Bahor"
y="Yoz"
k="Kuz"
if n==12 or n==1 or n==2:
    print(q)
elif n==3 or n==4 or n==5:
    print(b)
elif n==6 or n==7 or n==8:
    print(y)
elif n==9 or n==10 or n==11:
    print(k)
else:
    print("Oy raqamlari soni [1;12] oraliqda bo'ladi. Diqqatli bo'ling!")