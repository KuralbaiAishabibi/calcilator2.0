import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic

class UI(QWidget):
    def __init__(self):
        self.start()
        self.set()
        
    def start(self):
        self.ui = uic.loadUi('calculator.ui')
        self.ui.show()
        
    def set(self):
        self.ui.pushButton_18.clicked.connect(lambda: self.click(num=0))
        self.ui.pushButton_10.clicked.connect(lambda: self.click(num=1))
        self.ui.pushButton_11.clicked.connect(lambda: self.click(num=2))
        self.ui.pushButton_13.clicked.connect(lambda: self.click(num=3))
        self.ui.pushButton_14.clicked.connect(lambda: self.click(num=4))
        self.ui.pushButton_15.clicked.connect(lambda: self.click(num=5))
        self.ui.pushButton_16.clicked.connect(lambda: self.click(num=6))
        self.ui.pushButton_21.clicked.connect(lambda: self.click(num=7))
        self.ui.pushButton_19.clicked.connect(lambda: self.click(num=8))
        self.ui.pushButton_20.clicked.connect(lambda: self.click(num=9))
#знаки
        self.ui.pushButton_4.clicked.connect(lambda: self.click_equation('/'))
        self.ui.pushButton_5.clicked.connect(lambda: self.click_equation('+'))
        self.ui.pushButton_6.clicked.connect(lambda: self.click_equation('-'))
        self.ui.pushButton_7.clicked.connect(lambda: self.click_equation('*'))
        self.ui.pushButton_17.clicked.connect(lambda: self.click('.'))
#знаки с функциями
        self.ui.pushButton_8.clicked.connect(lambda: self.answer())
        self.ui.pushButton_3.clicked.connect(lambda: self.back())
        self.ui.pushButton_2.clicked.connect(lambda: self.minus_2())
        self.ui.pushButton.clicked.connect(lambda: self.delete())

#улучшенная версия :_)
    def click_equation(self, num):
        global answer1
        self.display(num)
        answer1 = self.ui.label.text()
        self.ui.label.setText('0')

    
#знаки
    def answer(self):
        answer2 = answer1 + self.ui.label.text()
        if '/0' in answer2:
            self.ui.label.setText('ERROR')
        else:
            answer2 = str(eval(answer2))
            self.ui.label.setText(answer2)

    def back(self):
        x = self.ui.label.text()
        x = x[:-1]
        self.ui.label.setText(x)
        
    def minus_2(self):
        m = self.ui.label.text()
        m_1 = eval(m)
        m_1 = m_1**0.5
        self.ui.label.setText(str(m_1))
        
    def delete(self):
        d = self.ui.label.text()
        d = '0'
        self.ui.label.setText(d)
#цифры
    
    def click(self, num = 0):
        self.display(text=num)

    def display(self, text ='0'):
        old_text=self.ui.label.text()
        if old_text == '0':
            old_text=''

        new_text = old_text + str(text)
        self.ui.label.setText(new_text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    uiWindow = UI()
    app.exec_()
