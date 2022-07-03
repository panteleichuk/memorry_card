from PyQt5.QtWidgets import QTableWidgetItem
class Question:
    def __init__(self, questions, correct_answer, wrong1_answer, wrong2_answer, wrong3_answer):
        self.QUESTION = questions
        self.CORRECT_ANSWER = correct_answer
        self.WRONG1_ANSWER = wrong1_answer
        self.WRONG2_ANSWER = wrong2_answer
        self.WRONG3_ANSWER = wrong3_answer
        self.ATTEMPTS = 0
        self.CORRECT_ATTEMPT = 0
    def true_answer(self):
        self.ATTEMPTS += 1
        self.CORRECT_ATTEMPT += 1
    def false_answer(self):
        self.ATTEMPTS += 1
    def return_str(self):
        return f"{self.QUESTION}/{self.CORRECT_ANSWER}/{self.WRONG1_ANSWER}/{self.WRONG2_ANSWER}/{self.WRONG3_ANSWER}/{self.ATTEMPTS}/{self.CORRECT_ATTEMPT}/"


class Frame_Questions:
    def __init__(self, questions_info, questions, rbn1, rbn2, rbn3, rbn4 ):
        self.QUESTIONS_INFO = questions_info
        self.QUESTION = questions
        self.RBN1_answer = rbn1
        self.RBN2_wrong = rbn2
        self.RBN3_wrong = rbn3
        self.RBN4_wrong = rbn4

    def info_update(self, new_info):
        self.QUESTIONS_INFO = new_info

    def Showtext(self):
        self.QUESTION.setText(self.QUESTIONS_INFO.QUESTION)
        self.RBN1_answer.setText(self.QUESTIONS_INFO.CORRECT_ANSWER)
        self.RBN2_wrong.setText(self.QUESTIONS_INFO.WRONG1_ANSWER)
        self.RBN3_wrong.setText(self.QUESTIONS_INFO.WRONG2_ANSWER)
        self.RBN4_wrong.setText(self.QUESTIONS_INFO.WRONG3_ANSWER)

class Frame_Edit(Frame_Questions):
    def save_question(self):
        self.QUESTIONS_INFO.QUESTION = self.QUESTION.text()
        self.LIST_WIDGET.takeItem(self.LIST_WIDGET.count()-1)
        self.LIST_WIDGET.addItem( self.QUESTIONS_INFO.QUESTION )
        self.LIST_WIDGET.setCurrentRow(self.LIST_WIDGET.count())
    def save_answer(self):
        self.QUESTIONS_INFO.CORRECT_ANSWER = self.RBN1_answer.text()
    def save_wrong(self):
        self.QUESTIONS_INFO.WRONG1_ANSWER = self.RBN2_wrong.text()
        self.QUESTIONS_INFO.WRONG2_ANSWER = self.RBN3_wrong.text()
        self.QUESTIONS_INFO.WRONG3_ANSWER = self.RBN4_wrong.text()

    def connects(self):
        self.QUESTION.editingFinished.connect(self.save_question)
        self.RBN1_answer.editingFinished.connect(self.save_answer)
        self.RBN2_wrong.editingFinished.connect(self.save_wrong)
        self.RBN3_wrong.editingFinished.connect(self.save_wrong)
        self.RBN4_wrong.editingFinished.connect(self.save_wrong)
    def clear_fram(self):
        self.QUESTION.setText("")
        self.RBN1_answer.setText("")
        self.RBN2_wrong.setText("")
        self.RBN3_wrong.setText("")
        self.RBN4_wrong.setText("")

    def __init__(self, questions_info, edit_questions, edit_answer, edit_wrong1,edit_wrong2,edit_wrong3,list_widget ):
        super().__init__(questions_info, edit_questions, edit_answer, edit_wrong1,edit_wrong2,edit_wrong3)
        self.LIST_WIDGET = list_widget
        self.connects()
class Statistic:
    def __init__(self,all_question, table):
        self.ALL_QW = all_question
        self.TABLE = table
        self.TABLE.setColumnCount(3)
        
    def Showtext(self,all_qw):
        self.ALL_QW = all_qw
        self.TABLE.setRowCount(len(self.ALL_QW)+1)
        for i in range(len(self.ALL_QW)):
            item1 = QTableWidgetItem(self.ALL_QW[i].QUESTION)
            item2 = QTableWidgetItem(self.ALL_QW[i].ATTEMPTS)
            item3 = QTableWidgetItem(self.ALL_QW[i].CORRECT_ATTEMPT)
            self.TABLE.setItem(i,0,item1)
            self.TABLE.setItem(i,1,item2)
            self.TABLE.setItem(i,2,item3)
        self.TABLE.resizeColumnsToContents()
        self.TABLE.resizeRowsToContents()