import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import time

from mysql.connector import cursor

from database import get_connection

class Travel:
    def __init__(self, root):
        self.root = root
        self.root.title("Passenger Information")
        self.root.geometry("1400x650+0+0")
        self.root.configure(background='black')

        # Initialize variables
        self.initialize_variables()

        # Define the layout and widgets
        self.define_layout()

    def initialize_variables(self):
        self.DateofOrder = StringVar()
        self.DateofOrder.set(time.strftime("%d/%m/%Y"))
        self.Receipt_Ref = StringVar()
        self.PaidTax = StringVar()
        self.SubTotal = StringVar()
        self.TotalCost = StringVar()

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = StringVar()
        self.var12 = StringVar()
        self.var13 = StringVar()

        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.Address = StringVar()
        self.PostCode = StringVar()
        self.Mobile = StringVar()
        self.Email = StringVar()

        self.AirportTax = StringVar()
        self.Travel_Ins = StringVar()
        self.Luggage = StringVar()

        self.Business = StringVar()
        self.Economy = StringVar()
        self.FirstClass = StringVar()

        self.AirportTax.set("0")
        self.Travel_Ins.set("0")
        self.Luggage.set("0")

        self.Business.set("0")
        self.Economy.set("0")
        self.FirstClass.set("0")

    def Airport_Tax(self):
        if self.var1.get() == 1:
            self.txtAirportTax.configure(state=NORMAL)
            Item1 = float(3800)
            self.AirportTax.set("₹" + str(Item1))
        else:
            self.txtAirportTax.configure(state=DISABLED)
            self.AirportTax.set("0")

    def Travelling(self):
        if self.var3.get() == 1:
            self.txtTravelling_Insurance.configure(state=NORMAL)
            Item3 = float(5400)
            self.Travel_Ins.set("₹" + str(Item3))
        else:
            self.txtTravelling_Insurance.configure(state=DISABLED)
            self.Travel_Ins.set("0")

    def Lug(self):
        if self.var4.get() == 1:
            self.txtExt_Luggage.configure(state=NORMAL)
            Item4 = float(6500)
            self.Luggage.set("₹" + str(Item4))
        else:
            self.txtExt_Luggage.configure(state=DISABLED)
            self.Luggage.set("0")

    def Economy_Fees(self):
        if self.var5.get() == 1:
            self.txtEconomy.configure(state=NORMAL)
            Item5 = float(24000)
            self.Economy.set("₹" + str(Item5))
        else:
            self.txtEconomy.configure(state=DISABLED)
            self.Economy.set("0")

    def Business_Fees(self):
        if self.var7.get() == 1:
            self.txtBusiness.configure(state=NORMAL)
            Item6 = float(36000)
            self.Business.set("₹" + str(Item6))
        else:
            self.txtBusiness.configure(state=DISABLED)
            self.Business.set("0")

    def FirstClass_Fees(self):
        if self.var9.get() == 1:
            self.txtFirstClass.configure(state=NORMAL)
            Item7 = float(60000)
            self.FirstClass.set("₹" + str(Item7))
        else:
            self.txtFirstClass.configure(state=DISABLED)
            self.FirstClass.set("0")

    def Total_Paid(self):
        if (self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 1 and self.var4.get() == 1 and
            self.var5.get() == 1 and self.var11.get() == "Delhi" and
            self.var12.get() == "Mumbai" and self.var13.get() == "1"):

            q1 = float(45)
            q2 = float(63)
            q3 = float(334.59)
            q4 = float(274.9)

            Cost_of_Fare = q1 + q2 + q3 + q4

            Tax = "£" + str('%.2f' % ((Cost_of_Fare) * 0.09))
            ST = "£" + str('%.2f' % ((Cost_of_Fare)))
            TT = "£" + str('%.2f' % (Cost_of_Fare + ((Cost_of_Fare) * 0.09)))
            self.PaidTax.set((Tax))
            self.SubTotal.set(ST)
            self.TotalCost.set(TT)

        elif (self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 1 and self.var4.get() == 1 and
              self.var7.get() == 1 and self.var11.get() == "Delhi" and
              self.var12.get() == "Mumbai" and self.var13.get() == "1"):

            q1 = float(45)
            q2 = float(63)
            q3 = float(334.59)
            q4 = float(365.5)

            Cost_of_Fare = q1 + q2 + q3 + q4

            Tax = "£" + str('%.2f' % ((Cost_of_Fare) * 0.09))
            ST = "£" + str('%.2f' % ((Cost_of_Fare)))
            TT = "£" + str('%.2f' % (Cost_of_Fare + ((Cost_of_Fare) * 0.09)))
            self.PaidTax.set((Tax))
            self.SubTotal.set(ST)
            self.TotalCost.set(TT)

        elif (self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 1 and self.var4.get() == 1 and
              self.var9.get() == 1 and self.var11.get() == "Delhi" and
              self.var12.get() == "Mumbai" and self.var13.get() == "1"):

            q1 = float(45)
            q2 = float(63)
            q3 = float(334.59)
            q4 = float(564.3)

            Cost_of_Fare = q1 + q2 + q3 + q4

            Tax = "£" + str('%.2f' % ((Cost_of_Fare) * 0.09))
            ST = "£" + str('%.2f' % ((Cost_of_Fare)))
            TT = "£" + str('%.2f' % (Cost_of_Fare + ((Cost_of_Fare) * 0.09)))
            self.PaidTax.set((Tax))
            self.SubTotal.set(ST)
            self.TotalCost.set(TT)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Trip Planner", "Confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return

    def Reset(self):

        self.AirportTax.set("0")
        self.Travel_Ins.set("0")
        self.Luggage.set("0")

        self.Business.set("0")
        self.Economy.set("0")
        self.FirstClass.set("0")

        self.Firstname.set("")
        self.Surname.set("")
        self.Address.set("")
        self.PostCode.set("")
        self.Mobile.set("")
        self.Email.set("")

        self.PaidTax.set("")
        self.SubTotal.set("")
        self.TotalCost.set("")
        self.txtReceipt.delete("1.0", END)

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set("0")
        self.var12.set("0")
        self.var13.set("0")

        self.cboDeparture.current(0)
        self.cboDestination.current(0)
        self.cboAccommodation.current(0)

        self.txtAirportTax.configure(state=DISABLED)
        self.txtTravelling_Insurance.configure(state=DISABLED)
        self.txtExt_Luggage.configure(state=DISABLED)

        self.txtBusiness.configure(state=DISABLED)
        self.txtEconomy.configure(state=DISABLED)
        self.txtFirstClass.configure(state=DISABLED)

    def Receipt(self):
        global x
        self.txtReceipt.delete("1.0", END)
        x = random.randint(10000, 99999)
        random_ref = str(x)
        self.Receipt_Ref.set(" Receipt No.: " + random_ref)

        receipt = x
        name = str(self.Firstname.get()) + str(self.Surname.get())
        departure = str(self.var11.get())
        destination = str(self.var12.get())
        mail = str(self.Email.get())  # Get the value for the mail column
        mobile = str(self.Mobile.get())
        query = "Insert into flight values({},'{}','{}','{}','{}','{}')".format(receipt, name, departure, destination,
                                                                                mail, mobile)
        con, cursor = get_connection()
        cursor.execute(query)
        con.commit()

        self.txtReceipt.insert(END, 'Receipt Ref:\t\t\t\t\t' + self.Receipt_Ref.get() + "\n")
        self.txtReceipt.insert(END, 'Date:\t\t\t\t\t' + self.DateofOrder.get() + "\n")
        self.txtReceipt.insert(END, 'Flight:\t\t\t\t\t' + "Travelling Details \n")
        self.txtReceipt.insert(END, 'Firstname:\t\t\t\t\t' + self.Firstname.get() + "\n")
        self.txtReceipt.insert(END, 'Surname:\t\t\t\t\t' + self.Surname.get() + "\n")
        self.txtReceipt.insert(END, 'Address:\t\t\t\t\t' + self.Address.get() + "\n")
        self.txtReceipt.insert(END, 'PostCode: \t\t\t\t\t' + self.PostCode.get() + "\n")
        self.txtReceipt.insert(END, 'Mobile: \t\t\t\t\t' + self.Mobile.get() + "\n")
        self.txtReceipt.insert(END, 'Email: \t\t\t\t\t' + self.Email.get() + "\n")
        self.txtReceipt.insert(END, 'Departure: \t\t\t\t\t' + self.var11.get() + "\n")
        self.txtReceipt.insert(END, 'Destination: \t\t\t\t\t' + self.var12.get() + "\n")
        self.txtReceipt.insert(END, 'Accomodation: \t\t\t\t\t' + self.var13.get() + "\n")
        self.txtReceipt.insert(END, 'Business: \t\t\t\t\t' + self.Business.get() + "\n")
        self.txtReceipt.insert(END, 'Economy: \t\t\t\t\t' + self.Economy.get() + "\n")
        self.txtReceipt.insert(END, 'FirstClass: \t\t\t\t\t' + self.FirstClass.get() + "\n")
        self.txtReceipt.insert(END, 'Paid:\t\t\t\t\t' + self.PaidTax.get() + "\n")
        self.txtReceipt.insert(END, 'SubTotal:\t\t\t\t\t' + str(self.SubTotal.get()) + "\n")
        self.txtReceipt.insert(END, 'Total Cost:\t\t\t\t\t' + str(self.TotalCost.get()))

    def define_layout(self):
        image_path = "airport.png"
        original_image = Image.open(image_path)

        MainFrame = Frame(self.root, bg="light blue")
        MainFrame.grid()

        Tops = Frame(MainFrame, bd=20, width=1350, relief=RIDGE, bg="sky blue")
        Tops.pack(side=TOP)

        self.lblTitle = Label(Tops, font=('arial', 70, 'bold'), text="    Ticket Receipt Generator     ",
                              compound="center")
        # Get the size of the label
        label_width = self.lblTitle.winfo_reqwidth()
        label_height = self.lblTitle.winfo_reqheight()
        resized_image = original_image.resize((label_width, label_height), Image.ANTIALIAS)

        # Convert the resized image to a PhotoImage
        background_image = ImageTk.PhotoImage(resized_image)

        # Update the label with the resized image
        self.lblTitle.config(image=background_image)
        self.lblTitle.image = background_image
        self.lblTitle.grid()

        # ===================Adding Columns and Rows where things will be added========================
        image_path_customer_details_frame = "air.png"
        original_image_customer_details_frame = Image.open(image_path_customer_details_frame)

        # Create the CustomerDetailsFrame
        CustomerDetailsFrame = Frame(MainFrame, width=1350, height=500, bd=20, pady=5, relief=RIDGE, bg="light blue")
        CustomerDetailsFrame.pack(side=BOTTOM)

        # Divide CustomerDetailsFrame into 2 parts
        frame_details = Frame(CustomerDetailsFrame, width=880, height=400, bd=10, relief=RIDGE, bg="light blue")
        frame_details.pack(side=LEFT)

        FrameReceipt = Frame(CustomerDetailsFrame, width=450, height=400, bd=10, relief=RIDGE, bg="light blue")
        FrameReceipt.pack(side=RIGHT)

        CustomerName = LabelFrame(frame_details, width=150, height=250, font=('arial', 20, 'bold'), text="Customer Name",
                                  relief=GROOVE, bg="light blue", bd=10)
        CustomerName.grid(row=0, column=0)

        TravelFrame = LabelFrame(frame_details, bd=10, width=300, height=250,
                                 font=('arial', 20, 'bold'), text='Travel Details', relief=GROOVE, bg="light blue")
        TravelFrame.grid(row=0, column=1)

        Ticket_Frame = LabelFrame(frame_details, width=300, height=150, relief=GROOVE)
        Ticket_Frame.grid(row=1, column=0)

        CostFrame = LabelFrame(frame_details, width=150, height=150, relief=GROOVE)
        CostFrame.grid(row=1, column=1)

        # ====================Adding Reciepts=============================================
        ReceiptFrame = LabelFrame(FrameReceipt, width=350, height=300,
                                  font=('arial', 12, 'bold'), text='Receipt', relief=RIDGE, bg="light blue")
        ReceiptFrame.grid(row=0, column=0)

        ButtonFrame = LabelFrame(FrameReceipt, width=350, height=100, relief=RIDGE)

        ButtonFrame.grid(row=1, column=0)

        # ==========================Customer Name Widgets===================================

        self.lblFirstname = Label(CustomerName, font=('arial', 14, 'bold'), text="Firstname", bd=7, bg="light blue")
        self.lblFirstname.grid(row=0, column=0, sticky=W)
        self.txtFirstname = Entry(CustomerName, font=('arial', 14, 'bold'), bd=7, width=22, justify='left',
                                  textvariable=self.Firstname)
        self.txtFirstname.grid(row=0, column=1)

        self.lblSurname = Label(CustomerName, font=('arial', 14, 'bold'), text="Surname", bd=7, bg="light blue")
        self.lblSurname.grid(row=1, column=0, sticky=W)
        self.txtSurname = Entry(CustomerName, font=('arial', 14, 'bold'), bd=7, width=22, justify='left',
                                textvariable=self.Surname)
        self.txtSurname.grid(row=1, column=1)

        self.lblAddress = Label(CustomerName, font=('arial', 14, 'bold'), text="Address", bd=7, bg="light blue")
        self.lblAddress.grid(row=2, column=0, sticky=W)
        self.txtAddress = Entry(CustomerName, font=('arial', 14, 'bold'), bd=7, width=22, justify='left',
                                textvariable=self.Address)
        self.txtAddress.grid(row=2, column=1)

        self.lblPostCode = Label(CustomerName, font=('arial', 14, 'bold'), text="PostCode", bd=7, bg="light blue")
        self.lblPostCode.grid(row=3, column=0, sticky=W)
        self.txtPostCode = Entry(CustomerName, font=('arial', 14, 'bold'), bd=7, width=22, justify='left',
                                 textvariable=self.PostCode)
        self.txtPostCode.grid(row=3, column=1)

        self.lblMobile = Label(CustomerName, font=('arial', 14, 'bold'), text="Mobile", bd=7, bg="light blue")
        self.lblMobile.grid(row=4, column=0, sticky=W)
        self.txtMobile = Entry(CustomerName, font=('arial', 14, 'bold'), bd=7, width=22, justify='left',
                               textvariable=self.Mobile)
        self.txtMobile.grid(row=4, column=1)

        self.lblEmail = Label(CustomerName, font=('arial', 14, 'bold'), text="Email", bd=7, bg="light blue")
        self.lblEmail.grid(row=5, column=0, sticky=W)
        self.txtEmail = Entry(CustomerName, font=('arial', 14, 'bold'), bd=7, width=22, justify='left',
                              textvariable=self.Email)
        self.txtEmail.grid(row=5, column=1)

        # ======================================Flight Information=====================================
        self.lblDeparture = Label(TravelFrame, font=('arial', 15, 'bold'), text="Departure\t", bd=7, bg="light blue")
        self.lblDeparture.grid(row=0, column=0, sticky=W)

        self.cboDeparture = ttk.Combobox(TravelFrame, textvariable=self.var11, state='readonly', font=('arial', 20, 'bold'),
                                         width=14)
        self.cboDeparture['value'] = (
        '', 'SVPIA,Ahmedabad', 'SGRDJA,Amritsar', 'KIA,Banglore', 'CSIA,Mumbai', 'IGIA,Delhi', 'JIA,Jaipur',
        'CCSIA,Lucknow', 'NSCBIA,Kolkata')
        self.cboDeparture.current(0)
        self.cboDeparture.grid(row=0, column=1)

        self.lblDestination = Label(TravelFrame, font=('arial', 15, 'bold'), text="Destination\t", bd=7,
                                    bg="light blue")
        self.lblDestination.grid(row=1, column=0, sticky=W)

        self.cboDestination = ttk.Combobox(TravelFrame, textvariable=self.var12, state='readonly',
                                           font=('arial', 20, 'bold'),
                                           width=14)
        self.cboDestination['value'] = (
        '', 'SVPIA,Ahmedabad', 'SGRDJA,Amritsar', 'KIA,Banglore', 'CSIA,Mumbai', 'IGIA,Delhi', 'JIA,Jaipur',
        'CCSIA,Lucknow', 'NSCBIA,Kolkata')
        self.cboDestination.current(0)
        self.cboDestination.grid(row=1, column=1)

        self.lblAccommodation = Label(TravelFrame, font=('arial', 15, 'bold'), text="Accommodation\t", bd=7,
                                      bg="light blue")
        self.lblAccommodation.grid(row=2, column=0, sticky=W)

        self.cboAccommodation = ttk.Combobox(TravelFrame, textvariable=self.var13, state='readonly',
                                             font=('arial', 20, 'bold'),
                                             width=14)
        self.cboAccommodation['value'] = ('', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.cboAccommodation.current(1)
        self.cboAccommodation.grid(row=2, column=1)

        # ==============================================================================================
        self.chkAirportTax = Checkbutton(TravelFrame, text="Airport Tax    \t  ", variable=self.var1, onvalue=1, offvalue=0,
                                         font=('arial', 16, 'bold'), command=self.Airport_Tax, bg="light blue").grid(row=3,
                                                                                                                     column=0,
                                                                                                                     sticky=W)
        self.txtAirportTax = Entry(TravelFrame, font=('arial', 14, 'bold'), textvariable=self.AirportTax, bd=7,
                                   insertwidth=2, state=DISABLED, justify=RIGHT, bg="light blue")
        self.txtAirportTax.grid(row=3, column=1)

        self.chkTravelling_Insurance = Checkbutton(TravelFrame, text="Travelling Insurance", variable=self.var3,
                                                   onvalue=1, offvalue=0,
                                                   font=('arial', 16, 'bold'), command=self.Travelling,
                                                   bg="light blue").grid(row=5, column=0, sticky=W)

        self.txtTravelling_Insurance = Entry(TravelFrame, font=('arial', 14, 'bold'), textvariable=self.Travel_Ins, bd=7,
                                             insertwidth=2, state=DISABLED, justify=RIGHT, bg="light blue")
        self.txtTravelling_Insurance.grid(row=5, column=1)

        self.chkExt_Luggage = Checkbutton(TravelFrame, text="Ext. Luggage    \t  ", variable=self.var4, onvalue=1,
                                          offvalue=0,
                                          font=('arial', 16, 'bold'), command=self.Lug, bg="light blue").grid(row=6,
                                                                                                              column=0,
                                                                                                              sticky=W)
        self.txtExt_Luggage = Entry(TravelFrame, font=('arial', 14, 'bold'), textvariable=self.Luggage, bd=7,
                                    insertwidth=2, state=DISABLED, justify=RIGHT, bg="light blue")
        self.txtExt_Luggage.grid(row=6, column=1)

        # =======================================Payment Information====================================

        self.lblPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), text="Paid Tax\t\t", bd=7, bg="light blue")
        self.lblPaidTax.grid(row=0, column=2, sticky=W)
        self.txtPaidTax = Entry(CostFrame, font=('arial', 14, 'bold'), textvariable=self.PaidTax, bd=7,
                                width=26, justify=RIGHT, bg="light blue")
        self.txtPaidTax.grid(row=0, column=3)

        self.lblSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), text="Sub Total\t", bd=7, bg="light blue")
        self.lblSubTotal.grid(row=1, column=2, sticky=W)
        self.txtSubTotal = Entry(CostFrame, font=('arial', 14, 'bold'), textvariable=self.SubTotal, bd=7,
                                 width=26, justify=RIGHT, bg="light blue")
        self.txtSubTotal.grid(row=1, column=3)

        self.lblTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), text="Total Cost\t", bd=7, bg="light blue")
        self.lblTotalCost.grid(row=2, column=2, sticky=W)
        self.txtTotalCost = Entry(CostFrame, font=('arial', 14, 'bold'), textvariable=self.TotalCost, bd=7, bg="light blue",
                                  width=26, justify=RIGHT)
        self.txtTotalCost.grid(row=2, column=3)

        # ==================Ticket Class==================

        self.chkEconomy = Checkbutton(Ticket_Frame, text="Economy  ", variable=self.var5, onvalue=1, offvalue=0,
                                      font=('arial', 14, 'bold'), command=self.Economy_Fees, bg="light blue").grid(row=0,
                                                                                                                   column=0)
        self.txtEconomy = Entry(Ticket_Frame, font=('arial', 14, 'bold'), width=6, textvariable=self.Economy, bd=5,
                                state=DISABLED, justify=RIGHT, bg="light blue")
        self.txtEconomy.grid(row=0, column=1)

        self.chkSingle = Checkbutton(Ticket_Frame, text="Single                    ", variable=self.var6, onvalue=1,
                                     offvalue=0,
                                     font=('arial', 14, 'bold'), bg="light blue").grid(row=0, column=2, sticky=W)

        self.chkBusiness = Checkbutton(Ticket_Frame, text="Business  ", variable=self.var7, onvalue=1, offvalue=0,
                                       font=('arial', 14, 'bold'), command=self.Business_Fees, bg="light blue").grid(row=1,
                                                                                                                     column=0,
                                                                                                                     sticky=W)

        self.txtBusiness = Entry(Ticket_Frame, font=('arial', 14, 'bold'), width=6, textvariable=self.Business, bd=5,
                                 state=DISABLED, justify=RIGHT, bg="light blue")
        self.txtBusiness.grid(row=1, column=1)

        self.chkReturn = Checkbutton(Ticket_Frame, text="Return                   ", variable=self.var8, onvalue=1,
                                     offvalue=0,
                                     font=('arial', 14, 'bold'), bg="light blue").grid(row=1, column=2, sticky=W)

        self.chkFirstClass = Checkbutton(Ticket_Frame, text="First Class", variable=self.var9, onvalue=1, offvalue=0,
                                         font=('arial', 14, 'bold'), command=self.FirstClass_Fees, bg="light blue").grid(
            row=2, column=0)
        self.txtFirstClass = Entry(Ticket_Frame, font=('arial', 14, 'bold'), width=6, textvariable=self.FirstClass, bd=5,
                                   bg="light blue"
                                   , state=DISABLED, justify=RIGHT)
        self.txtFirstClass.grid(row=2, column=1)

        self.chkSpecialsNeeds = Checkbutton(Ticket_Frame, text="Specials Needs   ", variable=self.var10, onvalue=1,
                                            offvalue=0, font=('arial', 14, 'bold'), bg="light blue").grid(row=2,
                                                                                                          column=2,
                                                                                                          sticky=W)

        # ==========================================Receipt=============================================

        self.txtReceipt = Text(ReceiptFrame, width=60, height=21, font=('arial', 10, 'bold'))
        self.txtReceipt.grid(row=0, column=0)

        # ===========================================Buttons============================================
        Button(ButtonFrame, padx=18, bd=7, font=('calibri', 16, 'bold'), width=4,
               text='Print', command=self.Total_Paid, bg="light blue").grid(row=0, column=0)
        Button(ButtonFrame, padx=18, bd=7, font=('calibri', 16, 'bold'), width=4,
               text='Receipt', command=self.Receipt, fg='blue', bg="light blue").grid(row=0, column=1)
        Button(ButtonFrame, padx=18, bd=7, font=('calibri', 16, 'bold'), width=4,
               text='Reset', command=self.Reset, bg="light blue").grid(row=0, column=2)
        Button(ButtonFrame, padx=18, bd=7, font=('calibri', 16, 'bold'), width=4,
               text='Exit', command=self.iExit, fg='black', bg="red").grid(row=0, column=3)
        # ==============================================================================================

if __name__ == "__main__":
    root = Tk()
    app = Travel(root)
    root.mainloop()
