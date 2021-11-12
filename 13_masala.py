print("\n1-Katet, 2-Gipotenuza, 3-Gip.tush.balandlik, 4-Yuza")
a=int(input("Istalgan o'lchov turini tanlang: => "))
b=float(input("Endi uning qiymatini kiriting: => "))
if a==1:
    print(f"Katet R={b} ga teng.")
    print(f"Gipotenuza c={b*(2**(1/2))} ga teng.")
    print(f"balandlik h={b*(2**(1/2))/2} ga teng.")
    print(f"yuzasi S={(b**2)/2} ga teng.")
elif a==2:
    print(f"Katet R={b/(2**(1/2))} ga teng.")
    print(f"Gipotenuza c={b} ga teng.")
    print(f"balandlik h={b/2} ga teng.")
    print(f"yuzasi S={(b**2)/4} ga teng.")
elif a==3:
    print(f"Katet R={2*b/(2**(1/2))} ga teng.")
    print(f"Gipotenuza c={2*b} ga teng.")
    print(f"balandlik h={b} ga teng.")
    print(f"yuzasi S={(b**2)} ga teng.")
elif a==4:
    print(f"Katet R={b**(1/2)*2**(1/2)} ga teng.")
    print(f"Gipotenuza c={2*(b**(1/2))} ga teng.")
    print(f"balandlik h={b**(1/2)} ga teng.")
    print(f"yuzasi S={b} ga teng.")
else: 
    print("[1;4] oraliqda kiriting...")