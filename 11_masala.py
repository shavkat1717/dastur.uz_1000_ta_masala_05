print("\n1-shimol, 2-janub, 3-sharq, 4-g'arb")
x=int(input("Lokator yuzlanib turgan yo'nalishini tanlang: => "))
# 1-shimol, 2-janub, 3-sharq, 4-g'arb
tomon=["shimol","janub","sharq","g'arb"]
print("\n0-o'ngga, 1-chapga, 2-orqaga")
K1=int(input("1-Harakat komandasini tanlang: => "))
K2=int(input("2-Harakat komandasini tanlang: => "))
# 0-o'ngga, 1-chapga, 2-orqaga

# Shimol tomon uchun:
    
if x==1 and K1==0 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==1 and K1==0 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[0]} tomon.")
elif x==1 and K1==0 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[3]} tomon.")
elif x==1 and K1==1 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[0]} tomon.")
elif x==1 and K1==1 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==1 and K1==1 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==1 and K1==2 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[3]} tomon.")
elif x==1 and K1==2 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==1 and K1==2 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[0]} tomon.")

# Sharq tomon uchun:

elif x==3 and K1==0 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[3]} tomon.")
elif x==3 and K1==0 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==3 and K1==0 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[0]} tomon.")
elif x==3 and K1==1 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==3 and K1==1 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[3]} tomon.")
elif x==3 and K1==1 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==3 and K1==2 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[0]} tomon.")
elif x==3 and K1==2 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==3 and K1==2 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[2]} tomon.")

# G'arb tomon uchun:

elif x==4 and K1==0 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==4 and K1==0 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[3]} tomon.")
elif x==4 and K1==0 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==4 and K1==1 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[3]} tomon.")
elif x==4 and K1==1 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==4 and K1==1 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[0]} tomon.")
elif x==4 and K1==2 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==4 and K1==2 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[0]} tomon.")
elif x==4 and K1==2 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[3]} tomon.")

# Janub tomon uchun:

elif x==2 and K1==0 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[0]} tomon.")
elif x==2 and K1==0 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==2 and K1==0 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==2 and K1==1 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==2 and K1==1 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[0]} tomon.")
elif x==2 and K1==1 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[3]} tomon.")
elif x==2 and K1==2 and K2==0:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==2 and K1==2 and K2==1:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[3]} tomon.")
elif x==2 and K1==2 and K2==2:
    print(f"Harakatdan keyingi lokatorning yuzlanib qolgan holati: {tomon[1]} tomon.")
else:
    print("Diqqatli bo'ling! Berilgan oraliqqa e'tibor qarating.")
