print("\n1-Radius, 2-Diametr, 3-Uzunlik, 4-Yuza")
a=int(input("Istalgan o'lchov turini tanlang: => "))
b=float(input("Endi uning qiymatini kiriting: => "))
pi=3.14159
if a==1:
    print(f"Doiraning radiusi R={b} ga teng.")
    print(f"Doiraning diametri D={b*2} ga teng.")
    print(f"Doiraning uzunligi L={2*pi*b} ga teng.")
    print(f"Doiraning yuzasi S={pi*(b**2)} ga teng.")
elif a==2:
    print(f"Doiraning radiusi R={b/2} ga teng.")
    print(f"Doiraning diametri D={b} ga teng.")
    print(f"Doiraning uzunligi L={pi*b} ga teng.")
    print(f"Doiraning yuzasi S={pi*(b**2)/4} ga teng.")
elif a==3:
    print(f"Doiraning radiusi R={b/(2*pi)} ga teng.")
    print(f"Doiraning diametri D={b/pi} ga teng.")
    print(f"Doiraning uzunligi L={b} ga teng.")
    print(f"Doiraning yuzasi S={(b**2)/4*pi} ga teng.")
elif a==4:
    print(f"Doiraning radiusi R={(b/pi)**(1/2)} ga teng.")
    print(f"Doiraning diametri D={2*((b/pi)**(1/2))} ga teng.")
    print(f"Doiraning uzunligi L={2*((b*pi)**(1/2))} ga teng.")
    print(f"Doiraning yuzasi S={b} ga teng.")
else: 
    print("[1;4] oraliqda kiriting...")