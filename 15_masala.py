qiymat=["Olti","Yetti","Sakkiz","To'qqiz","O'n","Valet","Dama","Karol","Tuz"]
tur=["kirpich","tappon","chillik","qarg'a"]
x=int(input("[6;14] oraliqda karta qiymatini tanlang: => "))
y=int(input("[1;4] oraliqda karta turini tanlang: => "))
if 6<=x<=14 and 1<=y<=4:
    print(f"{qiymat[x-6]} {tur[y-1]}")
else:
    print("Qiymat va turni belgilangan oraliqda kiriting!")