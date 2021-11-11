a=float(input("A haqiqiy sonni kiriting: A => "))
b=float(input("B haqiqiy sonni kiriting: B => "))
n=int(input("[1;4] oraliqda amal butun sonini kiriting: n => "))
if n==1:
    print(f"{a} + {b} = {a+b}")
elif n==2:
    print(f"{a} - {b} = {a-b}")
elif b==0 and n==3:
    print("Nolga bo'lish mumkin emas.")
elif n==3:
    print(f"{a} / {b} = {a/b}")
elif n==4:
    print(f"{a} * {b} = {a*b}")
else:
    print("Diqqatli bo'ling! amal butun sonini [1;4] oraliqda kiriting.")