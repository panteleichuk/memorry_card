from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QWidget, QLabel, QPushButton, QRadioButton, 
       QVBoxLayout, QHBoxLayout, QSpinBox, QGroupBox,
       QButtonGroup,QFormLayout,QListWidget,QLineEdit
       )
from memo___app import app 
#вікно-лист для списка питаннь 
list_question = QListWidget()
# панель з полями питання: 
# лайнедіт 5 шт - питання, 
edit_question = QLineEdit()
# 4 варфанта відповідей кнокпи:
edit_answer = QLineEdit()
edit_wrong1 = QLineEdit()
edit_wrong2 = QLineEdit()
edit_wrong3 = QLineEdit()
#  видалити,
btn_delet = QPushButton("Delet")
#  додати нове, 
btn_new = QPushButton("Add new qw")
# повернутись у меню
btn_back = QPushButton("Back train")

#лайоти: головний лайот V для всього вікна 
main_edit_line = QVBoxLayout()
# формлайто для едітів 
form_line = QFormLayout()
# лайот г для обєднання листа та форми
lineH_1 = QHBoxLayout()
# лайот г для видалити та додати 
lineH_2 = QHBoxLayout()
# лайот г для назад
lineH_3 = QHBoxLayout()


form_line.addRow("Question: ",edit_question)
form_line.addRow("Answer: ",edit_answer)
form_line.addRow("Wrong1: ",edit_wrong1)
form_line.addRow("Wrong2: ",edit_wrong2)
form_line.addRow("Wrong3: ",edit_wrong3)

lineH_1.addWidget(list_question)
lineH_1.addLayout(form_line)

lineH_2.addWidget(btn_delet)
lineH_2.addWidget(btn_new)

lineH_3.addWidget(btn_back)

main_edit_line.addLayout(lineH_1)
main_edit_line.addLayout(lineH_2)
main_edit_line.addLayout(lineH_3)