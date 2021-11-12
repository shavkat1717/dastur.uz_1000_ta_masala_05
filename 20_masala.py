s=int(input("Sanani kiriting: => "))
o=int(input("Oyni kiriting: => "))
if 1<=s<=31 and 1<=o<=12:
    if (s>=20 and o==1) or (1<=s<=18 and o==2) :
        print("Sizning burjingiz: Qovg'a!")
    elif (19<=s<=28 and o==2) or (1<=s<=20 and o==3):
        print("Sizning burjingiz: Baliq!")
    elif (29<=s<=31 and o==2):
        print("Fevral oyi 28-sanadan qaytadi...")
    elif (21<=s<=31 and o==3) or (1<=s<=19 and o==4):
        print("Sizning burjingiz: Qo'y!")
    elif (20<=s<=30 and o==4) or (1<=s<=20 and o==5):
        print("Sizning burjingiz: Buzoq!")
    elif (s==31 and o==4):
        print("Aprel oyi 30-sanadan qaytadi...")
    elif (21<=s<=31 and o==5) or (1<=s<=21 and o==6):
        print("Sizning burjingiz: Egizaklar!")
    elif (22<=s<=30 and o==6) or (1<=s<=22 and o==7):
        print("Sizning burjingiz: Qisqichbaqa!")
    elif (s==31 and o==6):
        print("Iyun oyi 30-sanadan qaytadi...")
    elif (23<=s<=31 and o==7) or (1<=s<=22 and o==8):
        print("Sizning burjingiz: Arslon!")
    elif (23<=s<=31 and o==8) or (1<=s<=22 and o==9):
        print("Sizning burjingiz: Parizod!")
    elif (23<=s<=30 and o==9) or (1<=s<=22 and o==10):
        print("Sizning burjingiz: Tarozi!")
    elif (s==31 and o==9):
        print("Sentyabr oyi 30-sanadan qaytadi...")
    elif (23<=s<=31 and o==10) or (1<=s<=22 and o==11):
        print("Sizning burjingiz: Chayon!")
    elif (23<=s<=30 and o==11) or (1<=s<=21 and o==12):
        print("Sizning burjingiz: O'qotar!")
    elif (s==31 and o==11):
        print("Noyabr oyi 30-sanadan qaytadi...")
    elif (22<=s<=31 and o==12) or (1<=s<=19 and o==1):
        print("Sizning burjingiz: Echki!")
else:
    print("Sana yoki oyni kiritishda xatolikka yo'l qo'ydingiz!")