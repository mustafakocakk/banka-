# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import re,random
import psycopg2
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from banka import Ui_Form
class deneme(object):
    def __init__(self):
        
        self.tc=""
        try:
            self.con = psycopg2.connect("host='localhost' dbname='deneme' user='postgres' password='1234'")   
            self.cur = self.con.cursor()
        except :
            print("bağlantı hatası")
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(747, 627)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 270, 671, 231))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.setMail = QtWidgets.QLineEdit(self.groupBox_2)
        self.setMail.setGeometry(QtCore.QRect(500, 120, 113, 23))
        self.setMail.setObjectName("setMail")
        self.setPass = QtWidgets.QLineEdit(self.groupBox_2)
        self.setPass.setGeometry(QtCore.QRect(500, 40, 113, 23))
        self.setPass.setObjectName("setPass")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(360, 40, 65, 15))
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(364, 120, 41, 21))
        self.label_6.setObjectName("label_6")
        self.setPassAgain = QtWidgets.QLineEdit(self.groupBox_2)
        self.setPassAgain.setGeometry(QtCore.QRect(500, 80, 113, 23))
        self.setPassAgain.setObjectName("setPassAgain")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 81, 16))
        self.label_4.setObjectName("label_4")
        self.setName = QtWidgets.QLineEdit(self.groupBox_2)
        self.setName.setGeometry(QtCore.QRect(140, 80, 113, 23))
        self.setName.setObjectName("setName")
        self.setTc = QtWidgets.QLineEdit(self.groupBox_2)
        self.setTc.setGeometry(QtCore.QRect(140, 40, 113, 23))
        self.setTc.setObjectName("setTc")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 65, 15))
        self.label_3.setObjectName("label_3")
        self.setTel = QtWidgets.QLineEdit(self.groupBox_2)
        self.setTel.setGeometry(QtCore.QRect(140, 120, 113, 23))
        self.setTel.setObjectName("setTel")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(360, 80, 101, 16))
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 120, 65, 15))
        self.label_5.setObjectName("label_5")
        
        self.setRegister = QtWidgets.QPushButton(self.groupBox_2)
        self.setRegister.setGeometry(QtCore.QRect(270, 180, 81, 23))
        self.setRegister.setObjectName("setRegister")
        self.setRegister.clicked.connect(self.userRegister)

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(130, 100, 411, 171))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.getPass = QtWidgets.QLineEdit(self.groupBox)
        self.getPass.setGeometry(QtCore.QRect(220, 70, 113, 23))
        self.getPass.setObjectName("getPass")
        
        self.login = QtWidgets.QPushButton(self.groupBox)
        self.login.setGeometry(QtCore.QRect(190, 120, 81, 23))
        self.login.setObjectName("login")
        self.login.clicked.connect(self.giris_yap)
        
        self.register_2 = QtWidgets.QPushButton(self.groupBox)
        self.register_2.setGeometry(QtCore.QRect(300, 120, 81, 23))
        self.register_2.setObjectName("register_2")
        self.register_2.clicked.connect(self.kayit)

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 65, 15))
        self.label_2.setObjectName("label_2")
        self.getTc = QtWidgets.QLineEdit(self.groupBox)
        self.getTc.setGeometry(QtCore.QRect(220, 30, 113, 23))
        self.getTc.setObjectName("getTc")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 30, 65, 15))
        self.label.setObjectName("label")
        self.groupBox_2.setVisible(False)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_9.setText(_translate("Form", "Parola"))
        self.label_6.setText(_translate("Form", "Mail"))
        self.label_4.setText(_translate("Form", "İsim Soyisim"))
        self.label_3.setText(_translate("Form", "Tc"))
        self.label_8.setText(_translate("Form", "Parola Tekrar"))
        self.label_5.setText(_translate("Form", "Telefon"))
        self.setRegister.setText(_translate("Form", "Kayıt ol"))
        self.login.setText(_translate("Form", "Giris Yap"))
        self.register_2.setText(_translate("Form", "Kayıt ol"))
        self.label_2.setText(_translate("Form", "Parola"))
        self.label.setText(_translate("Form", "Tc Giriniz"))

    def giris_yap(self):
        self.cur.execute("SELECT tc,parola FROM banka")
        row=   self.cur.fetchone()
        print(row)
        while row is not None:
            if self.getTc.text()==row[0] and self.getPass.text()==row[1]:
                print(row)
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Form()
                self.ui.setupUi(self.window,self.getTc.text())
                #14354312332
                Form.hide()
                self.window.show()  
            row = self.cur.fetchone()
        self.tc=self.getTc.text() 
        
    def kayit(self):
        self.groupBox_2.setVisible(True)
        self.groupBox.setVisible(False)

    def userRegister(self):
        hesap_no=self.setTc.text()[:4]+self.setTel.text()[:4]
        email_match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.setMail.text())
        regex= "\w{3}\w{3}\w{4}"
        tel=re.search(regex,self.setTel.text())
        tc_digit="^[-+]?[0-9]+$"
        tc=re.search(tc_digit,self.setTc.text())
        if email_match==None:
            print("email format uymuyot")
        else:
            if tel==None:
                print("telefon numarasını başında sıfır olmada girin")
        
            else:
                if tc==None:
                    print("tc sadece sayi olabilir")
        
                else:
                    if len(self.setTc.text())==11 and self.setPass.text()==self.setPassAgain.text():
                        try:
                            tc=self.setTc.text()
                            query =  "INSERT INTO banka (tc, name, tel,parola,mail,bakiye,doviz,altın,kart_borc) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s);"
                            data = (self.setTc.text(),self.setName.text(),self.setTel.text(),self.setPass.text(),self.setMail.text(),0,0,0,0)      
                            self.cur.execute(query, data)
                            self.con.commit()
                            self.groupBox_2.setVisible(False)
                            self.groupBox.setVisible(True)
                            self.cur.execute( """SELECT id FROM banka  Where tc = %s;""",(tc,))
                            row=   self.cur.fetchone()
                            print(row)
                            
                            
                            

                        except:
                            pass
                    else:
                         print("parolalr eşleşmiyor yada tc 11 hane olacak")
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = deneme()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

