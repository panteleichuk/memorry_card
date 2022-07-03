from PyQt5.QtCore import Qt
from memo_edit import*
from random import shuffle,choice
from memo___card_layout import*
from memo_data import*
from memo___app import app
from PyQt5.QtWidgets import QWidget, QTableWidget,QHBoxLayout
card_width, card_height = 600, 500
win_card = QWidget()
win_edit = QWidget()
win_sts = QWidget()
table = QTableWidget()
question_list = list()
frame = Frame_Questions(None, questions, rbn1, rbn2, rbn3, rbn4)
frame_edit = Frame_Edit(None, edit_question,edit_answer,edit_wrong1,edit_wrong2,edit_wrong3,list_question)
statistic = Statistic(question_list, table)
def creat_win_sts():
        win_card.hide()
        win_sts.resize(card_width,card_height)
        win_sts.setWindowTitle('Memory card')
        win_sts.move(0,0)
        line = QHBoxLayout()
        statistic.Showtext(question_list)
        
        line.addWidget(table)
        win_sts.setLayout(line)
        
        win_sts.show()
def add_qw():
    qw = Question('Яблуко', 'Apple', 'Aple', 'Aplle', 'Applle')
    question_list.append(qw)
    qw = Question('Собака', 'Dog', 'Dag', 'Sobaka', 'Gav')
    question_list.append(qw)
    qw = Question('Киця', 'Cat', 'Cot', 'Kat', 'Myu')
    question_list.append(qw)
    qw = Question('Дівчинка', 'Girl', 'Garl', 'Gil', 'Gilr')
    question_list.append(qw)
    qw = Question('Хлопчик', 'Boy', 'Bay', 'Bouy', 'Bou')
    question_list.append(qw)

def Random_Question():
    radio_list = [frame.RBN1_answer,frame.RBN2_wrong,frame.RBN3_wrong,frame.RBN4_wrong]
    shuffle(radio_list)
    frame.RBN1_answer = radio_list[0]
    frame.RBN2_wrong= radio_list[1]
    frame.RBN3_wrong = radio_list[2]
    frame.RBN4_wrong = radio_list[3]
    frame.info_update(choice(question_list))
    frame.Showtext()


def set_wincard():
    win_card.resize(card_width,card_height)
    win_card.setWindowTitle('Memory card')
    win_card.move(0,0)
    win_card.setLayout(layout_card)
    win_card.show()

def set_winedit():
    win_edit.resize(card_width,card_height)
    win_edit.setWindowTitle('Memory card')
    win_edit.move(0,0)
    win_edit.setLayout(main_edit_line)
  
def check_result():
    pass

    Random_Questions()
def click_ok():
    pass
def show_in_list():
    list_question.clear()
    for qw in question_list:
        list_question.addItem(qw.QUESTION)
def click_menu():
    win_card.hide()
    win_edit.show()
    show_in_list()

def show_qw(item):
    print(item.text())
    print((list_question.currentRow()))
    index = list_question.currentRow()
#   index = list_question.currentIndex().row()

    frame_edit.info_update(question_list[index])
    frame_edit.Showtext()
def click_back():
    win_card.show()
    win_edit.hide()
    Random_Question()
def click_del():
        index = list_question.currentRow()
        print(index)
        del question_list[index]
        # item = list_question.currentItem().text()
        # for el in question_list:
        #     if el.QUESTION == item:
        #             question_list.remove(el)
        frame_edit.clear_fram()
        show_in_list()
def click_new():
        question_list.append(Question("New question","Current answer","Wrong answer1","Wrong answer2","Wrong answer3"))
        list_question.addItem(question_list[-1].QUESTION)
        index = len(question_list) - 1
        list_question.setCurrentRow(index)
        show_qw(list_question.currentItem())

def sleep_card():
        win_card.hide()
        timer.setInterval(time_unit * box_Minutes.value() )
        timer.start()         
        data = data.split("/")
        print(data)
        read_list = list()
        for i in range(0,len(data)-1,7):
                read_list.append(Question(data[i],data[i+1],data[i+2],data[i+3],data[i+4]))
                index = len(read_list) -1
                read_list[index].ATTEMPTS = data[i+5]
                read_list[index].CORRECT_ATTEMPTS = data[i+6]
       

def connects():
        btn_menu.clicked.connect(click_menu)
        btn_ok.clicked.connect(click_ok)
        list_question.itemClicked.connect(show_qw)
        btn_back.clicked.connect(click_back)
        btn_delet.clicked.connect(click_del)
        btn_new.clicked.connect(click_new)
        btn_sts.clicked.connect(creat_win_sts)


add_qw()
Random_Question()
set_wincard()
set_winedit()
connects()
app.exec_()
write_file(question_list)