print("1=>detsimetr; 2=>kilometr; 3=>metr; 4=>millimetr; 5=>santimetr.")
l=float(input("uzunlik qiymatini kiriting: l => "))
n=int(input("[1;5] oraliqda o'lchov birligini kiriting: n => "))
if n==1:
    print(f"{l} detsimetr = {l/10} metr.")
elif n==2:
    print(f"{l} kilometr = {l*1000} metr.")
elif n==3:
    print(f"{l} metr = {l} metr.")
elif n==4:
    print(f"{l} ,millimetr = {l/1000} metr.")
elif n==5:
    print(f"{l} santimetr = {l/100} metr.")
else:
    print("Diqqatli bo'ling! [1;5] oraliqda o'lchov birligini kiriting.")