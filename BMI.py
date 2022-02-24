from tkinter import*

root=Tk()
root.geometry('1350x650+0+0')
root.resizable(0,0)
root.title('BMI')

def BMI_Cal():
    BHeight=float(var2.get())
    BWeight=float(var1.get())
    BMI=str("%.2f"%(BWeight/(BHeight*BHeight)))
    lblresult.config(text=BMI)
    
var1=DoubleVar()
var2=DoubleVar()

Tops=Frame(root,width=1350,height=50,bd=8,relief="raise")
Tops.pack(side=TOP)
f1=Frame(root,width=600,height=600,bd=8,relief="raise")
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,bd=8,relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1,width=600,height=200,bd=20,relief="raise")
f1a.pack(side=TOP)
f1b=Frame(f1,width=600,height=600,bd=20,relief="raise")
f1b.pack(side=TOP)

lblTitle=Label(Tops,text="  BODY MASS INDEX CALCULATOR  ",padx=16,pady=16,fg="#000000",font=('lucida fax',40,'bold'),bg="light green",relief="raise",width=32,height=1)
lblTitle.pack()

lblheight=Label(f1a,text="Select Weight (in kilograms)",font=('lucida fax',20,'bold'),bg="light green",bd=20).grid(row=0,column=0)
Bodyweight=Scale(f1a,variable=var1,from_=0,to=110,length=750,tickinterval=5,orient=HORIZONTAL)
Bodyweight.grid(row=2,column=0)

lblheight=Label(f1b,text='Enter Height (in metres)',font=('lucida fax',20,'bold'),bg="light green",bd=20).grid(row=0,column=0)
txtheight=Entry(f1b,textvariable=var2,font=('lucida fax',16,'bold'),bd=16,width=22,justify='center')
txtheight.grid(row=1,column=0)

lblresult=Label(f1b,padx=16,pady=1,bd=16,fg='#000000',font=('lucida fax',30,'bold'),bg='light green',relief='sunk',width=34,height=1)
lblresult.grid(row=2,column=0)

lbltable=Label(f2,font=('arial',20,'bold'),text='BMI TABLE',bg="light green").grid(row=0,column=0)
txttable=Text(f2,height=16,width=38,bd=16,font=('arial',12,'bold'))
txttable.grid(row=1,column=0)

txttable.insert(END,'Weight Status\t\t'+'BMI\n\n')
txttable.insert(END,'Underweight\t\t'+'_<18.9\n\n')
txttable.insert(END,'Normal Weight\t\t'+'19-24.9\n\n')
txttable.insert(END,'Overweight\t\t'+'25-29.9\n\n')
txttable.insert(END,'Obesity-I\t\t'+'30-34.9\n\n')
txttable.insert(END,'Obesity-II\t\t'+'35-39.9\n\n')
txttable.insert(END,'Obesity-III\t\t'+'>_40\n\n')

btnbmi=Button(f2,text='Click To \nCheck Your \nBMI',padx=8,pady=8,bd=12,width=18,font=('arial',16,'bold'),bg='light green',height=3,command=BMI_Cal)
btnbmi.grid(row=2,column=0)
root.mainloop()
               
