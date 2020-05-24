import tkinter as tk
from tkinter.constants import *
from tkinter import messagebox
from members_manager.database import Db

db = Db('members.db')


class Member(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Student Manager')
        self.geometry('700x600')

        # member display section design
        self.member_display_frame = tk.Frame(self)
        self.member_display_frame.grid(row=1, column=0, ipadx=20, ipady=20)
        self.member_info = tk.Listbox(self.member_display_frame, height=40, width=40)
        self.member_info.grid(row=0, column=0, rowspan=3, columnspan=3)

        # registering member section design
        self.user_enter_frame = tk.Frame(self)
        self.user_enter_frame.grid(row=0, column=0)

        self.first_name = tk.Label(self.user_enter_frame, text='First Name :', padx=10, pady=10)
        self.first_name.grid(row=0, column=0)
        self.first_name_text = tk.StringVar()
        self.first_name_text = tk.Entry(self.user_enter_frame, textvariable=self.first_name_text)
        self.first_name_text.grid(row=0, column=1)

        self.last_name = tk.Label(self.user_enter_frame, text='Last Name :', padx=10, pady=10)
        self.last_name.grid(row=1, column=0)
        self.last_name_text = tk.StringVar()
        self.last_name_text = tk.Entry(self.user_enter_frame, textvariable=self.last_name_text)
        self.last_name_text.grid(row=1, column=1)

        self.email = tk.Label(self.user_enter_frame, text='Email Address:', padx=10, pady=10)
        self.email.grid(row=2, column=0)
        self.email_text = tk.StringVar()
        self.email_text = tk.Entry(self.user_enter_frame, textvariable=self.email_text)
        self.email_text.grid(row=2, column=1)

        self.phone = tk.Label(self.user_enter_frame, text='Phone Number :', padx=10, pady=10)
        self.phone.grid(row=3, column=0)
        self.phone_text = tk.StringVar()
        self.phone_text = tk.Entry(self.user_enter_frame, textvariable=self.phone_text)
        self.phone_text.grid(row=3, column=1)

        self.home_address = tk.Label(self.user_enter_frame, text='Home Address :', padx=10, pady=10)
        self.home_address.grid(row=4, column=0)
        self.home_address_text = tk.StringVar()
        self.home_address_text = tk.Entry(self.user_enter_frame, textvariable=self.home_address_text)
        self.home_address_text.grid(row=4, column=1)

        self.add_member_button = tk.Button(self.user_enter_frame, text='Add Member', command=self.add_member)
        self.add_member_button.grid(row=5, column=0)

        # getting member info section design
        self.user_getting_frame = tk.Frame(self)
        self.user_getting_frame.grid(row=0, column=1)

        self.first_name_g = tk.Label(self.user_getting_frame, text='First Name :', padx=10, pady=10)
        self.first_name_g.grid(row=0, column=0)
        self.first_name_g_text = tk.StringVar()
        self.first_name_g_text = tk.Entry(self.user_getting_frame, textvariable=self.first_name_g_text)
        self.first_name_g_text.grid(row=0, column=1)

        self.email_g = tk.Label(self.user_getting_frame, text='Email Address:', padx=10, pady=10)
        self.email_g.grid(row=1, column=0)
        self.email_g_text = tk.StringVar()
        self.email_g_text = tk.Entry(self.user_getting_frame, textvariable=self.email_g_text)
        self.email_g_text.grid(row=1, column=1)

        self.get_member_button = tk.Button(self.user_getting_frame, text='Search Member', command=self.get_member)
        self.get_member_button.grid(row=2, column=0)

    def add_member(self):
        """ insert member in the database """
        if self.first_name_text.get() == '' or self.last_name_text.get() == '' or self.email_text.get() == '' or self.phone_text.get() == '' or self.home_address_text.get() == '':
            messagebox.showerror('Empty Field', 'all fields required')
            return False
        db.insert(self.first_name_text.get(), self.last_name_text.get(), self.email_text.get(), self.phone_text.get(),
                  self.home_address_text.get())
        self.clear_add_member_inputs()

    def get_member(self):
        """ retrieve member from database """
        if self.first_name_g_text.get() == '' or self.email_g_text.get() == '':
            messagebox.showerror('Empty Field', 'all fields required')
            self.clear_member_search_inputs()
            return False
        else:
            for row in db.fetch(self.first_name_g_text.get(), self.email_g_text.get()):
                row_dict = list(row)
                for r in row_dict:
                    self.member_info.insert(END, r)
                    self.clear_member_search_inputs()

    def clear_member_search_inputs(self):
        """ clear member retrieve inputs """
        self.first_name_g_text.delete(0, END)
        self.email_g_text.delete(0, END)

    def clear_add_member_inputs(self):
        """ clear member add inputs """
        self.first_name_text.delete(0, END)
        self.last_name_text.delete(0, END)
        self.email_text.delete(0, END)
        self.phone_text.delete(0, END)
        self.home_address_text.delete(0, END)


if __name__ == '__main__':
    app = Member()
    app.mainloop()
