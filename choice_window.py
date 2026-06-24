from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from customer_input import Travel
from database import get_connection
from tkinter import Tk, ttk, simpledialog
from tkinter.messagebox import showinfo


class ChoiceWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Database Manager")
        self.root.geometry("580x680")
        self.root.configure(background='light blue')

        self.lblTitle = Label(root, font=('Helvetica', 24, 'bold'), text="Flight Database Manager", bg="light blue",
                              fg="black", bd=10, relief="raised")
        self.lblTitle.pack(pady=20)

        self.image = PhotoImage(file="aeroplane.png")
        self.imgLabel = Label(root, image=self.image)
        self.imgLabel.pack()

        self.btnEnterInfo = Button(root, text="Enter Information", relief="raised", command=self.enter_info, width=20,
                                   font=('Helvetica', 14), background="sky blue")
        self.btnEnterInfo.pack(pady=10)

        self.btnShowDetails = Button(root, text="Show Database", relief="raised", command=self.show_details, width=20,
                                     font=('Helvetica', 14), background="sky blue")
        self.btnShowDetails.pack(pady=10)

        self.btnShowDepartureDatabase = Button(root, text="Show Database for Each Airport Departure", relief="raised",
                                               command=self.show_departure_database, width=40, font=('Helvetica', 14),
                                               background="sky blue")
        self.btnShowDepartureDatabase.pack(pady=10)

        self.btnShowDestinationDatabase = Button(root, text="Show Database for Airport Destination", relief="raised",
                                                 command=self.show_destination_database, width=40,
                                                 font=('Helvetica', 14), background="sky blue")
        self.btnShowDestinationDatabase.pack(pady=10)

    def enter_info(self):
        self.root.destroy()
        self.travel_app = Travel(Tk())

    def show_details(self):
        self.root.destroy()
        self.display_database_contents()

    def show_destination_database(self):
        self._show_database("destination")

    def show_departure_database(self):
        self._show_database("departure")

    def _show_database(self, mode):
        db_window = Tk()
        db_window.title(f"Choose {mode.capitalize()} Airport")

        lblInstruction = Label(db_window, text=f"Choose {mode.capitalize()} Airport:", font=('Helvetica', 16),
                               bg="light blue")
        lblInstruction.pack(pady=10)

        cbo = ttk.Combobox(db_window, state='readonly', font=('Helvetica', 16), width=25)
        cbo['values'] = (
        'SVPIA,Ahmedabad', 'SGRDJA,Amritsar', 'KIA,Banglore', 'CSIA,Mumbai', 'IGIA,Delhi', 'JIA,Jaipur',
        'CCSIA,Lucknow', 'NSCBIA,Kolkata')
        cbo.current(0)
        cbo.pack(pady=10)

        btnShowDatabase = Button(db_window, text="Show Database",
                                 command=lambda: self.show_database_by_airport(mode, cbo.get(), db_window),
                                 font=('Helvetica', 14), bg="sky blue")
        btnShowDatabase.pack(pady=10)

    def show_database_by_airport(self, mode, airport, window):
        # Function to prompt for password
        def prompt_password(parent):
            password = simpledialog.askstring("Password", "Enter Admin Password:", show='*', parent=parent)
            return password

        # Check password validity
        def is_valid_password(password):
            # Replace with your actual password validation logic
            return password == "jalaj"  # Example password validation

        # Main function logic
        con, cursor = get_connection()
        query = f"SELECT * FROM flight WHERE {mode.capitalize()}=%s"
        cursor.execute(query, (airport,))
        rows = cursor.fetchall()
        con.close()

        # Create a temporary window to act as the parent for the password prompt
        temp_window = Toplevel()
        temp_window.withdraw()  # Hide the window

        # Prompt for password
        password = prompt_password(temp_window)

        temp_window.destroy()  # Destroy the temporary window

        if password is None:
            # User canceled password prompt
            return

        # Validate password
        if not is_valid_password(password):
            showinfo("Access Denied", "Incorrect password.")
            return

        # Password is correct, show flight details
        details_window = Tk()
        details_window.title(f"Flight Details for {mode.capitalize()}: {airport}")

        # Create a frame to hold the Treeview and scrollbar
        frame = ttk.Frame(details_window)
        frame.pack(expand=True, fill=BOTH)

        # Create the Treeview
        tree = ttk.Treeview(frame)
        tree["columns"] = ("Receipt", "Name", "Departure", "Destination", "Mail", "Mobile")

        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, width=200)
        # Set the width of the first column to zero (hidden)
        tree.column("#0", width=0)

        for row in rows:
            tree.insert("", "end", values=row)

        # Create a vertical scrollbar
        vsb = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side=RIGHT, fill=Y)

        # Create a horizontal scrollbar
        hsb = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(side=BOTTOM, fill=X)

        # Pack the Treeview widget
        tree.pack(expand=True, fill=BOTH)

        window.destroy()
        details_window.mainloop()

    def display_database_contents(self):
        # Function to prompt for password
        def prompt_password(parent):
            password = simpledialog.askstring("Password", "Enter Admin Password:", show='*', parent=parent)
            return password

        # Check password validity
        def is_valid_password(password):
            # Replace with your actual password validation logic
            return password == "jalaj"  # Example password validation

        # Create a temporary window to act as the parent for the password prompt
        temp_window = Toplevel()
        temp_window.withdraw()  # Hide the window

        # Prompt for password
        password = prompt_password(temp_window)

        temp_window.destroy()  # Destroy the temporary window

        if password is None:
            # User canceled password prompt
            return

        # Validate password
        if not is_valid_password(password):
            showinfo("Access Denied", "Incorrect password.")
            return

        # Password is correct, show flight details
        con, cursor = get_connection()
        cursor.execute("SELECT * FROM flight")
        rows = cursor.fetchall()
        con.close()

        details_window = Tk()
        details_window.title("Flight Details")

        # Create a frame to hold the Treeview and scrollbar
        frame = ttk.Frame(details_window)
        frame.pack(expand=True, fill=BOTH)

        # Create the Treeview
        tree = ttk.Treeview(frame)
        tree["columns"] = ("Receipt", "Name", "Departure", "Destination", "Mail", "Mobile")

        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, width=200)
        # Set the width of the first column to zero (hidden)
        tree.column("#0", width=0)

        for row in rows:
            tree.insert("", "end", values=row)

        # Create a vertical scrollbar
        vsb = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side=RIGHT, fill=Y)

        # Create a horizontal scrollbar
        hsb = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(side=BOTTOM, fill=X)

        # Pack the Treeview widget
        tree.pack(expand=True, fill=BOTH)

        details_window.mainloop()
