hafta_kunlari=["Yanvar","Fevral","Mart","Aprel","May","Iyun","Iyul","Avgust","Sentyabr","Oktyabr","Noyabr","Dekabr"]
d=int(input("sanani kiriting: D => "))
m=int(input("[1;12] oraliqda oy raqamini kiriting: M => "))
if 1<=d<=31 and 1<=m<13:
    print(d, hafta_kunlari[m-1])
else:
    print("Diqqatli bo'ling! kun yoki oy raqami belgilangan oraliqda emas.")