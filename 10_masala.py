print("\n1-shimol, 2-janub, 3-sharq, 4-g'arb")
x=int(input("Robot yuzlanib turgan yo'nalishini tanlang: => "))
# 1-shimol, 2-janub, 3-sharq, 4-g'arb
tomon=["shimol","janub","sharq","g'arb"]
print("\n0-to'g'riga, 1-chapga, 2-o'ngga")
y=int(input("Harakat komandasini tanlang: => "))
# 0-to'g'riga, 1-chapga, 2-o'ngga
if x==1 and y==0:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[0]} tomon.")
elif x==1 and y==1:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[3]} tomon.")
elif x==1 and y==2:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==2 and y==0:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==2 and y==1:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==2 and y==2:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[3]} tomon.")
    
elif x==3 and y==0:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[2]} tomon.")
elif x==3 and y==1:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[0]} tomon.")
elif x==3 and y==2:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==4 and y==0:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[3]} tomon.")
elif x==4 and y==1:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[1]} tomon.")
elif x==4 and y==2:
    print(f"Harakatdan keyingi robotning yuzlanib qolgan holati: {tomon[0]} tomon.")
else:
    print("diqqatli bo'ling! Belgilangan oraliqda son kiriting.")