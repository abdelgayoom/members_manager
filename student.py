import tkinter as tk
from tkinter.constants import *


class Member(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Student Manager')
        self.geometry('500x600')

        self.first_name = tk.Label(self, text='First Name :', padx=10, pady=10)
        self.first_name.grid(row=0, column=0)
        self.first_name_text = tk.StringVar()
        self.first_name_text = tk.Entry(self, textvariable=self.first_name_text)
        self.first_name_text.grid(row=0, column=1)

        self.last_name = tk.Label(self, text='Last Name :', padx=10, pady=10)
        self.last_name.grid(row=1, column=0)
        self.last_name_text = tk.StringVar()
        self.last_name_text = tk.Entry(self, textvariable=self.last_name_text)
        self.last_name_text.grid(row=1, column=1)

        self.email = tk.Label(self, text='Email Address:', padx=10, pady=10)
        self.email.grid(row=2, column=0)
        self.email_text = tk.StringVar()
        self.email_text = tk.Entry(self, textvariable=self.email_text)
        self.email_text.grid(row=2, column=1)

        self.phone = tk.Label(self, text='Phone Number :', padx=10, pady=10)
        self.phone.grid(row=3, column=0)
        self.phone_text = tk.StringVar()
        self.phone_text = tk.Entry(self, textvariable=self.phone_text)
        self.phone_text.grid(row=3, column=1)

        self.home_address = tk.Label(self, text='Phone Number :', padx=10, pady=10)
        self.home_address.grid(row=4, column=0)
        self.home_address_text = tk.StringVar()
        self.home_address_text = tk.Entry(self, textvariable=self.home_address_text)
        self.home_address_text.grid(row=4, column=1)


if __name__=='__main__':
    app = Member()
    app.mainloop()