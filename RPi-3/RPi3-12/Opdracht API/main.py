import getquestion
import gui

while True:

    question, answer = getquestion.get_question()
    print("question =", question, "The answer=", answer)
    gui.handle_question(question, answer)