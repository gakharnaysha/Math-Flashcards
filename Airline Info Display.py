## Name: Naysha Gakhar, id: 869875
# Description:
#             With this program, the user is welcomed to the AirOntario website
#             and can view upcoming scheduled domestic flights. The user is
#             prompted to go to the next tab and choose what seat they would
#             like to purchase and in which class. Lastly, a final cost with the
#             appropriate taxes will be displayed for the use to pay. 

#Import from libraries
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox

#Colour Variables
bg_colour = "#E5D9C7" 

#Main window 
window = Tk()
window.title("AirOntario")
window.geometry("900x500")
window.configure(bg = bg_colour)

#Creating tabs 
my_notebook = ttk.Notebook(window)
my_notebook.pack(pady = 15)

tab1 = Frame(my_notebook, width = 900, height = 500)
tab1.configure(bg=bg_colour) 
tab2 = Frame(my_notebook, width = 900, height = 500)
tab2.configure(bg=bg_colour)
tab3 = Frame(my_notebook, width = 900, height = 500)
tab3.configure(bg=bg_colour) 

tab1.pack(fill="both", expand = 1)
tab2.pack(fill="both", expand = 1)
tab3.pack(fill="both", expand = 1)

my_notebook.add(tab1, text = "Welcome to AirOntario")
my_notebook.add(tab2, text = "AirOntario Flight Information")
my_notebook.add(tab3, text = "Purchase a Ticket")

#Data
flight_info = [
    ["City", "Departure", "Arrival", "Carousel", "Airport", "Flight Number", "Terminal", "Status"],
    ["Regina", "8:10 AM", "9:30 AM", "8", "YQR", "AO1921", "2", "On Time"],
    ["Thunder Bay", "9:40 AM", "11:30 AM", "1", "YQT", "AO1923", "1", "Cancelled"],
    ["Winnipeg", "9:30 AM", "12:35 PM", "3", "YWG", "AO1924", "1", "On Time"],
    ["Ottawa", "11:10 AM", "12:05 AM", "7", "YOW", "AO1926", "3", "Cancelled"],
    ["Yellowknife", "8:20 AM", "1:00 PM", "2", "YZF", "AO1922", "1", "On Time"],
    ["PEI", "11:10 AM", "1:30 PM", "3", "YYG", "AO1928", "1", "Arrived"],
    ["Halifax", "5:10 AM", "7:15 AM", "6", "YHZ", "AO1927", "3", "Cancelled"],
    ["Edmonton", "4:10 AM", "8:30 AM", "4", "YEG", "AO1929", "1", "Delayed"],
    ["Hamilton", "9:10 AM", "9:50 AM", "3", "YHM", "AO1930", "2", "On Time"],
    ["Montreal", "2:30 PM", "3;30 PM", "9", "YUL", "AO1934", "2", "On Time"],
    ["Vancouver", "4;05 PM", "9:30 PM", "10", "YVR", "AO1932", "1", "Delayed"],
    ["Calgary", "3:30 PM", "7:10 PM", "13", "YYC", "AO1935", "2", "On Time"]
]

#Colours for each city
city_colours = [
    ("Regina", "#07DA63"),
    ("Thunder Bay", "#C62D42"),
    ("Winnipeg", "#07DA63"),
    ("Ottawa", "#C62D42"),
    ("Yellowknife", "#07DA63"),
    ("PEI", "#7DBBC3"),
    ("Halifax", "#C62D42"),
    ("Edmonton", "#FFDB58"),
    ("Hamilton", "#07DA63"),
    ("Montreal", "#07DA63"),
    ("Vancouver", "#FFDB58"),
    ("Calgary", "#07DA63")
]

#Main Code
def get_colour(city):
    for name, colour in city_colours:
        if name == city:
            return colour

def generate_table(data, parent):
    def create_label(parent, text, row, column, font=None, bg_colour=bg_colour):
        label = Label(parent, text=text, borderwidth=1, relief="solid", \
                      padx=10, pady=5, bg=bg_colour, font=font)
        label.grid(row=row, column=column, sticky="nsew")
    
    for i in range(len(data)):
        row = data[i]
        for j in range(len(row)):
            value = row[j]
            if i == 0:
                create_label(parent, value, i, j, font=("Times", 15, "bold"),\
                             bg_colour="white")
            else:
                city = row[0]
                colour = get_colour(city)
                create_label(parent, value, i, j, bg_colour=colour)

    #Cells expanding according to frame
    for i in range(len(data)):
        parent.grid_rowconfigure(i, weight=1)
    for j in range(len(data[0])):
        parent.grid_columnconfigure(j, weight=1)

#Generate table in tab2
generate_table(flight_info, tab2)

#Tab 3
#Info for dropdown menu
cities = ["Regina", "Thunder Bay", "Winnipeg", "Ottawa", "Yellowknife", "PEI", \
          "Halifax", "Edmonton", "Hamilton", "Montreal", "Vancouver", "Calgary"]

class_box = ["Business", "Premium Economy", "Economy"]

bags = [0, 1, 2, 3]

bagfee = 20 

#Pricing for each city
def city_pricing(city):
    if city == "Regina":
        return 160
    elif city == "Thunder Bay":
        return 120
    elif city == "Winnipeg":
        return 100
    elif city == "Ottawa":
        return 250
    elif city == "Yellowknife":
        return 350
    elif city == "PEI":
        return 150
    elif city == "Halifax":
        return 110
    elif city == "Edmonton":
        return 150
    elif city == "Hamilton":
        return 80
    elif city == "Montreal":
        return 250
    elif city == "Vancouver":
        return 210
    elif city == "Calgary":
        return 160
    else:
        return 0

#Pricing for each class
def class_pricing(plane_class):
    if plane_class == "Business":
        return 200
    elif plane_class == "Economy":
        return 0
    elif plane_class == "Premium Economy":
        return 100
    else:
        return 0

#Total pricing
def total():
    city = citycombo.get()
    plane_class = classcombo.get()
    bags = int(bagcombo.get()) 
    
    #City price
    city_price = city_pricing(city)
    
    #Class price
    class_price = class_pricing(plane_class)
    
    #Total Bag fee
    bag_fee_sum = bags * bagfee
    
    #Final price with tax 
    price = city_price + class_price + bag_fee_sum
    
    final_price = round(price * 1.13, 2)
    
    twodecimalprice = format(final_price, ".2f") #Make $ in two decimal places
    
    #Update final cost label
    pricelbl.config(text=f"Your total price is: ${twodecimalprice}")

#City ComboBox
citycombo = Combobox(tab3)
citycombo['values'] = cities
citycombo.set('Select a City')
citycombo.place(relx=0.18, rely=0.3, anchor=CENTER)

#Class ComboBox
classcombo = Combobox(tab3)
classcombo['values'] = class_box
classcombo.set('Select a Class')
classcombo.place(relx=0.49, rely=0.3, anchor=CENTER)

#Bags ComboBox
bagcombo = Combobox(tab3)
bagcombo['values'] = bags
bagcombo.set('Select number of Bags')
bagcombo.place(relx=0.8, rely=0.3, anchor=CENTER)

#Labels
   #Tab 1 Title 
lbl_title = Label(tab1, text = "Air Ontario", font = ("Times", 70), \
                  bg=bg_colour,fg = "#8B0000")
lbl_title.config(borderwidth=0, relief="groove", padx=10, pady=10)
lbl_title.place(relx=0.5, rely=0.3, anchor=CENTER)

    #Text in Tab 1
lbl_title = Label(tab1, text = "Thank you for choosing Air Ontario.", font = ("Times", 20),\
                  bg=bg_colour,fg = "#8B0000")
lbl_title.config(borderwidth=0, relief="groove", padx=10, pady=10)
lbl_title.place(relx=0.5, rely=0.5, anchor=CENTER)

   #Title for tab 3
title2 = Label(tab3, text = "Air Ontario", font = ("Times", 40), \
                  bg=bg_colour,fg = "#8B0000")
title2.place(relx=0.5, rely=0.1, anchor=CENTER)

    #Price label
pricelbl = Label(tab3, text="Your total price is $0", font = ("Times", 20), \
                  bg=bg_colour,fg = "#8B0000")
pricelbl.place(relx=0.5, rely=0.5, anchor=CENTER)

    #Thank you label
thankslbl = Label(tab3, text="Thank you for choosing Air Ontario", \
                  font = ("Times", 20), bg=bg_colour,fg = "#8B0000")
thankslbl.place(relx=0.5, rely=0.9, anchor=CENTER)

#Buttons
    #Button to switch to tab 2
def clicked():
    my_notebook.select(tab2)
    
bttn = Button(tab1, text="View Flights for July 7 2024", command=clicked)
bttn.place(relx=0.5, rely=0.7, anchor=CENTER)

    #Button to switch to tab 3
def clicked1():
    my_notebook.select(tab3)
bttn1 = Button(tab2, text="Buy Ticket", command=clicked1)
bttn1.grid(row=len(flight_info), column=0, columnspan=len(flight_info[0]), pady=10)

    #Calculate price button
calculate_price = Button(tab3, text="Calculate Price", command = total)
calculate_price.place(relx=0.5, rely=0.4, anchor=CENTER)

#Images
airhostess_img = PhotoImage(file = 'pics Small.png')
lbl_airhostess = Label(tab1, image = airhostess_img)
lbl_airhostess.place(relx = 0.15, rely = 0.37, anchor=CENTER)

plane_img = PhotoImage(file = 'planepic.png')
lbl_plane = Label(tab1, image = plane_img)
lbl_plane.place(relx = 0.85, rely = 0.35, anchor=CENTER)

airplane_img = PhotoImage(file = 'airplane.png')
lbl_airhostess = Label(tab3, image = airplane_img)
lbl_airhostess.place(relx = 0.5, rely = 0.7, anchor=CENTER)

#Mainloop
window.mainloop()