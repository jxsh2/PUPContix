from tkinter import *
from tkinter import messagebox
import os

# Value of each ticket 
VIP = 3000
LOWER_BOX = 1500
UPPER_BOX = 1000
GEN_AD = 800
# Value of the available ticket
MAX_VIP = 100
MAX_LOWER_BOX = 200
MAX_UPPER_BOX = 300
MAX_GEN_AD = 400

tickets_sold = {"VIP": 0, "LOWER_BOX": 0, "UPPER_BOX": 0, "GEN_AD": 0}

window = Tk()
window.title("Ticketing System")
window.geometry('1280x720')
bg_color = '#800000'

def verify():
    global dis
    if c_name.get() != "" or c_phone.get() != "":
        if c_phone.get().isnumeric() is not True:
          messagebox.showerror('Error', 'Phone number should be integer')
    else:
        messagebox.showwarning('Warning ', 'Input correct details')
        return
    messagebox.showinfo('Verified', 'Successfully Verified')

def calculate_cost():
  section = selected_section.get()
  tickets = int(num_tickets.get())
  
  if tickets > 4:
    messagebox.showerror('Error', 'You can only purchase a maximum of 4 tickets at a time')
    return
  if section == "VIP":
    total_cost = VIP * tickets
    tickets_sold["VIP"] += tickets
  elif section == "LOWER_BOX":
    total_cost = LOWER_BOX * tickets
    tickets_sold["LOWER_BOX"] += tickets
  elif section == "UPPER_BOX":
    total_cost = UPPER_BOX * tickets
    tickets_sold["UPPER_BOX"] += tickets
  elif section == "GEN_AD":
    total_cost = GEN_AD * tickets
    tickets_sold["GEN_AD"] += tickets
  else:
    total_cost = 0

  cost_label.config(text="Total cost: PHP " + str(total_cost))

def print_tickets_sold():
  vip_label.config(text="VIP: " + str(tickets_sold["VIP"]) + " (Remaining: " + str(MAX_VIP - tickets_sold["VIP"]) + ")")
  lower_box_label.config(text="LOWER_BOX: " + str(tickets_sold["LOWER_BOX"]) + " (Remaining: " + str(MAX_LOWER_BOX - tickets_sold["LOWER_BOX"]) + ")")
  upper_box_label.config(text="UPPER_BOX: " + str(tickets_sold["UPPER_BOX"]) + " (Remaining: " + str(MAX_UPPER_BOX - tickets_sold["UPPER_BOX"]) + ")")
  gen_ad_label.config(text="GEN_AD: " + str(tickets_sold["GEN_AD"]) + " (Remaining: " + str(MAX_GEN_AD - tickets_sold["GEN_AD"]) + ")")
  
def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        window.destroy()
        
def clear():
    c_name.set('')
    c_phone.set('')
    c_email.set('')
    num_tickets.set('')
    person.set(0)
    
def save_txt():
    fields = ['Name', 'Phone', 'Email', 'Number of Tickets', 'Type of Ticket', 'Price']
    filename = "ticket_sales.txt"

    # Make sure that the section and tickets variables are being defined correctly
    section = selected_section.get()
    tickets = int(num_tickets.get())

    # Calculate the price of the tickets
    if tickets_sold[section] + tickets > MAX_VIP:  
        messagebox.showerror('Error', 'There are not enough tickets available in this section')
        return
    if section == "VIP":
        price = VIP * tickets
    elif section == "LOWER_BOX":
        price = LOWER_BOX * tickets
    elif section == "UPPER_BOX":
        price = UPPER_BOX * tickets
    elif section == "GEN_AD":
        price = GEN_AD * tickets
    else:
        price = 0
    if tickets_sold[section] + tickets > MAX_VIP:  # Change MAX_VIP to the maximum number of tickets for the selected section
        messagebox.showerror('Error', 'There are not enough tickets available in this section')
        return  

    # Define the data variable with the correct values
    data = "Name: " + c_name.get() + "\n"
    data += "Phone: " + c_phone.get() + "\n"
    data += "Email: " + c_email.get() + "\n"
    data += "Number of Tickets: " + num_tickets.get() + "\n"
    data += "Type of Ticket: " + selected_section.get() + "\n"
    data += "Price: PHP " + str(price) + "\n"

    # Write the data to the file
    with open(filename, 'a') as file:
        file.write(data)

    # Increment the tickets_sold count and update the labels
    tickets_sold[section] += tickets
    print_tickets_sold()
    clear()
    messagebox.showinfo('Success', 'Ticket sale has been saved.')

  
title=Label(window,pady=2,text="PUP ConTIX",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)
  
F1=LabelFrame(window,bd=10,relief=GROOVE,text=' Details',font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

c_name = StringVar()
cname_lbl=Label(F1,text='Name',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

c_phone = StringVar()
cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

c_email = StringVar()
cemail_lbl=Label(F1,text='Email ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=5,padx=20,pady=5)
cemail_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_email,relief=SUNKEN,bd=7).grid(row=0,column=7,padx=10,pady=5)

F2 = LabelFrame(window, text='WELCOME TO PUP ConTIX!', font=('times new romon', 18, 'bold'), fg='gold',bg=bg_color)
F2.place(x=10, y=190,width=630,height=500)

selected_section = StringVar()
section_menu = OptionMenu(F2,  selected_section, "VIP", "LOWER_BOX", "UPPER_BOX", "GEN_AD")
section_menu.config(font='arial 15 bold')
section_menu.grid(row=2, column=1, padx=30, pady=20)

num_tickets = StringVar()
tickets_entry_label = Label(F2, text="Ticket")
tickets_entry = Entry(F2,textvariable=num_tickets, font='arial 15 bold', relief=SUNKEN, bd=7)
tickets_entry.config(font='arial 15 bold')
tickets_entry.grid(row=1, column=1)

person=IntVar()
n= Label(F2, text='Number of ticket', font=('times new roman',18, 'bold'), bg=bg_color, fg='white').grid(
row=1, column=0, padx=20, pady=20)

select_ticket=IntVar()
a= Label(F2, text='Select Ticket', font=('times new roman',18, 'bold'), bg=bg_color, fg='white').grid(
row=2, column=0, padx=20, pady=20)


calculate_button = Button(F2, text="Confirm Purchase", command=calculate_cost, font='arial 15 bold', padx=5, pady=10, bg='#FFD700', width=15)
calculate_button.config(font='arial 15 bold')
calculate_button.grid(row=3, column=0)

btn1 = Button(F2, text='Verify', font='arial 15 bold', command=verify, padx=5, pady=10, bg='#FFD700', width=15)
btn1.grid(row=3, column=1, padx=10, pady=30)

btn2 = Button(F2, text='Exit', font='arial 15 bold', command=exit, padx=5, pady=10, bg='#FFD700', width=15)
btn2.grid(row=4, column=0, padx=10, pady=30)

btn3 = Button(F2, text='Clear', font='arial 15 bold', padx=5, pady=10, command=clear, bg='#FFD700', width=15)
btn3.grid(row=4, column=1, padx=10, pady=30)

F3=Frame(window,relief=RAISED,bd=10)
F3.place(x=700,y=180,width=500,height=500)

cost_label = Label(F3, text="Total cost:",font='arial 15 bold', padx=5, pady=10, width=20)
cost_label.config(font='arial 15 bold')
cost_label.grid(row=1, column=0)
  
vip_label = Label(F3, text="VIP:")
vip_label.config(font='arial 10')
vip_label.grid(row=2, column=0, padx=10, pady=10)

lower_box_label = Label(F3, text="LOWER_BOX:")
lower_box_label.config(font='arial 10')
lower_box_label.grid(row=3, column=0, padx=10, pady=10 )

upper_box_label = Label(F3, text="UPPER_BOX:")
upper_box_label.config(font='arial 10')
upper_box_label.grid(row=4, column=0, padx=10, pady=10)

gen_ad_label = Label(F3, text="GEN_AD:")
gen_ad_label.config(font='arial 10')
gen_ad_label.grid(row=5, column=0, padx=10, pady=10)

print_button = Button(F3, text="Print Tickets Sold", command=print_tickets_sold,bg='#FFD700')
print_button.config(font='arial 15 bold')
print_button.grid(row=0, column=1, padx=10, pady=10)

btn4 = Button(F3, text="Save", command=save_txt, font='arial 15 bold', bg='#FFD700', width=15)
btn4.grid(row=6, column=1, padx=10, pady=10)

window.mainloop()