from tkinter import *
import random
import time

root = Tk()
root.title("TMP")
root.configure(background='coral')
text_Input = StringVar()
operator = ""

Tops = Frame(root, width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

rand = StringVar()
Biryani = StringVar()
Noodles = StringVar()
Manchuarian = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Momos = StringVar()

# =====================================Time================================

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="TMP", fg="black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblDateTime = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="black", bd=10, anchor='w')
lblDateTime.grid(row=1, column=0)


# ========================================Calculator=================================


def Ref():

    x = random.randint(10908, 500867)

    randomRef = str(x)
    rand.set(randomRef)
    try:
        CoB = int(Biryani.get())
    except:
        CoB=0
    try:
        CoD = int(Drinks.get())
    except:
        CoD=0
    try:
        CoM = int(Manchuarian.get())
    except:
        CoM=0
    try:
        CoNoodles = int(Noodles.get())
    except:
        CoNoodles=0
    try:
        CoChickenBurger = int(Chicken_Burger.get())
    except:
        CoChickenBurger=0
    try:
        CoMomos = int(Momos.get())
    except:
        CoMomos=0
    CostofBiryani = CoB * 100
    CostofDrinks = CoD * 20
    CostofManchurian = CoM * 40
    CostofNoodles = CoNoodles * 50
    CostofChicken_Burger = CoChickenBurger * 50
    CostofMomos = CoMomos * 40

    CostofMeal = "Rs", str('%.2f' % (CostofBiryani + CostofDrinks + CostofManchurian + CostofNoodles + CostofChicken_Burger + CostofMomos))
    PayTax = ((CostofBiryani + CostofDrinks + CostofManchurian + CostofNoodles + CostofChicken_Burger + CostofMomos) * (18/100))
    TotalCost = (CostofBiryani + CostofDrinks + CostofManchurian + CostofNoodles + CostofChicken_Burger + CostofMomos)
    Ser_Charge = ((CostofBiryani + CostofDrinks + CostofManchurian + CostofNoodles + CostofChicken_Burger + CostofMomos) *(15/100))

    Service = "Rs", str('%.2f' % Ser_Charge)
    OverAllCoast = "Rs", str(PayTax + TotalCost + Ser_Charge)
    PaidTax = "Rs", str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Total.set(OverAllCoast)


def qExit():
    root.destroy()


def Reset():
    rand.set("0")
    Biryani.set("0")
    Noodles.set("0")
    Manchuarian.set("0")
    Total.set("0")
    Service_Charge.set("0")
    Drinks.set("0")
    Tax.set("0")
    Chicken_Burger.set("0")
    Momos.set("0")
    Cost.set("0")


# txtDisplay = Label(f2,font=('arial', 20,'bold'), text="", bd=30, justify='right')
# txtDisplay.grid(columnspan=4)
# ------------------------------------------ Menu ----------------------------------------------------------
bir = Label(f2, font=('arial', 16, 'bold'), text="Menu", fg="red", bd=16, justify="right")
bir.grid(row=0, column=0)
birp = Label(f2, font=('arial', 16, 'bold'), text="Price", fg="red", bd=16, justify="right")
birp.grid(row=0, column=1)
bir = Label(f2, font=('arial', 16, 'bold'), text="Biryani..........", fg="green", bd=16, anchor='w')
bir.grid(row=1, column=0)
birp = Label(f2, font=('arial', 16, 'bold'), text="100", fg="blue", bd=16, anchor='w')
birp.grid(row=1, column=1)
bir = Label(f2, font=('arial', 16, 'bold'), text="Noodles..........", fg="green", bd=16, anchor='w')
bir.grid(row=2, column=0)
birp = Label(f2, font=('arial', 16, 'bold'), text="50", fg="blue", bd=16, anchor='w')
birp.grid(row=2, column=1)
bir = Label(f2, font=('arial', 16, 'bold'), text="Manchurian..........", fg="green", bd=16, anchor='w')
bir.grid(row=3, column=0)
birp = Label(f2, font=('arial', 16, 'bold'), text="40", fg="blue", bd=16, anchor='w')
birp.grid(row=3, column=1)
bir = Label(f2, font=('arial', 16, 'bold'), text="Burger..........", fg="green", bd=16, anchor='w')
bir.grid(row=4, column=0)
birp = Label(f2, font=('arial', 16, 'bold'), text="50", fg="blue", bd=16, anchor='w')
birp.grid(row=4, column=1)
bir = Label(f2, font=('arial', 16, 'bold'), text="Momos..........", fg="green", bd=16, anchor='w')
bir.grid(row=5, column=0)
birp = Label(f2, font=('arial', 16, 'bold'), text="40", fg="blue", bd=16, anchor='w')
birp.grid(row=5, column=1)
bir = Label(f2, font=('arial', 16, 'bold'), text="Drinks..........", fg="green", bd=16, anchor='w')
bir.grid(row=6, column=0)
birp = Label(f2, font=('arial', 16, 'bold'), text="20", fg="blue", bd=16, anchor='w')
birp.grid(row=6, column=1)
# ----------------------------------------- HOD INFO 1-----------------------------------------------------

iblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor='w')
iblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4,
                     bg="red", justify='right')
txtReference.grid(row=0, column=1)

iblBiryani = Label(f1, font=('arial', 16, 'bold'), text="Biryani ", bd=16, anchor='w')
iblBiryani.grid(row=1, column=0)
txtBiryani = Entry(f1, font=('arial', 16, 'bold'), textvariable=Biryani, bd=10, insertwidth=4,
                   bg="red", justify='right')
txtBiryani.grid(row=1, column=1)

iblNoodles = Label(f1, font=('arial', 16, 'bold'), text="Noodles", bd=16, anchor='w')
iblNoodles.grid(row=2, column=0)
txtNoodles = Entry(f1, font=('arial', 16, 'bold'), textvariable=Noodles, bd=10, insertwidth=4,
                   bg="red", justify='right')
txtNoodles.grid(row=2, column=1)

iblManchurian = Label(f1, font=('arial', 16, 'bold'), text="Manchuarian", bd=16, anchor='w')
iblManchurian.grid(row=3, column=0)
txtManchurian = Entry(f1, font=('arial', 16, 'bold'), textvariable=Manchuarian, bd=10, insertwidth=4,
                      bg="red", justify='right')
txtManchurian.grid(row=3, column=1)

iblChicken = Label(f1, font=('arial', 16, 'bold'), text="Chicken Meal", bd=16, anchor='w')
iblChicken.grid(row=4, column=0)
txtChicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken_Burger, bd=10, insertwidth=4,
                   bg="red", justify='right')
txtChicken.grid(row=4, column=1)

iblMomos = Label(f1, font=('arial', 16, 'bold'), text="Momos", bd=16, anchor='w')
iblMomos.grid(row=5, column=0)
txtCMomos = Entry(f1, font=('arial', 16, 'bold'), textvariable=Momos, bd=10, insertwidth=4,
                  bg="red", justify='right')
txtCMomos.grid(row=5, column=1)
# ----------------------------------------------- HOD INFO 2 ------------------------------------

iblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor='w')
iblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4,
                  bg="red", justify='right')
txtDrinks.grid(row=0, column=3)

iblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of meal ", bd=16, anchor='w')
iblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4,
                bg="red", justify='right')
txtCost.grid(row=1, column=3)

iblService = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor='w')
iblService.grid(row=2, column=2)
txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4,
                   bg="red", justify='right')
txtService.grid(row=2, column=3)

iblStateTax = Label(f1, font=('arial', 16, 'bold'), text="StateTax", bd=16, anchor='w')
iblStateTax.grid(row=3, column=2)
txtStateTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4,
                    bg="red", justify='right')
txtStateTax.grid(row=3, column=3)

iblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor='w')
iblTotalCost.grid(row=4, column=2)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4,
                     bg="red", justify='right')
txtTotalCost.grid(row=4, column=3)

# ----------------------------------- Button ---------------------------------------

btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Total", bg="powder blue", command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Reset", bg="powder blue", command=Reset).grid(row=7, column=2)

btnqExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Exit", bg="powder blue", command=qExit).grid(row=7, column=3)

root.mainloop()
