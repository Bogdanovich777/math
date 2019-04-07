import random
import sys
import time
import webbrowser

from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QCloseEvent
from PySide2 import QtCore

from go import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)

        self.setupUi(self)
        a = self.pushButton.clicked.connect(self.checkb1)
        b = self.pushButton_2.clicked.connect(self.checkb2)
        c = self.pushButton_3.clicked.connect(self.checkb3)
        d = self.pushButton_4.clicked.connect(self.checkb4)

    def checkb1(self):
        res1 = self.pushButton.text()
        res2 = self.pushButton_2.text()
        res3 = self.pushButton_3.text()
        res4 = self.pushButton_4.text()
        r = self.textEdit.toPlainText()
        if len(r) > 0:
            g = r.split(' ')
            point1 = int(g[0])
            point2 = int(g[2])
            if g[1] == '-':
                if g[1] == '-':
                    if point1 - point2 == int(res1):
                        self.pushButton.setStyleSheet('background-color: lightgreen')
                        self.progressBar.setValue(self.progress())
                        self.final()
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res2):
                        self.pushButton_2.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res3):
                        self.pushButton_3.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res4):
                        self.pushButton_4.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
            else:
                if point1 + point2 == int(res1):
                    self.pushButton.setStyleSheet('background-color: lightgreen')
                    self.progressBar.setValue(self.progress())
                    self.final()
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res2):
                    self.pushButton_2.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res3):
                    self.pushButton_3.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res4):
                    self.pushButton_4.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
        else:
            self.__new_example()

    def checkb2(self):
        res1 = self.pushButton.text()
        res2 = self.pushButton_2.text()
        res3 = self.pushButton_3.text()
        res4 = self.pushButton_4.text()
        r = self.textEdit.toPlainText()
        if len(r) > 0:
            g = r.split(' ')
            point1 = int(g[0])
            point2 = int(g[2])
            if g[1] == '-':
                if g[1] == '-':
                    if point1 - point2 == int(res1):
                        self.pushButton.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res2):
                        self.pushButton_2.setStyleSheet('background-color: lightgreen')
                        self.progressBar.setValue(self.progress())
                        self.final()
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res3):
                        self.pushButton_3.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res4):
                        self.pushButton_4.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
            else:
                if point1 + point2 == int(res1):
                    self.pushButton.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res2):
                    self.pushButton_2.setStyleSheet('background-color: lightgreen')
                    self.progressBar.setValue(self.progress())
                    self.final()
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res3):
                    self.pushButton_3.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res4):
                    self.pushButton_4.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
        else:
            self.__new_example()

    def checkb3(self):
        res1 = self.pushButton.text()
        res2 = self.pushButton_2.text()
        res3 = self.pushButton_3.text()
        res4 = self.pushButton_4.text()
        r = self.textEdit.toPlainText()
        if len(r) > 0:
            g = r.split(' ')
            point1 = int(g[0])
            point2 = int(g[2])
            if g[1] == '-':
                if g[1] == '-':
                    if point1 - point2 == int(res1):
                        self.pushButton.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res2):
                        self.pushButton_2.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res3):
                        self.pushButton_3.setStyleSheet('background-color: lightgreen')
                        self.progressBar.setValue(self.progress())
                        self.final()
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res4):
                        self.pushButton_4.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
            else:
                if point1 + point2 == int(res1):
                    self.pushButton.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res2):
                    self.pushButton_2.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res3):
                    self.pushButton_3.setStyleSheet('background-color: lightgreen')
                    self.progressBar.setValue(self.progress())
                    self.final()
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res4):
                    self.pushButton_4.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
        else:
            self.__new_example()

    def checkb4(self):
        res1 = self.pushButton.text()
        res2 = self.pushButton_2.text()
        res3 = self.pushButton_3.text()
        res4 = self.pushButton_4.text()
        r = self.textEdit.toPlainText()
        if len(r) > 0:
            g = r.split(' ')
            point1 = int(g[0])
            point2 = int(g[2])
            if g[1] == '-':
                if g[1] == '-':
                    if point1 - point2 == int(res1):
                        self.pushButton.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res2):
                        self.pushButton_2.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res3):
                        self.pushButton_3.setStyleSheet('background-color: lightgreen')
                        self.progressBar2.setValue(self.progress2())
                        time.sleep(0.5)
                        self.__new_example()
                    elif point1 - point2 == int(res4):
                        self.pushButton_4.setStyleSheet('background-color: lightgreen')
                        self.progressBar.setValue(self.progress())
                        self.final()
                        time.sleep(0.5)
                        self.__new_example()
            else:
                if point1 + point2 == int(res1):
                    self.pushButton.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res2):
                    self.pushButton_2.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res3):
                    self.pushButton_3.setStyleSheet('background-color: lightgreen')
                    self.progressBar2.setValue(self.progress2())
                    time.sleep(0.5)
                    self.__new_example()
                elif point1 + point2 == int(res4):
                    self.pushButton_4.setStyleSheet('background-color: lightgreen')
                    self.progressBar.setValue(self.progress())
                    self.final()
                    time.sleep(0.5)
        else:
            self.__new_example()

    def __new_example(self):
        example = self.total()
        self.text_new(example=example)
        answer = self.answer(example=example)
        self.set_default()
        self.pushButton.setText(str(answer['1']))
        self.pushButton_2.setText(str(answer['2']))
        self.pushButton_3.setText(str(answer['3']))
        self.pushButton_4.setText(str(answer['4']))

    def set_default(self):
        self.pushButton.setStyleSheet("")
        self.pushButton.setStyleSheet("QPushButton:pressed { background-color: yellow }")
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setStyleSheet("QPushButton:pressed { background-color: yellow }")
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setStyleSheet("QPushButton:pressed { background-color: yellow }")
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setStyleSheet("QPushButton:pressed { background-color: yellow }")

    def progress(self):
        start = self.progressBar.text()
        g = start.split('%')
        count = int(g[0])
        count += 10
        return count

    def progress2(self):
        start = self.progressBar2.text()
        g = start.split('%')
        count = int(g[0])
        count += 10
        return count

    def final(self):
        first = self.progressBar.text()
        g = first.split('%')
        count = int(g[0])
        if count == 20:
            webbrowser.open("https://drasler.ru/wp-content/uploads/2018/04/%D0%9A%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%"
                            "D0%B8-%D0%BD%D0%B0-%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9-%D1%81%D1%82%D0%BE%D0"
                            "%BB-windows-7-%D1%81%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C-%D0%BA%D1%80%D0%B0%D1%81%"
                            "D0%B8%D0%B2%D1%8B%D0%B5-%D0%B8-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%BD%D1%8B%D0%B5-14.jpg")
            sys.exit()

    def text_new(self, example):
        self.textEdit.setText(example['1'])
        self.textEdit.update()
        time.sleep(0.3)

    def answer(self, example):
        answer2 = int(example['2']) + 1
        answer3 = int(example['2']) + 2
        answer4 = int(example['2']) - 1
        answer1 = int(example['2'])

        ans = [answer1, answer2, answer3, answer4]

        button1 = random.choice(ans)
        ans.pop(ans.index(button1))
        button2 = random.choice(ans)
        ans.pop(ans.index(button2))

        button3 = random.choice(ans)
        ans.pop(ans.index(button3))

        button4 = random.choice(ans)
        ans.pop(ans.index(button4))

        return {'1': button1,
                '2': button2,
                '3': button3,
                '4': button4}

    def total(self):
        a = random.randint(1, 10)
        b = random.randint(1, a)
        c = ('+', '-')
        operate = random.choice(c)
        if operate == '-':
            answer = a - b
        else:
            answer = a + b
        text = str(a) + ' ' + operate + ' ' + str(b)
        total = {'1': text,
                 '2': answer}
        return total


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    Ui_MainWindow()
    main.show()
    sys.exit(app.exec_())

main()