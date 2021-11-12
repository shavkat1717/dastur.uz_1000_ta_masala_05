onliklar=["O'n","Yigirma","O'ttiz","Qirq"]
birliklar=["bir","ikki","uch","to'rt","besh","olti","yetti","sakkiz","to'qqiz"]
x=int(input("[10;40] oraliqda istalgan masala nomerini kiriting: => "))
import math
a=math.floor(x/10)
q=x-a*10
if x>=10 and x<=40:
    if x%10!=0:
        print(f"{onliklar[a-1]} {birliklar[q-1]}ta masala.")
    else:
        print(f"{onliklar[a-1]}ta masala.")
else:
    print("Diqqatli bo'ling! Belgilangan [10;40] oraliqqa amal qiling!")