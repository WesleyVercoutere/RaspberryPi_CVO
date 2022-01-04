'''
https://opentdb.com/api.php?amount=1&type=boolean

{
"response_code": 0,
"results": [
            {
            "category": "Entertainment: Board Games",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Snakes and Ladders was originally created in India?",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
            }
        ]
}
'''
import requests
import datetime
import html

def get_question():


    response = requests.get("https://opentdb.com/api.php?amount=1&type=boolean", timeout=5)

    my_dict =response.json()
    question = my_dict["results"][0]["question"]
    answer   = my_dict["results"][0]["correct_answer"]
    #print("question=",question)
    #print("answer=",answer)
    question_html_decoding = html.unescape(question)
    #print("question_html_decoding=",question_html_decoding)

    return question_html_decoding, answer



