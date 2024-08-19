from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication

app = QApplication([])

from main_widnow import *
from menu_window import *
from time import*

class Question():
    def __init__(self,question,answer,wrong_ans1,wrong_ans2,wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
        self.is_Check = False
        self.count_answer=0
        self.count_right_answers=0

    def got_right(self):
        self.count_answer += 1
        self.count_right_answers += 1

    def got_wrong(self):
        self.count_answer += 1

question1=Question('Яблуко','apple','penaple','application','caterpillar')
question2=Question("М'яч",'bread','ball','perdon','book')
question3=Question('Будинок','house','sergion','break','pool')
question4=Question('Корабель','sea','sergion','shep','pool')


question=[question1,question2,question3,question4]

radio_list=[rb_ans1,rb_ans2,rb_ans3,rb_ans4]
shuffle(radio_list)

def new_question():
    global current_question
    current_question=choice(question)
    lb_question.setText(current_question.question)
    radio_list[0].setText(current_question.answer)
    radio_list[1].setText(current_question.wrong_ans1)
    radio_list[2].setText(current_question.wrong_ans2)
    radio_list[3].setText(current_question.wrong_ans3)
    current_question.is_Check=False
    current_question.count_answer=0
    current_question.count_right_answers=0
    gb_answer.hide()
    gb_question.show()

new_question()

def rest():
    seconds=sp_rest.value()
    window.hide()
    sleep(seconds*60)
    window.show()

btn_rest.clicked.connect(rest)









window.show()
app.exec_()