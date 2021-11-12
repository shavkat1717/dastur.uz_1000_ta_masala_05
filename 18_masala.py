yuzliklar=["yuz"]
onliklar=["o'n","yigirma","o'ttiz","qirq","ellik","oltmish","yetmish","sakson","to'qson"]
birliklar=["bir","ikki","uch","to'rt","besh","olti","yetti","sakkiz","to'qqiz"]
x=int(input("[100;999] oraliqda istalgan butun son kiriting: => "))
import math
a=math.floor(x/100)
b=x-a*100
c=math.floor(b/10)
d=b-c*10
if x>=100 and x<1000:
    if x%100!=0 and b%10!=0 and b<10:
        print(f"{birliklar[a-1]} {yuzliklar[a-a]} {birliklar[d-1]}.")
    elif x%100!=0 and b%10!=0 and b>10:
        print(f"{birliklar[a-1]} {yuzliklar[a-a]} {onliklar[c-1]} {birliklar[d-1]}.")
    elif x%100!=0 and b%10==0:
        print(f"{birliklar[a-1]} {yuzliklar[a-a]} {onliklar[c-1]}.")
    else:
        print(f"{birliklar[a-1]} {yuzliklar[a-a]}.")
else:
    print("Diqqatli bo'ling! Belgilangan [100;999] oraliqqa amal qiling!")