print("\n1-tomoni, 2-ich.chz.ayl.radiusi, 3-tash.chz.ayl.radiusi, 4-Yuza")
a=int(input("Istalgan o'lchov turini tanlang: => "))
b=float(input("Endi uning qiymatini kiriting: => "))
if a==1:
    print(f"Tomoni: a={b} ga teng.")
    print(f"Ich.chz.ayl.radiusi: r={b*(3**(1/2))/6} ga teng.")
    print(f"Tash.chz.ayl.radiusi: R={b*(3**(1/2))/3} ga teng.")
    print(f"Yuzasi: S={(b**2)*(3**(1/2))/4} ga teng.")
elif a==2:
    print(f"Tomoni: a={2*(3**(1/2))*b} ga teng.")
    print(f"Ich.chz.ayl.radiusi: r={b} ga teng.")
    print(f"Tash.chz.ayl.radiusi: R={2*b} ga teng.")
    print(f"Yuzasi: S={3*(3**(1/2))*b**2} ga teng.")
elif a==3:
    print(f"Tomoni: a={b/(3**(1/2))} ga teng.")
    print(f"Ich.chz.ayl.radiusi: r={b/2} ga teng.")
    print(f"Tash.chz.ayl.radiusi: R={b} ga teng.")
    print(f"Yuzasi: S={3**(3**(1/2))/4*b**2} ga teng.")
elif a==4:
    print(f"Tomoni: a={((4*b)/(3**(1/2)))**(1/2)} ga teng.")
    print(f"Ich.chz.ayl.radiusi: r={(b/(3*(3**(1/2))))} ga teng.")
    print(f"Tash.chz.ayl.radiusi: R={(4*b/(3*(3**(1/2))))} ga teng.")
    print(f"Yuzasi: S={b} ga teng.")
else: 
    print("[1;4] oraliqda kiriting...")