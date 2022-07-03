from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QWidget, QLabel, QPushButton, QRadioButton, 
       QVBoxLayout, QHBoxLayout, QSpinBox, QGroupBox,
       QButtonGroup
       )
from memo___app import app 


btn_menu = QPushButton('Menu')

btn_rest = QPushButton('Take a rest')

time_rest = QSpinBox()
time_rest.setValue(30)
label_rest = QLabel('minutes')

btn_ok = QPushButton('Answer question')
btn_sts = QPushButton("Statistic")

questions = QLabel('')    

frame1 = QGroupBox('Veriants of answers:')
btn_group = QButtonGroup()
rbn1 = QRadioButton('')
rbn2 = QRadioButton('')
rbn3 = QRadioButton('')
rbn4 = QRadioButton('')
btn_group.addButton(rbn1)
btn_group.addButton(rbn2)
btn_group.addButton(rbn3)
btn_group.addButton(rbn4)

frame2 = QGroupBox('Result:')
label_result = QLabel()
correct_answer = QLabel()

layout_card = QVBoxLayout()
LH1 = QHBoxLayout()
LH2 = QHBoxLayout()
LH3 = QHBoxLayout()
LH4 = QHBoxLayout()

LHF = QHBoxLayout()
LVF1 = QVBoxLayout()
LVF2 = QVBoxLayout()

LH1.addWidget(btn_menu)
LH1.addStretch(1)
LH1.addWidget(btn_sts)
LH1.addWidget(btn_rest)
LH1.addWidget(time_rest)
LH1.addWidget(label_rest)

LH2.addWidget(questions)

LH3.addWidget(frame1)
LH3.addWidget(frame2)

LH4.addWidget(btn_ok)

LVF1.addWidget(rbn1)
LVF1.addWidget(rbn2)

LVF2.addWidget(rbn3)
LVF2.addWidget(rbn4)

LHF.addLayout(LVF1)
LHF.addLayout(LVF2)

frame1.setLayout(LHF)

layout_card.addLayout(LH1)
layout_card.addLayout(LH2, stretch=2)
layout_card.addLayout(LH3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(LH4, stretch=2)
layout_card.addStretch(1)

layout_res = QVBoxLayout()
layout_res.addWidget(label_result, alignment = (Qt.AlignLeft| Qt.AlignTop))
layout_res.addWidget(correct_answer, alignment =Qt.AlignCenter, stretch=2)
frame2.setLayout(layout_res)
frame2.hide()

def show_result():
       frame2.show()
       frame1.hide()
       btn_ok.setText("Next")


def show_question():
       frame1.show()
       frame2.hide()
       btn_ok.setText("Ok")