from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
FONT_NAME = "Ariel"
FONT_SIZE = 8

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def data_tofile():

        #get data from app
        website = web_entry.get()
        login = user_entry.get()
        password = pw_entry.get()

        #create PYTHON dictionary to store new data entries
        new_data = {
            website: {
                "login": login,
                "password" : password,
            }
        }

        if len(website) == 0:
            messagebox.showinfo(title="Oops!", message="You didn't enter a website! \n "
                                                       "Please check your info and try again. ")
        elif len(login) == 0:
            messagebox.showinfo(title="Oops!", message="You didn't enter a username/email! \n "
                                                       "Please check your info and try again. ")
        elif len(password) == 0:
            messagebox.showinfo(title="Oops!", message="You didn't enter a password! \n "
                                                       "Please check your info and try again. ")

        else:
            try:
                #access data file
                with open('PW_Manager.json', 'r') as data_file:
                    #Read old data
                    data = json.load(data_file)

            #if 'PW_Manager.json' does'nt exist..
            except FileNotFoundError:
                #create the data file and put the new data in!
                with open('PW_Manager.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)

            #otherwise if the file already exists
            else:
                #update the python data file with new data
                data.update(new_data)

                #open the JSON data file
                with open("PW_Manager.json", 'w') as data_file:

                    #save updated PYTHON data into JSON file
                    json.dump(new_data, data_file, indent=4)

            finally:
                # clear entry fields of text
                    web_entry.delete(0,END)
                    pw_entry.delete(0, END)

                #confirmation
                    messagebox.showinfo(title="Secure", message="Your credentials have been saved! \n"
                                                                "New password copied to clipboard! :)")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    #pull website from web_entry
    website = web_entry.get()
    # access data file
    try:
        with open('PW_Manager.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data from {website} found.")
    else:
        if website in data:
            login = data[website]["login"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Login: {login}\n"
                                                       f"Password: {password}")
        else:
            messagebox.showinfo(title=website, message=f"no details for {website} exist.")


# ---------------------------- UI SETUP ------------------------------- #

"""Main Window"""
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
window.minsize(300,300)

#CANVAS
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

"""COMPONENTS"""

#LABELS
web_lbl = Label(text="Website:", font=(FONT_NAME, FONT_SIZE))
web_lbl.grid(column=0, row=1)

user_lbl = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
user_lbl.grid(column=0, row=2)

pw_lbl = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
pw_lbl.grid(column=0, row=3)

#ENTRY FORMS
web_entry = Entry(width=32)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=1)

user_entry = Entry(width=50)
user_entry.insert(0, "Jbbrunner10@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2)

pw_entry = Entry(width=32)
pw_entry.grid(column=1, row=3,)

#BUTTONS
gen_btn = Button(text="Generate Password", font=(FONT_NAME, FONT_SIZE), command=generate_pw)
gen_btn.grid(column=2, row=3)

add_btn = Button(text="Add", font=(FONT_NAME, FONT_SIZE), width=49, command=data_tofile)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", font=(FONT_NAME, FONT_SIZE), width=16, command=find_password)
search_btn.grid(column=2, row=1)

"""MAINLOOP"""
window.mainloop()