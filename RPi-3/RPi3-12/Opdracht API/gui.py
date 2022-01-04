import tkinter as tk


def update_score(score):
    global your_score
    your_score.set(score) 
    print("your_score=",score)
    window.update()

def fct_button(par):
    global is_waiting_for_answer
    global the_answer
    global score
    print(par)
    is_waiting_for_answer = False
    if the_answer == par:
        score += 1
        update_score(score)
    else:
        score -= 1
        update_score(score)  

def handle_question(question, answer):
    global is_waiting_for_answer
    global the_answer 
    the_answer = answer
    is_waiting_for_answer = True
    your_question.set(question)
    while is_waiting_for_answer:
        window.update()      


window = tk.Tk()  # main window object
window.geometry('800x200')
window.title("Quiz")

your_question = tk.StringVar()
entry_question = tk.Entry(window, textvariable=your_question, width=125)
entry_question.place(x=20, y=50)

your_score = tk.StringVar()
entry_score = tk.Entry(window, textvariable=your_score)
entry_score.place(x=20, y=100)


button_juist = tk.Button(window, text="JUIST", width=10, command=lambda : fct_button("True")) 
button_juist.place(x=20,y=150)

button_fout = tk.Button(window, text="FOUT", width=10, command=lambda : fct_button("False")) 
button_fout.place(x=300,y=150)

score = 0
nr_of_questions = 0
is_waiting_for_answer = True
the_answer = ""

your_score.set(score)
window.update()









