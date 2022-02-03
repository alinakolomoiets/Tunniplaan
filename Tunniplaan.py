from tkinter import *
from tkinter.font import *
from tkinter.messagebox import *

def failist_sonastikusse():
    tund_kirjeldus={}
    file=open("TextFile1.txt","r")
    for line in file:
        tund,kirjeldus=line.strip().split(":")
        tund_kirjeldus[tund.strip()]=kirjeldus.strip()
    file.close()
    print(tund_kirjeldus)
    return tund_kirjeldus

tund_kirjeldus=failist_sonastikusse()
def kirjeldus_aknasse(t:str,tit:str):
    if (askyesno("Kusimus","Kas tahad kirjeldust naha?")):
        alam_aken=Toplevel()
        alam_aken.title(tit)
        lbl_kirjeldus=Label(alam_aken,text=tund_kirjeldus[t]).pack()
        c=Canvas(alam_aken,height=700,width=700)
        file=PhotoImage(file=t)
        c.create_image(10,10,image=file,anchor=NW)
        c.pack()
        alam_aken.mainloop()
    else:
        showinfo("Vastus","Kui ei taha, siis ei taha!!!")

aken=Tk()
aken.title("Tunniplaan")
aken.geometry("1920x1080")
p=["Esmaspaev","Teisipaev","Kolmapaev","Neljapaev","Reede"]
j=0
for i in range(1,10,2):
    paev=Label(aken, text=p[j],relief="solid",font="Calibri 20").grid(row=i, column=0, rowspan=2, sticky=N+S+W+E)
    j+=1
kell=["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]
for i in range(11):
    tund="t"+str(i)
    tund=tund1=Label(aken, text=str(i)+"\n"+kell[i], relief="solid",font="Calibri 15").grid(row=0, column=i+1, sticky=N+S+W+E)

##Tunnid
#t0=Label(text="0",relief="solid",width=10,height=5).grid(row=0,column=1,sticky=N+S+W+E)
#t1=Label(text="1",relief="solid",width=10,height=5).grid(row=0,column=2,sticky=N+S+W+E)
#t2=Label(text="2",relief="solid",width=10,height=5).grid(row=0,column=3,sticky=N+S+W+E)
#t3=Label(text="3",relief="solid",width=10,height=5).grid(row=0,column=4,sticky=N+S+W+E)
#t4=Label(text="4",relief="solid",width=10,height=5).grid(row=0,column=5,sticky=N+S+W+E)
#t5=Label(text="5",relief="solid",width=10,height=5).grid(row=0,column=6,sticky=N+S+W+E)
#t6=Label(text="6",relief="solid",width=10,height=5).grid(row=0,column=7,sticky=N+S+W+E)
#t7=Label(text="7",relief="solid",width=10,height=5).grid(row=0,column=8,sticky=N+S+W+E)
#t8=Label(text="8",relief="solid",width=10,height=5).grid(row=0,column=9,sticky=N+S+W+E)
#t9=Label(text="9",relief="solid",width=10,height=5).grid(row=0,column=10,sticky=N+S+W+E)
#t10=Label(text="10",relief="solid",width=10,height=5).grid(row=0,column=11,sticky=N+S+W+E)

##Paevad
#Ep=Label(aken,text="Esmaspaev",relief="solid",height=7).grid(row=1,column=0,rowspan=2,sticky=N+S+W+E)
#Tp=Label(aken,text="Teisipaev",relief="solid",height=7).grid(row=3,column=0,rowspan=2,sticky=N+S+W+E)
#Kl=Label(aken,text="Kolmapaev",relief="solid",height=7).grid(row=5,column=0,rowspan=2,sticky=N+S+W+E)
#Nl=Label(aken,text="Neljapaev",relief="solid",height=7).grid(row=7,column=0,rowspan=2,sticky=N+S+W+E)
#Rd=Label(aken,text="Reede",relief="solid",height=7).grid(row=9,column=0,rowspan=2,sticky=N+S+W+E)

#Esmaspäev
p1=Button(text="Multimeedia Grupp1", font="Calibri 26",bg="cornflowerblue",command=lambda:kirjeldus_aknasse("mu.png","Multimeedia")).grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
p3=Button(text="Programmeerimise alused Grupp2", font="Calibri 26",bg="skyblue",command=lambda:kirjeldus_aknasse("image-7.png","Programmeerimise alused ")).grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
p4=Button(text="Programmeerimise alused Grupp1", font="Calibri 26",bg="skyblue",command=lambda:kirjeldus_aknasse("image-7.png","Programmeerimise alused")).grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
p5=Button(text="Multimeedia Grupp2", font="Calibri 26",bg="cornflowerblue",command=lambda:kirjeldus_aknasse("mu.png","Multimeedia")).grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
p27=Button(text="Rühma juhatuja tund", font="Calibri 26",bg="skyblue",command=lambda:kirjeldus_aknasse("bunda.png","Ruhmajuhatajatund")).grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)

#Teisipäev
p6=Button(text="Inglise keel Grupp1", font="Calibri 26",bg="floralwhite",command=lambda:kirjeldus_aknasse("pip.png","Inglise keel Grupp 1")).grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
p7=Button(text="Inglise keel Grupp2", font="Calibri 26",bg="mediumorchid",command=lambda:kirjeldus_aknasse("pip.png","Inglise keel Grupp 2")).grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
p8=Button(text="Operatsioonisüsteemide alused", font="Calibri 26",bg="darkorchid",command=lambda:kirjeldus_aknasse("kkk.png","Operatsioonisusteemide alused")).grid(row=3,column=4,columnspan=2,rowspan=2,sticky=N+S+W+E)
p10=Button(text="Kehaline kasvatus", font="Calibri 26",bg="palevioletred",command=lambda:kirjeldus_aknasse("kuki.png","Kehaline kasvatus")).grid(row=3,column=7,columnspan=2,rowspan=2,sticky=N+S+W+E)
p11=Button(text="Eesti keel Grupp1", font="Calibri 26",bg="mediumpurple",command=lambda:kirjeldus_aknasse("big.png","Eesti keel Grupp 1")).grid(row=3,column=9,sticky=N+S+W+E)
p12=Button(text="Eesti keel Grupp2", font="Calibri 26",bg="darkgrey",command=lambda:kirjeldus_aknasse("big.png","Eesti keel Grupp 2")).grid(row=4,column=9,sticky=N+S+W+E)
p13=Button(text="Ajalugu", font="Calibri 26",bg="khaki",command=lambda:kirjeldus_aknasse("mimi.png","Ajalugu, inimgeograafia")).grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)

#Kolmapäev
p14=Button(text="Programmeerimise alused Grupp1", font="Calibri 26",bg="skyblue",command=lambda:kirjeldus_aknasse("image-7.png","Programmeerimise alused ")).grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
p15=Button(text="Multimeedia Grupp2", font="Calibri 26",bg="cornflowerblue",command=lambda:kirjeldus_aknasse("mu.png","Multimeedia")).grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
p16=Button(text="Multimeedia Grupp1", font="Calibri 26",bg="cornflowerblue",command=lambda:kirjeldus_aknasse("mu.png","Multimeedia")).grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
p17=Button(text="Programmeerimise alused Grupp2", font="Calibri 26",bg="skyblue",command=lambda:kirjeldus_aknasse("image-7.png","Programmeerimise alused ")).grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
p18=Button(text="Kunstiained", font="Calibri 26",bg="orchid",command=lambda:kirjeldus_aknasse("bu.png","Kunstiained")).grid(row=5,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)

#Neljapäev
p19=Button(text="Andmebaasisüsteemide alused", font="Calibri 26",bg="salmon",command=lambda:kirjeldus_aknasse("puk.png","Andmebaasisusteemide alused")).grid(row=7,column=2,columnspan=5,rowspan=2,sticky=N+S+W+E)
p20=Button(text="Ajalugu", font="Calibri 26",bg="khaki",command=lambda:kirjeldus_aknasse("mimi.png","Ajalugu, inimgeograafia")).grid(row=7,column=6,rowspan=2,sticky=N+S+W+E)
p21=Button(text="Eesti keel Grupp1", font="Calibri 26",bg="mediumpurple",command=lambda:kirjeldus_aknasse("big.png","Eesti keel Grupp 1")).grid(row=7,column=7,sticky=N+S+W+E)
p22=Button(text="Eesti keel Grupp2", font="Calibri 26",bg="darkgrey",command=lambda:kirjeldus_aknasse("big.png","Eesti keel Grupp 2")).grid(row=8,column=7,sticky=N+S+W+E)

#Reede
p23=Button(text="Vene keel", font="Calibri 26",bg="greenyellow",command=lambda:kirjeldus_aknasse("eel.png","Keel ja kirjandus")).grid(row=9,column=3,columnspan=2,rowspan=2,sticky=N+S+W+E)
p24=Button(text="Matemaatika", font="Calibri 26",bg="lightpink",command=lambda:kirjeldus_aknasse("mmm.png","Matemaatika")).grid(row=9,column=6,columnspan=2,rowspan=2,sticky=N+S+W+E)
p25=Button(text="Suhtlemine ja kliienditeenindus", font="Calibri 26",bg="mediumslateblue",command=lambda:kirjeldus_aknasse("bubu.png","Suhtlemine ja klienditeenindus")).grid(row=9,column=8,columnspan=2,rowspan=2,sticky=N+S+W+E)
p26=Button(text="Ajalugu", font="Calibri 26",bg="khaki",command=lambda:kirjeldus_aknasse("mimi.png","Ajalugu, inimgeograafia")).grid(row=9,column=10,rowspan=2,sticky=N+S+W+E)

aken.mainloop()
