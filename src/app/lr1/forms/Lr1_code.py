from PyQt5 import QtWidgets
from src.app.lr1.desing.Lr1 import Ui_MainWindow
from src.app.lr1.desing.Ru import Ui_Ru_lang
from src.app.lr1.desing.two_windows import Ui_alf_two
import sys
import math


class Mywindow(QtWidgets.QMainWindow):
    var_klav = 0
    N_f = 0
    i = 0
    ru_alf = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    eng_alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cvoi_alf = []
    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_win.clicked.connect(self.show_ru)
        self.ui.reshenie.clicked.connect(self.find)
        self.ui.pokasform.clicked.connect(self.formul)
        self.ui.new_alf.clicked.connect(self.show_new_alf)


    def show_ru(self):
        self.ru = Ri_Win()

    def show_new_alf(self):
        self.alf = New_lang()

    def find(self):
        self.N_f = 0
        text = self.ui.textfor.toPlainText()
        if self.var_klav == 3:
            self.i = math.log2(len(self.ru_alf))
            self.ui.findN.setText("N = " + str(len(self.ru_alf)))
            self.ui.findi.setText(" i = " + str(self.i))
            for item in text:
                if item in self.ru_alf:
                    self.N_f += 1

        if self.var_klav == 2:
            self.i = math.log2(len(self.eng_alf))
            self.ui.findN.setText("N = " + str(len(self.eng_alf)))
            self.ui.findi.setText(" i = " + str(self.i))
            for item in text:
                if item in self.eng_alf:
                    self.N_f += 1

        if self.var_klav == 4:
            self.i = math.log2(len(self.cvoi_alf))
            self.ui.findN.setText("N = " + str(len(self.cvoi_alf)))
            self.ui.findi.setText(" i = " + str(self.i))
            for item in text:
                if item in self.cvoi_alf:
                    self.N_f += 1

        self.ui.findI.setText(" I = " + str(self.N_f * self.i))
        self.ui.fi_N.setText("")
        self.ui.fi_i.setText("")
        self.ui.fi_I.setText("")
    def formul(self):
        self.ui.fi_N.setText("N = len(alphabet)")
        if self.var_klav == 3:
            self.ui.fi_i.setText("i = Log2(" + str(len(self.ru_alf)) + ")")
        if self.var_klav == 2:
            self.ui.fi_i.setText("i = Log2(" + str(len(self.eng_alf)) + ")")
        if self.var_klav == 4:
            self.ui.fi_i.setText("i = Log2(" + str(len(self.cvoi_alf)) + ")")
        self.ui.fi_I.setText(" I = " + str(self.N_f) + "*" + str(self.i))

    def number_of_letters(self, number, vibor_kl):
        self.ui.character.setText(str(number))
        self.var_klav = vibor_kl

    def language_selection(self):
        self.ui.Ru_btn.clicked.connect(lambda: self.number_of_letters(len(self.ru_alf), 3))
        self.ui.English_btn.clicked.connect(lambda: self.number_of_letters(len(self.eng_alf), 2))
        self.ui.alf_alf.clicked.connect(self.for_new_alf)

    def for_new_alf(self):
        self.var_klav = 4
        f = open('alfavit.txt')
        open_file = f.read()
        self.cvoi_alf = open_file.split()
        self.number_of_letters(len(self.cvoi_alf), 4)
        f.close()


class Ri_Win(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ri_Win, self).__init__()
        self.ru = Ui_Ru_lang()
        self.ru.setupUi(self)
        self.show()
        self.zadachi()

    def zadachi(self):
        self.ru.pushButton_2.clicked.connect(lambda: self.otv(1))
        self.ru.pushButton_3.clicked.connect(lambda: self.otv(2))
        self.ru.pushButton_8.clicked.connect(lambda: self.otv(3))
        self.ru.pushButton_10.clicked.connect(lambda: self.otv(4))
        self.ru.pushButton_4.clicked.connect(lambda: self.otv(5))
        self.ru.pushButton_5.clicked.connect(lambda: self.otv(6))
        self.ru.pushButton_6.clicked.connect(lambda: self.otv(7))
        self.ru.pushButton_7.clicked.connect(lambda: self.otv(8))
        self.ru.pushButton_9.clicked.connect(lambda: self.otv(9))
        self.ru.pushButton.clicked.connect(lambda: self.otv(10))

    def otv(self, num):
        if num == 1:
            self.ru.no1.setText(str(7 * 70) + " бит")
        if num == 2:
            self.ru.no2.setText(str(7 * 60) + " бит")
        if num == 3:
            self.ru.no3.setText(str(4 * 150) + " бит")
        if num == 4:
            self.ru.no4.setText(str(7 * 80) + " бит")
        if num == 5:
            self.ru.no5.setText(str(30 * 10 * 2) + " бит")
        if num == 6:
            self.ru.no6.setText("i = log3(18)=2.63093 or i = 3")
        if num == 7:
            self.ru.no7.setText(str(pow(2, 4) + pow(2, 5)))
        if num == 8:
            self.ru.no8.setText(str(pow(3, 4) + pow(3, 3)))
        if num == 9:
            self.ru.no9.setText(str(pow(3,5))+ "<" + str(pow(4,5))+ " n = 5")
        if num == 10:
            self.ru.no10.setText("n=5")

class New_lang(QtWidgets.QMainWindow):
    def __init__(self):
        super(New_lang, self).__init__()
        self.ui_alf = Ui_alf_two()
        self.ui_alf.setupUi(self)
        self.show()
        self.open_alf()
        self.ui_alf.add_btn.clicked.connect(self.write_alf)
        self.ui_alf.clean_btn.clicked.connect(self.clean_al)

    def open_alf(self):
        f = open('alfavit.txt')
        open_file = f.read()
        self.ui_alf.textforalf.setText(open_file)
        f.close()

    def write_alf(self):
        text = self.ui_alf.textforalf.toPlainText()
        file = open('alfavit.txt', 'w')
        file.write(text)
        file.close()

    def clean_al(self):
        self.ui_alf.textforalf.setText("")
        file = open('alfavit.txt', 'w')
        file.write("")
        file.close()

