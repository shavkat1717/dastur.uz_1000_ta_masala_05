onliklar=["Yigirma","O'ttiz","Qirq","Ellik","Oltmish"]
birliklar=["bir","ikki","uch","to'rt","besh","olti","yetti","sakkiz","to'qqiz"]
x=int(input("[20;69] oraliqda istalgan yoshni kiriting: => "))
import math
a=math.floor(x/10)
q=x-a*10
if x>=20 and x<70:
    if x%10!=0:
        print(f"{onliklar[a-2]} {birliklar[q-1]}")
    else:
        print(f"{onliklar[a-2]}")
else:
    print("Belgilangan [20;69] oraliqda yosh kiriting!")