# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
import math


class Ui_Form(object):
    def __init__(self):
        self.dolar=4.80
        self.Altin=190
        try:
            self.con = psycopg2.connect("host='localhost' dbname='deneme' user='postgres' password='1234'")   
            self.cur = self.con.cursor()
        except :
            print("bağlantı hatası")
    def setupUi(self, Form,a):
        self.tc=a
        Form.setObjectName("Form")
        Form.resize(900, 604)
        self.get_Hesap = QtWidgets.QPushButton(Form)
        self.get_Hesap.setGeometry(QtCore.QRect(0, 10, 111, 23))
        self.get_Hesap.setObjectName("get_Hesap")
        self.get_Hesap.clicked.connect(self.get_CardList)
        
        self.doviz_Altn = QtWidgets.QPushButton(Form)
        self.doviz_Altn.setGeometry(QtCore.QRect(520, 10, 111, 23))
        self.doviz_Altn.setObjectName("doviz_Altn")
        self.doviz_Altn.clicked.connect(self.doviz_cevir)

        self.odemeler = QtWidgets.QPushButton(Form)
        self.odemeler.setGeometry(QtCore.QRect(390, 10, 111, 23))
        self.odemeler.setObjectName("odemeler")
        self.odemeler.clicked.connect(self.ode)

        self.para_Transfer = QtWidgets.QPushButton(Form)
        self.para_Transfer.setGeometry(QtCore.QRect(260, 10, 111, 23))
        self.para_Transfer.setObjectName("para_Transfer")
        self.para_Transfer.clicked.connect(self.transfer)

        self.get_Kart = QtWidgets.QPushButton(Form)
        self.get_Kart.setGeometry(QtCore.QRect(130, 10, 111, 23))
        self.get_Kart.setObjectName("get_Kart")
        self.get_Kart.clicked.connect(self.get_CardList)

        self.guvenlik = QtWidgets.QPushButton(Form)
        self.guvenlik.setGeometry(QtCore.QRect(650, 10, 130, 23))
        self.guvenlik.setObjectName("guvenlik")
        self.guvenlik.clicked.connect(self.guvenlik_visible)

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(780, 580, 111, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.cikis)

        self.hesaplar_Groupbox = QtWidgets.QGroupBox(Form)
        self.hesaplar_Groupbox.setGeometry(QtCore.QRect(50, 40, 461, 201))
        self.hesaplar_Groupbox.setObjectName("hesaplar_Groupbox")
        self.hesaplar_Groupbox.setTitle("")
        
        

        self.hesap_Detay = QtWidgets.QListWidget(self.hesaplar_Groupbox)
        self.hesap_Detay.setGeometry(QtCore.QRect(20, 40, 431, 121))
        self.hesap_Detay.setObjectName("hesap_Detay")
        self.hesap_Detay.setVisible(False)

        

        self.card_List = QtWidgets.QListWidget(self.hesaplar_Groupbox)
        self.card_List.setGeometry(QtCore.QRect(80, 40, 291, 121))
        self.card_List.setObjectName("card_List")
     
        
        self.incele = QtWidgets.QPushButton(self.hesaplar_Groupbox)
        self.incele.setGeometry(QtCore.QRect(290, 170, 80, 23))
        self.incele.setObjectName("incele")
        self.incele.clicked.connect(self.btn_incele)    
     
        self.transfer_Groupbox = QtWidgets.QGroupBox(Form)
        self.transfer_Groupbox.setGeometry(QtCore.QRect(50, 240, 461, 171))
        self.transfer_Groupbox.setObjectName("transfer_Groupbox")
        
        self.hedep_hesap = QtWidgets.QLineEdit(self.transfer_Groupbox)
        self.hedep_hesap.setGeometry(QtCore.QRect(110, 30, 113, 23))
        self.hedep_hesap.setObjectName("hedep_hesap")
        
        self.label = QtWidgets.QLabel(self.transfer_Groupbox)
        self.label.setGeometry(QtCore.QRect(10, 30, 99, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.transfer_Groupbox)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 90, 21))
        self.label_2.setObjectName("label_2")
        
        self.hesap_list = QtWidgets.QListWidget(self.transfer_Groupbox)
        self.hesap_list.setGeometry(QtCore.QRect(110, 100, 171, 61))
        self.hesap_list.setObjectName("hesap_list")
        
        self.label_3 = QtWidgets.QLabel(self.transfer_Groupbox)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 59, 21))
        self.label_3.setObjectName("label_3")
        
        self.miktar = QtWidgets.QLineEdit(self.transfer_Groupbox)
        self.miktar.setGeometry(QtCore.QRect(110, 60, 113, 23))
        self.miktar.setObjectName("miktar")
        
        self.gonder = QtWidgets.QPushButton(self.transfer_Groupbox)
        self.gonder.setGeometry(QtCore.QRect(320, 140, 80, 23))
        self.gonder.setObjectName("gonder")
        self.gonder.clicked.connect(self.para_gonder)
        
        self.odeme_Groupbox = QtWidgets.QGroupBox(Form)
        self.odeme_Groupbox.setGeometry(QtCore.QRect(530, 40, 370, 201))
        self.odeme_Groupbox.setObjectName("odeme_Groupbox")
        
        self.odeme_Combo = QtWidgets.QComboBox(self.odeme_Groupbox)
        self.odeme_Combo.setGeometry(QtCore.QRect(100, 20, 79, 23))
        self.odeme_Combo.setObjectName("odeme_Combo")
        self.odeme_Combo.addItem("")
        self.odeme_Combo.addItem("")
        self.odeme_Combo.addItem("")
        self.odeme_Combo.addItem("")
        
        self.btn_odeme = QtWidgets.QPushButton(self.odeme_Groupbox)
        self.btn_odeme.setGeometry(QtCore.QRect(180, 170, 80, 23))
        self.btn_odeme.setObjectName("btn_odeme")
        self.btn_odeme.clicked.connect(self.odeme_yap)

        self.odeme_kaynak_hesap = QtWidgets.QListWidget(self.odeme_Groupbox)
        self.odeme_kaynak_hesap.setGeometry(QtCore.QRect(140, 100, 171, 51))
        self.odeme_kaynak_hesap.setObjectName("odeme_kaynak_hesap")
        self.label_4 = QtWidgets.QLabel(self.odeme_Groupbox)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 130, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.odeme_Groupbox)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.label_5.setObjectName("label_5")
        self.odeme_hedef_hesap = QtWidgets.QLineEdit(self.odeme_Groupbox)
        self.odeme_hedef_hesap.setGeometry(QtCore.QRect(100, 60, 113, 23))
        self.odeme_hedef_hesap.setObjectName("odeme_hedef_hesap")

        self.odeme_miktar = QtWidgets.QLineEdit(self.odeme_Groupbox)
        self.odeme_miktar.setGeometry(QtCore.QRect(220, 60, 113, 23))
        self.odeme_miktar.setObjectName("odeme_hedef_hesap")
        
        self.doviz_Groupbox = QtWidgets.QGroupBox(Form)
        self.doviz_Groupbox.setGeometry(QtCore.QRect(530, 240, 370, 171))
        self.doviz_Groupbox.setObjectName("doviz_Groupbox")
        self.altin_combo = QtWidgets.QComboBox(self.doviz_Groupbox)
        self.altin_combo.setGeometry(QtCore.QRect(70, 20, 79, 23))
        self.altin_combo.setObjectName("altin_combo")
        self.altin_combo.addItem("")
        self.altin_combo.addItem("")
     
        self.label_6 = QtWidgets.QLabel(self.doviz_Groupbox)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 230, 21))
        self.label_6.setObjectName("label_6")
        
        self.altin_miktar = QtWidgets.QLineEdit(self.doviz_Groupbox)
        self.altin_miktar.setGeometry(QtCore.QRect(190, 70, 113, 23))
        self.altin_miktar.setObjectName("altin_miktar")

        self.altin_cevir = QtWidgets.QPushButton(self.doviz_Groupbox)
        self.altin_cevir.setGeometry(QtCore.QRect(230, 140, 80, 23))
        self.altin_cevir.setObjectName("altin_cevir")
        self.altin_cevir.clicked.connect(self.para_cevir)

        self.guvenlik_Groupbox = QtWidgets.QGroupBox(Form)
        self.guvenlik_Groupbox.setGeometry(QtCore.QRect(160, 410, 410, 181))
        self.guvenlik_Groupbox.setObjectName("guvenlik_Groupbox")
        self.combo_guvenlik = QtWidgets.QComboBox(self.guvenlik_Groupbox)
        self.combo_guvenlik.setGeometry(QtCore.QRect(120, 30, 141, 23))
        self.combo_guvenlik.setObjectName("combo_guvenlik")
        self.combo_guvenlik.addItem("")
        self.combo_guvenlik.addItem("")
        self.combo_guvenlik.addItem("")
        self.guvenlik_telefon = QtWidgets.QLineEdit(self.guvenlik_Groupbox)
        self.guvenlik_telefon.setGeometry(QtCore.QRect(190, 70, 113, 23))
        self.guvenlik_telefon.setObjectName("guvenlik_telefon")
        self.guvenlik_yeni_telefon = QtWidgets.QLineEdit(self.guvenlik_Groupbox)
        self.guvenlik_yeni_telefon.setGeometry(QtCore.QRect(190, 100, 113, 23))
        self.guvenlik_yeni_telefon.setObjectName("guvenlik_yeni_telefon")
        self.guvenlik_yeni_tel_tekrar = QtWidgets.QLineEdit(self.guvenlik_Groupbox)
        self.guvenlik_yeni_tel_tekrar.setGeometry(QtCore.QRect(190, 130, 113, 30))
        self.guvenlik_yeni_tel_tekrar.setObjectName("guvenlik_yeni_tel_tekrar")
        self.label_7 = QtWidgets.QLabel(self.guvenlik_Groupbox)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 180, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.guvenlik_Groupbox)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 180, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.guvenlik_Groupbox)
        self.label_9.setGeometry(QtCore.QRect(10, 140, 170, 16))
        self.label_9.setObjectName("label_9")

        self.btn_guvenlik = QtWidgets.QPushButton(self.guvenlik_Groupbox)
        self.btn_guvenlik.setGeometry(QtCore.QRect(320, 130, 80, 23))
        self.btn_guvenlik.setObjectName("btn_guvenlik")
        self.btn_guvenlik.clicked.connect(self.guvenlik_update)

        self.odeme_Groupbox.setVisible(False)
        self.guvenlik_Groupbox.setVisible(False)
        self.doviz_Groupbox.setVisible(False)
        self.hesaplar_Groupbox.setVisible(False)
        self.transfer_Groupbox.setVisible(False) 
        self.get_CardList()
     
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.get_Hesap.setText(_translate("Form", "Hesaplarım "))
        self.doviz_Altn.setText(_translate("Form", "Döviz/Altın"))
        self.odemeler.setText(_translate("Form", "Ödemeler"))
        self.para_Transfer.setText(_translate("Form", "Para Transferi"))
        self.get_Kart.setText(_translate("Form", "Kartlarım"))
        self.guvenlik.setText(_translate("Form", "Guvenlik  Ayarları"))
        self.pushButton_7.setText(_translate("Form", "Çıkış"))
        self.hesaplar_Groupbox.setTitle(_translate("Form", ""))
        self.incele.setText(_translate("Form", "İncele"))
        self.transfer_Groupbox.setTitle(_translate("Form", ""))
        self.label.setText(_translate("Form", "Alıcı tc"))
        self.label_2.setText(_translate("Form", "Gonderici"))
        self.label_3.setText(_translate("Form", "Miktar"))
        self.gonder.setText(_translate("Form", "Gonder"))
        self.odeme_Groupbox.setTitle(_translate("Form", ""))
        self.odeme_Combo.setItemText(0, _translate("Form", "Fatura"))
        self.odeme_Combo.setItemText(1, _translate("Form", "Kredi"))
        self.odeme_Combo.setItemText(2, _translate("Form", "Tl "))
        self.odeme_Combo.setItemText(3, _translate("Form", "Şans Oyunları"))
        self.btn_odeme.setText(_translate("Form", "odeme yap"))
        self.label_4.setText(_translate("Form", "Odenecek  hesap"))
        self.label_5.setText(_translate("Form", "Fatura No"))
        self.doviz_Groupbox.setTitle(_translate("Form", "GroupBox"))
        self.altin_combo.setItemText(0, _translate("Form", "Altın"))
        self.altin_combo.setItemText(1, _translate("Form", "Dolar"))
        self.label_6.setText(_translate("Form", "Çevirmek istediğiniz miktar"))
        self.altin_cevir.setText(_translate("Form", "Çevir"))
        self.guvenlik_Groupbox.setTitle(_translate("Form", "GroupBox"))
        self.combo_guvenlik.setItemText(0, _translate("Form", "Telefon Güncelle"))
        self.combo_guvenlik.setItemText(1, _translate("Form", "Parola Güncelle"))
        self.combo_guvenlik.setItemText(2, _translate("Form", "Mail Adresi Güncelle"))
        self.label_7.setText(_translate("Form", "Mevcut Telefon No"))
        self.label_8.setText(_translate("Form", "Yeni Telefon No"))
        self.label_9.setText(_translate("Form", "Tekrar Yeni telefon No"))
        self.btn_guvenlik.setText(_translate("Form", "Guncelle"))

    def get_CardList(self):
        self.visible()
        self.hesaplar_Groupbox.setVisible(True)
        self.hesap_Detay.setVisible(False)
        self.card_List.setVisible(True)
        self.card_List.clear()
        
        try:
            self.cur.execute( """SELECT id FROM banka  Where tc = %s;""",(self.tc,))
            row=   self.cur.fetchone()
            print(row[0])
            self.card_List.addItem(str(row[0]))
        except:
            pass
    def btn_incele(self):
        self.visible()
        self.hesaplar_Groupbox.setVisible(True)
        self.hesap_Detay.clear()
        self.card_List.setVisible(False)
        hesap=self.card_List.currentItem().text()
        self.hesap_Detay.setVisible(True)
        try:
            self.cur.execute( """SELECT * FROM banka  Where id = %s;""",(hesap,))
            row=   self.cur.fetchone()
            bakiye="bakiyeniz "+ str(row[6])+ "tl dir"
            dolar="dolat hesabınız "+ str(row[7])+ " $ dir"
            self.hesap_Detay.addItem(bakiye)
            self.hesap_Detay.addItem(dolar)
            self.hesap_Detay.addItem("altın hesabınız "+str(row[8])+" tane dir")
            self.hesap_Detay.addItem("kredi kartı borcunuz "+str(row[9])+" tl")
            
            
        except:
            pass
    def transfer(self):
        self.visible()
        self.transfer_Groupbox.setVisible(True)
        self.hedep_hesap.clear()
        self.miktar.clear()
        self.hesap_list.clear()
        try:
            self.cur.execute( """SELECT id FROM banka  Where tc = %s;""",(self.tc,))
            row=   self.cur.fetchone()
            self.hesap_list.addItem(str(row[0]))
        except:
            pass
    def para_gonder(self):
        id=self.hesap_list.currentItem().text()
        try:
            self.cur.execute( """SELECT bakiye FROM banka  Where id = %s;""",(id,))
            row=self.cur.fetchone()
            
        except:
            pass
        print(self.miktar.text())
        if int(self.miktar.text()) <= int(row[0]):
            kalan=int(row[0])-int(self.miktar.text())
            self.cur.execute( """SELECT bakiye FROM banka  Where tc = %s;""",(self.hedep_hesap.text(),))
            row=   self.cur.fetchone()
            gonderilen=int(row[0])+int(self.miktar.text())
            self.cur.execute( """update banka SET bakiye =%s    Where tc = %s;""",(gonderilen,self.hedep_hesap.text()),)
            self.cur.execute( """update banka SET bakiye =%s    Where id = %s;""",(kalan,id,))
            self.con.commit()
            self.transfer_Groupbox.setVisible(False)
            self.hesaplar_Groupbox.setVisible(True)

        else:
            print("gonderme")

    def ode(self):
        self.visible()
        self.odeme_Groupbox.setVisible(True)
        self.odeme_Combo.currentTextChanged.connect(self.combo_change)
    def combo_change(self):
        self.odeme_kaynak_hesap.clear()
        self.label_5.setText(self.odeme_Combo.currentText())
        try:
            self.cur.execute( """SELECT id FROM banka  Where tc = %s;""",(self.tc,))
            row=   self.cur.fetchone()
            self.odeme_kaynak_hesap.addItem(str(row[0]))
        except:
            pass
        if self.odeme_Combo.currentText()=="Kredi":
            self.cur.execute( """SELECT kart_borc FROM banka  Where tc = %s;""",(self.tc,))
            kredi=self.cur.fetchone()
            if int(kredi[0]>0):
                print("borc var")
            else:
                self.odeme_hedef_hesap.setVisible(False)
                self.odeme_miktar.setVisible(False)
                self.odeme_kaynak_hesap.setVisible(False)
                self.label_5.setText("borc yok")
        else:
            self.odeme_miktar.clear()
            self.hedep_hesap.clear()
            self.odeme_hedef_hesap.setVisible(True)
            self.odeme_miktar.setVisible(True)
            self.odeme_kaynak_hesap.setVisible(True)
                
    def odeme_yap(self):
        id=self.odeme_kaynak_hesap.currentItem().text()
        try:
            self.cur.execute( """SELECT bakiye FROM banka  Where id = %s;""",(id,))
            row=self.cur.fetchone()
            print(row)
            
        except:
            pass
        if self.odeme_Combo.currentText()=="Kredi":
            self.cur.execute( """SELECT kart_borc FROM banka  Where id = %s;""",(id,))
            kredi=self.cur.fetchone()
            if int(self.odeme_miktar.text())<=int(kredi[0]):
                
                if int(self.odeme_miktar.text())<=int(row[0]):
                    kalan=int(row[0])-int(self.odeme_miktar.text())
                    borc_kalan=int(kredi[0])-int(self.odeme_miktar.text())
                    print(borc_kalan,kalan)
                    self.cur.execute( """update banka SET bakiye =%s    Where id = %s;""",(kalan,id,))
                    self.cur.execute( """update banka SET kart_borc =%s    Where id = %s;""",(borc_kalan,id,))
                    self.con.commit()

        elif int(self.odeme_miktar.text()) <= int(row[0]):
            kalan=int(row[0])-int(self.odeme_miktar.text())
            self.cur.execute( """update banka SET bakiye =%s    Where id = %s;""",(kalan,id,))
            self.con.commit()
        self.get_CardList()
    def doviz_cevir(self):
        self.visible()
        self.doviz_Groupbox.setVisible(True)
       

    def para_cevir(self):
        secim=self.altin_combo.currentText()
        try:
            self.cur.execute( """SELECT * FROM banka  Where tc = %s;""",(self.tc,))
            row=   self.cur.fetchone()
            #row[7] dolar row[8] altın
        except :
            pass
        miktar=self.altin_miktar.text()
        if secim=="Altın":
            
            if int(miktar)<=int(row[6]):
                cevir=float(int(miktar)/self.Altin)
                kalan=float(int(row[6])-int(miktar))
                altin=int(row[8])+math.ceil(cevir)
                self.cur.execute( """update banka SET bakiye =%s  ,altın=%s   Where tc = %s;""",(int(kalan),altin,self.tc,))

            else:
                print("cevirme")
        elif secim=="Dolar":
            if int(miktar)<=int(row[6]):
                cevir=float(int(miktar)/self.dolar)
                kalan=float(int(row[6])-int(miktar))
                doviz=int(row[7])+math.ceil(cevir)
                print(math.ceil(cevir),kalan)
                self.cur.execute( """update banka SET bakiye =%s  ,doviz=%s   Where tc = %s;""",(int(kalan),doviz,self.tc,))

            else:
                print("cevirme")
      
        else:
            pass
        self.con.commit()
        self.altin_miktar.clear()


    def guvenlik_visible(self):
        self.visible()
        self.guvenlik_Groupbox.setVisible(True)
        self.combo_guvenlik.currentTextChanged.connect(self.guvenlik_change)
    def guvenlik_change(self):
       
        print(self.combo_guvenlik.currentText())
        if "Telefon Güncelle"==self.combo_guvenlik.currentText():
            self.label_7.setText("mevcut Telefon no")
            self.label_8.setText("yeni Telefon no")
            self.label_9.setText("tekrar Telefon no")
        if "Parola Güncelle"==self.combo_guvenlik.currentText():
            self.label_7.setText("mevcut Parola")
            self.label_8.setText("yeni Parola")
            self.label_9.setText("tekrar Parola")
        if "Mail Adresi Güncelle"==self.combo_guvenlik.currentText():
            self.label_7.setText("mevcut mail")
            self.label_8.setText("yeni mail")
            self.label_9.setText("tekrar mail")
    def guvenlik_update(self):
        self.cur.execute( """SELECT * FROM banka  Where tc = %s;""",(self.tc,))
        row=   self.cur.fetchone()
        if self.guvenlik_yeni_telefon.text()==self.guvenlik_yeni_tel_tekrar.text():
            if self.combo_guvenlik.currentText()=="Mail Adresi Güncelle":
                if self.guvenlik_telefon.text()==str(row[5]):
                    self.cur.execute( """update banka SET mail =%s     Where tc = %s;""",(self.guvenlik_yeni_telefon.text(),self.tc,))
            elif self.combo_guvenlik.currentText()=="Parola Güncelle":
                if self.guvenlik_telefon.text()==str(row[4]):
                    self.cur.execute( """update banka SET parola =%s     Where tc = %s;""",(self.guvenlik_yeni_telefon.text(),self.tc,))
            else:
                if self.guvenlik_telefon.text()==str(row[3]):
                    self.cur.execute( """update banka SET tel =%s     Where tc = %s;""",(self.guvenlik_yeni_telefon.text(),self.tc,))
        else:
            pass
        self.con.commit()

        
    def visible(self):
        self.odeme_Groupbox.setVisible(False)
        self.guvenlik_Groupbox.setVisible(False)
        self.doviz_Groupbox.setVisible(False)
        self.hesaplar_Groupbox.setVisible(False)
        self.transfer_Groupbox.setVisible(False)           
        
    def cikis(self):
        exit()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

