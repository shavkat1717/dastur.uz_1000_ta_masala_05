hafta_kunlari=["Yanvar","Fevral","Mart","Aprel","May","Iyun","Iyul","Avgust","Sentyabr","Oktyabr","Noyabr","Dekabr"]
d=int(input("[1;31] oraliqda sanani kiriting: D => "))
m=int(input("[1;12] oraliqda oy raqamini kiriting: M => "))
while 1<=d<=31 and 1<=m<13:
    if d==31 and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10):
        print(d,"-", hafta_kunlari[m-1],"dan keyingi sana:","1-", hafta_kunlari[m])
        break
    elif d==30 and (m==4 or m==6 or m==9 or m==11):
        print(d,"-", hafta_kunlari[m-1],"dan keyingi sana:","1-", hafta_kunlari[m])
        break
    elif d==28 and m==2:
        print(d,"-", hafta_kunlari[m-1],"dan keyingi sana:","1-", hafta_kunlari[m])
        break
    elif (d==29 or d==30 or d==31) and m==2:
        print(f"Kechirasiz! {hafta_kunlari[m-1]} oyi 28-dan qaytadi.")
        break
    elif d==31 and m==12:
        print(d,"-", hafta_kunlari[m-1],"dan keyingi sana:","1-", hafta_kunlari[m-12])
        break
    elif d==31  and (m==4 or m==6 or m==9 or m==11):
        print(f"Kechirasiz {hafta_kunlari[m-1]} oyi 30-sanadan qaytadi.")
        break
    else:
        print(d,"-", hafta_kunlari[m-1],"dan keyingi sana:",d+1,"-", hafta_kunlari[m-1])
        break
else:
    print("Diqqatli bo'ling! kun yoki oy raqami belgilangan oraliqda emas.")