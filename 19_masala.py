rang=["yashil","qizil","sariq","oq","qora"]
hayvonlar=["sichqon","sigir","yo'lbars","quyon","ajdar","ilon","ot","qo'y","maymun","tovuq","it","to'ng'iz"]
x=int(input("Istalgan milodiy yil kiriting: => "))
a=x%5
b=x%12
if x>0:
    print(f"{x}-yil {rang[a-1]} {hayvonlar[b-1]} yili.")
else:
    print("Diqqatli bo'ling! Kiritilgan yil belgilangan oraliqda emas!")