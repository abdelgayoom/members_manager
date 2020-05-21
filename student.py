import tkinter as tk


class Member(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Student Manager')
        self.geometry('500x600')

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

    def add_member(self):
        pass

    def display_member(self):
        pass










if __name__=='__main__':
    app = Member()
    app.mainloop()