from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")

    else:
        is_okay = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \nEmail:"
                                                                            f"{usr_entry.get()} \nPassword: "
                                                                            f"{password_entry.get()} "
                                                                            f"\nIs it okay to save?")
        if is_okay:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_entry.get()} | {usr_entry.get()} | {password_entry.get()}\n")
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image and canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
usr_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(column=0, row=1)
usr_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.focus()
usr_entry = Entry(width=52)
usr_entry.insert(0, "@gmail.com")
password_entry = Entry(width=33)

website_entry.grid(column=1, row=1, columnspan=2)
usr_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=44, command=add_data)

generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
