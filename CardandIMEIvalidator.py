from tkinter import *
import sys
from tkinter import messagebox

#var = IntVar()
window = Tk()
window.title("Card/IMEI validator")
window.geometry('400x250')

label1 = Label(window, text='Enter Credit card/Debit card/IMEI number',font=('Consolas Bold', 12))
label1.grid(column=0, row=0)

user_in = Entry(window, width=20)
user_in.grid(column=0, row=1)
user_in.focus()# This will place the cursor on entry widget by default

def validator():

    user_input_raw = user_in.get() # to get the text input from entry
    # removing white spaces between numbers if entered
    user_input = user_input_raw.strip().replace(' ', '')

    # checks whether any alphabet is present in number
    if any(a.isalpha() for a in user_input) is True:
        messagebox.showerror('Error', 'INVALID Card/IMEI number')
        sys.exit()  # terminates the program

        # checks for special characters
        # regex = re.compile('[@_!#$%^&*()<>?/\|}{~:+-`=;"./,]')
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if (regex.search(user_input) != None):
        messagebox.showerror('Error', 'INVALID Card/IMEI number')
        sys.exit()

    list1 = list(map(int, user_input))
    list2 = []
    counter = 0

    for digit in list1[::-1]:
        counter += 1
        if counter % 2 == 0:
            even_element = digit * 2
            if even_element > 9:
                even_element_to_list = list(map(int, str(even_element)))
                list_to_sum = sum(even_element_to_list)
                list2.append(list_to_sum)
            else:
                list2.append(even_element)
        else:
            list2.append(digit)

    list3 = list2[::-1]
    total_sum = sum(list3)
    if total_sum % 10 == 0:
        messagebox.showinfo('Message', 'Card/IMEI number is VALID')
    else:
        messagebox.showerror('Error', 'INVALID Card/IMEI number')


button1 = Button(window, text='Validate', command=validator, bg='khaki1',font=("Consolas Bold", 12))
button1.grid(column=0, row=2)

window.mainloop()