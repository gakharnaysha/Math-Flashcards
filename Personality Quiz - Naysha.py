import tkinter as tk
from tkinter import messagebox



# Function to handle the quiz
def start_quiz():
    questions = [
        "Do you enjoy spending time alone?",
        "Do people usually tell you that you are a good listener?",
        "Do you tend to think before you speak?",
        "Are you energized by socializing?",
        "Is it easy for you to make friends?",
        "Do you often take the lead in group settings?",
        "Do you prefer to stay home instead of going out?",
        "Do you prefer solitary activities?",
        "Do you often initiate conversations with strangers?",
        "Do you prefer to be spontaneous \ninstead of planning out activities?",
        "Do you often need to recharge your 'social battery?'",
        "Do you volunteer to speak or present in front of groups?",
        "Do you like attending concerts, festivals, or public events?",
        "Do you usually find it easy to share \nyour thoughts and opinions with others?",
        "Do you feel restless or bored when you \nspend too much time alone?"
    ]

    question_count = 0
    introvert_count = 0
    extrovert_count = 0

    def ask_question(question_count, introvert_count, extrovert_count):
        if question_count < len(questions):
            question_label.config(text=questions[question_count])

            def record_response(response, question_count, introvert_count, extrovert_count):
                if response == "yes":
                    if question_count in [0, 1, 2, 6, 7, 10]:
                        introvert_count += 1
                    else:
                        extrovert_count += 1
                else:
                    if question_count in [0, 1, 2, 6, 7, 10]:
                        extrovert_count += 1
                    else:
                        introvert_count += 1

                ask_question(question_count + 1, introvert_count, extrovert_count)

            yes_button.config(command=lambda: record_response("yes", question_count, introvert_count, extrovert_count))
            no_button.config(command=lambda: record_response("no", question_count, introvert_count, extrovert_count))
        else:
            show_results(extrovert_count, introvert_count)

    def show_results(extrovert_count, introvert_count):
        extrovert_percent = round(extrovert_count / len(questions) * 100)
        introvert_percent = round(introvert_count / len(questions) * 100)

        if extrovert_percent >= 60:
            result = f"\nYou are {extrovert_percent}% extroverted and {introvert_percent}% introverted.\n\nYou are an extrovert! You thrive in social environments and are often seen as talkative or chatty. You enjoy being the centre of attention and are easily able to connect with others!"
        elif introvert_percent >= 60:
            result = f"\nYou are {extrovert_percent}% extroverted and {introvert_percent}% introverted.\n\nYou are an introvert! You love spending time alone and enjoy doing solitary activities. You prefer intimate and meaningful connections rather than small talk, and you often need time to regain energy after social interactions."
        else:
            result = f"\nYou are {extrovert_percent}% extroverted and {introvert_percent}% introverted.\n\nYou are an ambivert! You display qualities of both extroverts and introverts. You feel comfortable in social situations, and appreciate being alone as well. You can adapt to different situations depending on the context and your mood."

        messagebox.showinfo("Quiz Results", result)

    ask_question(0, introvert_count, extrovert_count)

colour = "#C8F4FD"

# Tkinter setup
window = tk.Tk()
window.title("Personality Quiz")
window.geometry("500x300")
window.configure(bg = colour)

# Introduction
intro_label = tk.Label(window, text="~~~ Welcome to Personality Quiz ~~~", \
                       font=("Times", 14), bg = colour)
intro_label.place(relx=0.5, rely=0.1, anchor="center")

instructions = tk.Label(window, text="Answer a series of questions to \
determine whether you \nare an extrovert, an introvert, or both!", \
                        font=("times", 13), bg = colour)
instructions.place(relx=0.5, rely=0.27, anchor="center")

start_btn = tk.Button(window, text="Start Quiz", command=start_quiz, font=("times", 12))
start_btn.place(relx=0.5, rely=0.5, anchor="center")

# Quiz question label
question_label = tk.Label(window, text="", font=("times", 12), bg = colour)
question_label.place(relx=0.5, rely=0.65, anchor="center")

# Yes and No buttons
yes_button = tk.Button(window, text="Yes", font=("times", 12))
yes_button.place(relx=0.3, rely=0.8, anchor="center")

no_button = tk.Button(window, text="No", font=("times", 12))
no_button.place(relx=0.7, rely=0.8, anchor="center")

window.mainloop()

