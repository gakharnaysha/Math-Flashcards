# Name: Naysha Gakhar, id: 869875
# Description:
#              With this prgram, the user can practice randomly generated math
#              questions. On the first page, they are provided with instructions
#              on how to play, and then they can pick the level of difficulty
#              they would like on the second page. They can choose between
#              levels 1-6, in which level 5 is negative numbers and level 6
#              is division. There is a stopwatch provided for the user to time
#              themselves as well as a reset button if they would like to begin
#              again. This program also counts the number of incorrect, correct,
#              and total number of questions and displays a picture according
#              to whether the answer was right or wrong. The user can also go
#              back to the second tab using the "Change leve" button to change
#              the difficulty. 

# Import from libraries 
from tkinter import *
from tkinter import ttk
from random import randint
from tkinter.ttk import Combobox
from tkinter import messagebox
import random
from tkinter import scrolledtext

# Variables for the stopwatch 
running = False # Whether it is running or not 
hours, minutes, seconds = 0, 0, 0

def start():
    global running
    # Ensure to focus the cursor if start button has been pressed
    txt.focus()
    if not running:
        update()
        running = True

def pause():
    global running
    if running:
        # Stops updating the time 
        stopwatch_label.after_cancel(update_time)
        running = False
        
# Stopwatch
# Update the time, ensure that 60s = 1 min
def update():
    global hours
    global minutes
    global seconds
    global update_time
    
# Increase time
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
# Format 
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    
# Update the label after 1000 ms (1 second)
    stopwatch_label.config(text = hours_string + ':' + minutes_string + ':' \
                           + seconds_string)
    update_time = stopwatch_label.after(1000, update)

# Random numbers for the flashcard integers
global rando
num_1 = randint(1, 3)
num_2 = randint(1, 3)
num_3 = randint(1, 6)
num_4 = randint(1, 6)
num_5 = randint(1, 9)
num_6 = randint(1, 9)
num_7 = randint(1, 12)
num_8 = randint(1, 12)
num_9 = randint(-12, 12)
num_10 = randint(-12, 12)

# Colour variable 
greenlight = "#3fd467" 

# Create main window
window = Tk()
window.title("Math Flashcards")
window.geometry('800x500')
window.configure(bg= greenlight)


# Reset Button - Update everything to go back to the way it was before 
def resetbutton():
    global cor
    global incor
    global ques
    global ans_response
    global running
    
# Ask user if they want to reset everything
    reset = messagebox.askquestion('Reset', 'Reset All?')
    
# Reset the screen if yes is chosen 
    if reset == 'yes':
        
# Make counter values 0 
        cor = 0
        incor = 0
        ques = 0
        
        correct_counter.config(text = cor)
        incorrect_counter.config(text = incor)
        questions_counter.config(text = ques)
        
# Delete answer response 
        ans_response.config(text = '')
        
# Delete the values in the scrolled text widget
        scroll.delete(0.0, END)
        
# The stopwatch returns to zero
        if running:
            stopwatch_label.after_cancel(update_time)
            running = False
        global hours, minutes, seconds
        hours, minutes, seconds = 0, 0, 0
        stopwatch_label.config(text = '00:00:00')
        
# Ensure the images go away when everything is reset 
        lbl_correctimg.config(image = '')
        lbl_wrongimg.config(image = '')
        
# Delete the integers in the entry box and ensure the entrybox is on focus 
        txt.delete(0, 'end')
        txt.focus()
    
# Initialize counters
cor = 0
incor = 0
ques = 0

# Defining Buttons
def clicked1():
    my_notebook.select(tab2)

def clicked2():
    my_notebook.select(tab3)

# Create three tabs 
my_notebook = ttk.Notebook(window)
my_notebook.pack(pady = 15)

tab1 = Frame(my_notebook, width = 800, height = 500)
tab2 = Frame(my_notebook, width = 800, height = 500)
tab3 = Frame(my_notebook, width = 800, height = 500)

tab1.pack(fill="both", expand = 1)
tab2.pack(fill="both", expand = 1)
tab3.pack(fill="both", expand = 1) 

my_notebook.add(tab1, text = "Instructions")
my_notebook.add(tab2, text = "Levels")
my_notebook.add(tab3, text = "Flashcards")

# Set background image for tab1
bg = PhotoImage(file = "background2.png")
my_label = Label(tab1, image = bg)
my_label.place(x = 0, y = 0)

# Add image
snow_img = PhotoImage(file = "snow-white.png")
lbl_snow = Label(tab1, image = snow_img) 

# Print the title of the game
lbl_title = Label(tab1, text = "Snow White's Math Magic", font = ("Times", 40),\
bg = "#3fd467", fg = "white")

lbl_title.config(borderwidth=5, relief="groove", padx=10, pady=10)

# Print instructions for the user
lbl_instruct = Label(tab1, text = "Choose a level of difficulty and answer \
the math questions\n given to you to best of your ability! Get \
the answers\n right to avoid receiving poisonous apples from \
The Evil Queen.\n If you’d like to challenge yourself, try using \
the stopwatch\n to see how fast you can answer the questions!", \
font = ("Times", 20), bg = greenlight, fg = "white")

lbl_instruct.config(borderwidth = 5, relief="groove", padx=10, pady=10)

# Make button to proceed to next tab
btn_cont = Button(tab1, text = "Continue", font = ("Times", 14), fg = "green", \
command = clicked1) 

# Make tab 2 with description of the levels
my_label = Label(tab2, image = bg)
my_label.place(x = 0, y = 0)

lbl_level = Label(tab2, text = "Level 1: Numbers between 1 - 3\n Level 2: \
Numbers between 1 - 6\n Level 3: Numbers between 1 - 9\n Level 4: Numbers \
between 1 - 12\n Level 5: Negative numbers\n Level 6: Numbers with division",
font = ("Times", 30), bg = "#3fd467", fg = "white")

lbl_level.config(borderwidth=5, relief="groove", padx=10, pady=10)

# Make button to go to game
btn_start = Button(tab2, text = "Go To Game!", font = ("Times", 20),
fg = "green", command = clicked2)

# Set background for tab 3
my_label = Label(tab3, image = bg)
my_label.place(x = 0, y = 0)

def math_number():
    global rando
    global res
    global sign
    global num_1 
    global num_2 
    global num_3 
    global num_4 
    global num_5 
    global num_6 
    global num_7 
    global num_8
    global num_9 
    global num_10
    global multi
    
# Random number ranges
    num_1 = randint(1, 3)
    num_2 = randint(1, 3)
    num_3 = randint(1, 6)
    num_4 = randint(1, 6)
    num_5 = randint(1, 9)
    num_6 = randint(1, 9)
    num_7 = randint(1, 12)
    num_8 = randint(1, 12)
    num_9 = randint(-12, 12)
    num_10 = randint(-12, 12)
    
# Define the levels according to number ranges 
        
    
# Create labels based on chosen level 
    lbl.configure(text=combo.get())
    if combo.get() == '1':
        lbl.configure(text=level_1())
        lbl.configure(text='')
    elif combo.get() == '2':
        lbl.configure(text=level_2())
        lbl.configure(text='')
    elif combo.get() == '3':
        lbl.configure(text=level_3())
        lbl.configure(text='')
    elif combo.get() == '4':
        lbl.configure(text=level_4())
        lbl.configure(text='')
    elif combo.get() == '5':
        lbl.configure(text=level_5())
        lbl.configure(text='')
    elif combo.get() == '6':
        lbl.configure(text=level_6())
        lbl.configure(text='')
    
# Update the signs 
    signs = ['+', '-', 'x']
    sign = random.choice(signs)
    sign_1.config(text=sign, font=('Times', 30))
    if combo.get() == '6':
        sign_1.config(text='/', font=('Times', 30))
    
# Calculate the answers based on the new sign 
# Division
    if combo.get() == '6':
        multi = num_7 * num_8
        res = multi // num_7
# Addition
    elif sign == '+' and combo.get() == '1':
        res = num_1 + num_2
    elif sign == '+' and combo.get() == '2':
        res = num_3 + num_4
    elif sign == '+' and combo.get() == '3':
        res = num_5 + num_6
    elif sign == '+' and combo.get() == '4':
        res = num_7 + num_8
    elif sign == '+' and combo.get() == '5':
        res = num_9 + num_10
# Subtraction
    elif sign == '-' and combo.get() == '1':
        res = num_1 - num_2
    elif sign == '-' and combo.get() == '2':
        res = num_3 - num_4
    elif sign == '-' and combo.get() == '3':
        res = num_5 - num_6
    elif sign == '-' and combo.get() == '4':
        res = num_7 - num_8
    elif sign == '-' and combo.get() == '5':
        res = num_9 - num_10
# Multiplication
    elif sign == 'x' and combo.get() == '1':
        res = num_1 * num_2
    elif sign == 'x' and combo.get() == '2':
        res = num_3 * num_4
    elif sign == 'x' and combo.get() == '3':
        res = num_5 * num_6
    elif sign == 'x' and combo.get() == '4':
        res = num_7 * num_8
    elif sign == 'x' and combo.get() == '5':
        res = num_9 * num_10

# Ensure the user's answers are correct
# Add correct answer and their answer to the scroll as well as increase
# Counters by 1 
def entry():
    global cor
    global incor
    global ques
    global response
    global ans_response
    global scroll
    global lbl_correctimg
    global lbl_wrongimg
    answer = txt.get()
    
# Display whether answer is correct or incorrect 
    if int(txt.get()) == res:
        response = 'You are right!'
        cor += 1
        ques += 1
        lbl_correctimg.config(image = correctimg)
        lbl_correctimg.lift()
        lbl_wrongimg.lower()  
    else:
        response = 'You are incorrect :( The answer is ' + str(res)
        incor += 1
        ques += 1
        lbl_wrongimg.config(image = wrongimg)
        lbl_wrongimg.lift()
        lbl_correctimg.lower() 
    
# Update corrent answer message 
    ans_response.config(text=response)
    
# Ensure that cursor goes back to entry box and there is nothing in there
    txt.delete(0, 'end')
    txt.focus()
    
# Update counters to ensure they are increasing accordingly 
    correct_counter.config(text = cor)
    incorrect_counter.config(text = incor)
    questions_counter.config(text = ques)
    
# Display the question, the right answer and the user's answer in the scroll
# widget so that they can look back on it later. 
    if combo.get() == '1':
        scroll.insert(INSERT, num_1)
        scroll.insert(INSERT, ' ')
        scroll.insert(INSERT, sign)
        scroll.insert(INSERT, ' ')
        scroll.insert(INSERT, num_2)
        scroll.insert(INSERT, ' = ')
        scroll.insert(INSERT, res)
        scroll.insert(INSERT, ', You answered: ')
        scroll.insert(INSERT, answer)
        scroll.insert(INSERT, '\n')
    elif combo.get() == '2':
        scroll.insert(INSERT, num_3)
        scroll.insert(INSERT, ' ')
        scroll.insert(INSERT, sign)
        scroll.insert(INSERT, ' ')
        scroll.insert(INSERT, num_4)
        scroll.insert(INSERT, ' = ')
        scroll.insert(INSERT, res)
        scroll.insert(INSERT, ', You answered: ')
        scroll.insert(INSERT, answer)
        scroll.insert(INSERT, '\n')
    elif combo.get() == '3':
        scroll.insert(INSERT, num_5)
        scroll.insert(INSERT, ' ')
        scroll.insert(INSERT, sign)
        scroll.insert(INSERT, ' ')
        scroll.insert(INSERT, num_6)
        scroll.insert(INSERT, ' = ')
        scroll.insert(INSERT, res)
        scroll.insert(INSERT, ', You answered: ')
        scroll.insert(INSERT, answer)
        scroll.insert(INSERT, '\n')
    elif combo.get() == '4':
        scroll.insert(INSERT, num_7)
        scroll.insert(INSERT, ' ')
        scroll.insert(INSERT, sign)
        scroll.insert(INSERT, ' ')
        scroll.insert(INSERT, num_8)
        scroll.insert(INSERT, ' = ')
        scroll.insert(INSERT, res)
        scroll.insert(INSERT, ', You answered: ')
        scroll.insert(INSERT, answer)
        scroll.insert(INSERT, '\n')
    elif combo.get() == '5':
        scroll.insert(INSERT, num_9)
        scroll.insert(INSERT, ' ')
        scroll.insert(INSERT, sign)
        scroll.insert(INSERT, ' ')
        scroll.insert(INSERT, num_10)
        scroll.insert(INSERT, ' = ')
        scroll.insert(INSERT, res)
        scroll.insert(INSERT, ', You answered: ')
        scroll.insert(INSERT, answer)
        scroll.insert(INSERT, '\n')
    elif combo.get() == '6':
        scroll.insert(INSERT, multi)
        scroll.insert(INSERT, ' / ')
        scroll.insert(INSERT, num_7)
        scroll.insert(INSERT, ' = ')
        scroll.insert(INSERT, res)
        scroll.insert(INSERT, ', You answered: ')
        scroll.insert(INSERT, answer)
        scroll.insert(INSERT, '\n')
    
    math_number()

# Update the integers to the level that was chosen first 
def level_1():
    int_1.config(text=num_1, font=('Times', 30))
    int_2.config(text=num_2, font=('Times', 30))

def level_2():
    int_1.config(text=num_3, font=('Times', 30))
    int_2.config(text=num_4, font=('Times', 30))

def level_3():
    int_1.config(text=num_5, font=('Times', 30))
    int_2.config(text=num_6, font=('Times', 30))
    
def level_4():
    int_1.config(text=num_7, font=('Times', 30))
    int_2.config(text=num_8, font=('Times', 30))

def level_5():
    int_1.config(text=num_9, font=('Times', 30))
    int_2.config(text=num_10, font=('Times', 30))

def level_6():
    global multi
    multi = num_7 * num_8
    int_1.config(text=multi, font=('Times', 30))
    int_2.config(text=num_7, font=('Times', 30))

# Command for combobox - To choose level of difficulty 
def clicked(event):
    global res
    global sign
    
# Focus to entry box after combobox has been used 
    txt.focus()
    
# Randomzie integers based on level 
    lbl.configure(text=combo.get())
    if combo.get() == '1':
        lbl.configure(text=level_1())
        lbl.configure(text='')
    elif combo.get() == '2':
        lbl.configure(text=level_2())
        lbl.configure(text='')
    elif combo.get() == '3':
        lbl.configure(text=level_3())
        lbl.configure(text='')
    elif combo.get() == '4':
        lbl.configure(text=level_4())
        lbl.configure(text='')
    elif combo.get() == '5':
        lbl.configure(text=level_5())
        lbl.configure(text='')
    elif combo.get() == '6':
        lbl.configure(text=level_6())
        lbl.configure(text='')
      
# Randomize the operators 
    signs = ['+', '-', 'x']
    sign = random.choice(signs)
    sign_1.config(text=sign, font=('Times', 30))
    if combo.get() == '6':
        sign_1.config(text='/', font=('Times', 30))
    
# Calculate the correct answers
# Division
    if combo.get() == '6':
        multi = num_7 * num_8
        res = multi // num_7
# Addition
    elif sign == '+' and combo.get() == '1':
        res = num_1 + num_2
    elif sign == '+' and combo.get() == '2':
        res = num_3 + num_4
    elif sign == '+' and combo.get() == '3':
        res = num_5 + num_6
    elif sign == '+' and combo.get() == '4':
        res = num_7 + num_8
    elif sign == '+' and combo.get() == '5':
        res = num_9 + num_10
# Subtraction
    elif sign == '-' and combo.get() == '1':
        res = num_1 - num_2
    elif sign == '-' and combo.get() == '2':
        res = num_3 - num_4
    elif sign == '-' and combo.get() == '3':
        res = num_5 - num_6
    elif sign == '-' and combo.get() == '4':
        res = num_7 - num_8
    elif sign == '-' and combo.get() == '5':
        res = num_9 - num_10
# Multiplication
    elif sign == 'x' and combo.get() == '1':
        res = num_1 * num_2
    elif sign == 'x' and combo.get() == '2':
        res = num_3 * num_4
    elif sign == 'x' and combo.get() == '3':
        res = num_5 * num_6
    elif sign == 'x' and combo.get() == '4':
        res = num_7 * num_8
    elif sign == 'x' and combo.get() == '5':
        res = num_9 * num_10

# Main Program 

# Labels for integers - Configure '?'
int_1 = Label(tab3)
int_2 = Label(tab3) 

int_1.config(text='?', font=('Times', 70), bg = greenlight, fg = "white", \
borderwidth=5, relief="groove", padx=10, pady=10)
int_2.config(text='?', font=('Times', 70), bg = greenlight, fg = "white", \
borderwidth=5, relief="groove", padx=10, pady=10)

# Label for the math operator 
sign_1 = Label(tab3)

# Configure '?'
sign_1.config(text='?', font=('Times', 70), bg = greenlight, fg = "white", \
borderwidth=5, relief="groove", padx=10, pady=10)

# Label for answer response 
ans_response = Label(tab3, text ='', font=('Times', 15), bg = greenlight, \
fg = "white")  

# Labels for counters
# Correct 
correct = Label(tab3, text='Correct: ', font=('Times', 15), \
bg = greenlight, fg = "white", borderwidth=5, relief="groove", padx=7, pady=7)
correct_counter = Label(tab3, text = cor, font=('Times', 15), \
bg = greenlight, fg = "white", borderwidth=5, relief="groove", padx=7, pady=7)

# Incorrect 
incorrect = Label(tab3, text='Incorrect: ', font=('Times', 15), \
bg = greenlight, fg = "white", borderwidth=5, relief="groove", padx=7, pady=7)
incorrect_counter = Label(tab3, text = incor, font=('Times', 15), \
bg = greenlight, fg = "white", borderwidth=5, relief="groove", padx=7, pady=7)

# Total Questions 
questions = Label(tab3, text='Questions: ', font=('Times', 15), \
bg = greenlight, fg = "white", borderwidth=5, relief="groove", padx=7, pady=7)
questions_counter = Label(tab3, text = ques, font=('Times', 15), \
bg = greenlight, fg = "white", borderwidth=5, relief="groove", padx=7, pady=7)

# Title for scrolled widget
label_scrl = Label(tab3, text = 'Previous Questions', font=('Times', \
14), bg = greenlight, fg = "white")

# Make combobox
combo = Combobox(tab2)
combo['values'] = ['1', '2', '3', '4', '5', '6']
combo.set('Select a Level')

# Replace question marks with integers
lbl = Label(window, bg='green') 
lbl.pack()
combo['state'] = 'readonly'
combo.bind('<<ComboboxSelected>>', clicked)

# Ensure cursor is at entry box 
txt = Entry(tab3, width=10)

# Button to check answer 
btn = Button(tab3, text='Check', fg = 'green', \
command = entry)

# Change level
btn_change = Button(tab3, text='Change level', fg = 'green', \
command = clicked1)

# Reset button 
reset = Button(tab3, text="Reset All", fg = 'green', \
highlightthickness = 0, command=resetbutton)

# Stopwatch label 
stopwatch_label = Label(tab3, text = '00:00:00', font = ('Times', 20),\
bg = greenlight, fg = 'white')

# Make start button 
start_button = Button(tab3, text = 'Start Stopwatch', fg = 'green', \
highlightthickness = 0, command = start)

# Pause button 
pause_button = Button(tab3, text = 'Pause Stopwatch', fg = 'green', \
highlightthickness = 0, command = pause)

# Create scrolled text widget 
scroll = scrolledtext.ScrolledText(tab3, width = 40, height = 10)

# Images
wrongimg = PhotoImage(file = 'evil queen apple.png')
correctimg = PhotoImage(file = 'happysnow Small.png')
lbl_correctimg = Label(tab3)
lbl_wrongimg = Label(tab3)

# Placement
lbl_title.place(relx=0.5, rely=0.2, anchor=CENTER)
lbl_instruct.place(relx = 0.5, rely = 0.5, anchor=CENTER)
btn_cont.place(relx = 0.5, rely = 0.8, anchor=CENTER)
lbl_snow.place(relx = 0.8, rely = 0.85, anchor=CENTER)

btn_start.place(relx = 0.5, rely = 0.9, anchor=CENTER)
lbl_level.place(relx=0.5, rely=0.4, anchor=CENTER)

int_1.place(relx = 0.3, rely = 0.2, anchor=CENTER) 
int_2.place(relx = 0.7, rely = 0.2, anchor=CENTER)

sign_1.place(relx = 0.5, rely = 0.2, anchor=CENTER)
ans_response.place(relx = 0.5, rely = 0.5, anchor=CENTER)

correct.place(relx = 0.15, rely = 0.6, anchor=CENTER)
correct_counter.place(relx = 0.3, rely = 0.6, anchor=CENTER)

incorrect.place(relx = 0.15, rely = 0.75, anchor=CENTER)
incorrect_counter.place(relx = 0.3, rely = 0.75, anchor=CENTER)

questions.place(relx = 0.15, rely = 0.9, anchor=CENTER)
questions_counter.place(relx = 0.3, rely = 0.9, anchor=CENTER)

label_scrl.place(relx = 0.7, rely = 0.6, anchor=CENTER)
combo.place(relx = 0.5, rely = 0.8, anchor=CENTER)
txt.place(relx = 0.5, rely = 0.4, anchor=CENTER) 

btn.place(relx = 0.7, rely = 0.4, anchor=CENTER)
btn_change.place(relx = 0.9, rely = 0.2, anchor=CENTER)
reset.place(relx = 0.9, rely = 0.1, anchor=CENTER)

stopwatch_label.place(relx = 0.12, rely = 0.15, anchor=CENTER)
start_button.place(relx = 0.12, rely = 0.25, anchor=CENTER)
pause_button.place(relx = 0.12, rely = 0.35, anchor=CENTER)
scroll.place(relx = 0.7, rely = 0.8, anchor=CENTER)

lbl_correctimg.place(relx = 0.9, rely = 0.45, anchor=CENTER)
lbl_wrongimg.place(relx = 0.9, rely = 0.45, anchor=CENTER)

# Mainloop 
window.mainloop()
