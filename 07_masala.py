print("1=>kilogramm; 2=>milligramm; 3=>gramm; 4=>tonna; 5=>sentner.")
m=float(input("og'irlik qiymatini kiriting: m => "))
n=int(input("[1;5] oraliqda o'lchov birligini kiriting: n => "))
if n==1:
    print(f"{m} kilogramm = {m} kilogramm.")
elif n==2:
    print(f"{m} milligramm = {m/1000000} kilogramm.")
elif n==3:
    print(f"{m} gramm = {m/1000} kilogramm.")
elif n==4:
    print(f"{m} tonna = {m*1000} kilogramm.")
elif n==5:
    print(f"{m} sentner = {m*100} kilogramm.")
else:
    print("Diqqatli bo'ling! [1;5] oraliqda o'lchov birligini kiriting.")