# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beta.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter.filedialog import askopenfilename
from tkinter import Tk
import MySQLdb
import re
import threading
import os
from Dialogbox import Ui_Dialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,qntd):
        #cria os widgets da interface gráfica
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(0, 0, 721, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.listView_2.setPalette(palette)
        self.listView_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listView_2.setObjectName("listView_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 681, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_3.addWidget(self.pushButton_19, 2, 1, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 325, 354))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.imagem = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imagem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imagem.setText("")
        self.imagem.setObjectName("imagem")
        self.gridLayout_2.addWidget(self.imagem, 0, 0, 1, 2)
        self.valores = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.valores.setObjectName("valores")
        self.gridLayout_2.addWidget(self.valores, 1, 0, 1, 1)
        self.pedidos = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pedidos.setObjectName("pedidos")
        self.gridLayout_2.addWidget(self.pedidos, 1, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea_2, 1, 1, 1, 7)
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 5, 1, 1)
        self.apaga_td = QtWidgets.QPushButton(self.tab_5)
        self.apaga_td.setObjectName("apaga_td")
        self.gridLayout_3.addWidget(self.apaga_td, 2, 3, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 303, 356))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.total = QtWidgets.QLabel(self.tab_5)
        self.total.setObjectName("total")
        self.gridLayout_3.addWidget(self.total, 2, 6, 1, 1)

        #self.toolButton = QtWidgets.QToolButton(self.tab_5)
        #self.toolButton.setObjectName("toolButton")
        #self.gridLayout_3.addWidget(self.toolButton, 2, 4, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 371, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 371, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.tab_6)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_6)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_6)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 47, 21))
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_6)
        self.doubleSpinBox.setGeometry(QtCore.QRect(60, 120, 62, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_18.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.add_imagem = QtWidgets.QPushButton(self.tab_6)
        self.add_imagem.setGeometry(QtCore.QRect(130, 120, 61, 23))
        self.add_imagem.setObjectName("add_imagem")
        self.imagem_2 = QtWidgets.QLabel(self.tab_6)
        self.imagem_2.setGeometry(QtCore.QRect(10, 160, 401, 211))
        self.imagem_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imagem_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imagem_2.setText("")
        self.imagem_2.setObjectName("imagem_2")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 50, 461, 211))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 459, 209))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pedidosF = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.pedidosF.setText("")
        self.pedidosF.setObjectName("pedidosF")
        self.horizontalLayout.addWidget(self.pedidosF)
        self.valoresF = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.valoresF.setText("")
        self.valoresF.setObjectName("valoresF")
        self.horizontalLayout.addWidget(self.valoresF)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.mesa_le = QtWidgets.QLineEdit(self.tab)
        self.mesa_le.setGeometry(QtCore.QRect(10, 20, 221, 20))
        self.mesa_le.setObjectName("mesa_le")
        self.search = QtWidgets.QPushButton(self.tab)
        self.search.setGeometry(QtCore.QRect(240, 20, 75, 23))
        self.search.setObjectName("search")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 270, 171, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(200, 270, 61, 16))
        self.label_9.setObjectName("label_9")
        self.valor_pago = QtWidgets.QLineEdit(self.tab)
        self.valor_pago.setGeometry(QtCore.QRect(260, 270, 131, 20))
        self.valor_pago.setObjectName("valor_pago")
        self.ok = QtWidgets.QPushButton(self.tab)
        self.ok.setGeometry(QtCore.QRect(400, 270, 71, 23))
        self.ok.setObjectName("ok")
        self.tabWidget.addTab(self.tab, "")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 9, 311, 41))
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";Tio do Ramen")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setLineWidth(1)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow,qntd)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow,qntd)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tam=qntd
        self.path=''
        self.is_atualizando=False
        self.set_buttons()
        self.set_pratos()
        self.th=threading.Thread(target=self.att_data) #inicia a thread para função de atualizar os dados na aba de pedidos
        self.th.daemon=True
        self.th.start()

    def pagar(self):#função para pegar o valor do pedido a ser pago então compara o valor total com o valor pago
        sql='update mesa set valor=0,pedidos=null,valores=null where cod=%s' 
        valor=self.label_8.text()
        print(valor[15:])
        valor=float(valor[15:]) 
        if self.pedidosF.text() and self.valoresF.text():
            if valor==float(self.valor_pago.text()):
                entrada=[self.mesa_le.text()]
                conn(sql,entrada)
                self.showdialog('Valor pago com sucesso!')
            elif valor<=float(self.valor_pago.text()):
                entrada=[self.mesa_le.text()]
                conn(sql,entrada)
                self.showdialog('Valor pago com sucesso!\nTroco de '+str(float(self.valor_pago.text())-valor)+' R$')
            else:
                self.showdialog('Valor pago é inferior ao total!')
            self.valor_pago.clear()
            self.mesa_le.clear()
            self.valoresF.clear()
            self.pedidosF.clear()
            self.label_8.setText("Valor total: ")

    def showdialog(self,st): #função para mostrar a tela se o dado foi ou não enviado ao BD
       self.window=QtWidgets.QDialog()
       self.ui=Ui_Dialog()
       self.ui.setupUi(self.window,st)
       self.window.show()

    def set_pedidos(self): #seta os pedidos se todos os campoes estiverem preenchidos
        sql='update mesa set pedidos=%s,valor=%s,valores=%s where cod=%s'
        ped=self.pedidos.text()
        entrada=[ped,self.tota_pg,self.valores.text(),self.cb.currentIndex()+1]
        if ped!='' and self.tota_pg!=0 and self.valores.text()!='':
            conn(sql,entrada)
            self.showdialog('Pedido efetuado com sucesso!')
        else:
            self.showdialog('Há campos não preenchidos')
        self.apaga()

    def busca_pedidos_e(self):
        x=self.mesa_le.text() #pega o numero da mesa
        if x:
            sql='select pedidos,valor,valores from mesa where cod=%s' 
            entrada=(x)
            lista=conn(sql,entrada)
            if len(lista)>0: #se houver dados ele seta na aba de finalizar pedidos
                x=lista[0]
                self.pedidosF.setText(x[0])
                self.valoresF.setText(x[2])
                self.label_8.setText('Total a pagar: '+str(x[1]))

    def set_pratos(self):
        sql1='select *from prato'
        sql2='select *from tipo'
        sql3='select cod from mesa'
        dados=conn(sql1,'') #recebe todos os dados da tabela prato
        dados2=conn(sql2,'')#recebe todos os dados da tabela tipo
        dados3=conn(sql3,'')#recebe todos os dados da tabela mesa
        print(dados2)
        self.tipos=[]
        self.boxs=[]
        self.paths=[]
        res=[]

        #seta as mesas no botão de selecionar mesas
        for i in range(len(dados3)):
            x=str(dados3[i])
            x=x.replace('(','')
            x=x.replace(')','')
            x=x.replace(',','')
            x='Mesa '+x
            res.append(x)

        self.cb=QtWidgets.QComboBox()
        self.cb.addItems(res) #coloca a lista no botão
        self.gridLayout_3.addWidget(self.cb, 2, 4, 1, 1)

        #seta todos os tipos na aba de pedidos
        for i in range(len(dados2)):
            x=dados2[i]
            self.tipos.append(x[1])

            groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
            groupBox.setObjectName("groupBox")
            groupBox.setTitle(x[1])
            self.verticalLayout.addWidget(groupBox)
            formLayout = QtWidgets.QFormLayout(groupBox)
            formLayout.setObjectName("formLayout")
            self.boxs.append((groupBox,formLayout))

        self.data=''
        self.dcount=0
        self.pushButton=[]
        self.ctrl=[]
        self.info=[]
        self.precos=[]
        self.eve=''
        self.tota_pg=0
        qntd=len(dados)

        #seta todos os pratos na tabela de pedidos
        for i in range(qntd):
            st='comida '+str(i)
            x=dados[i]
            self.info.append(x[1])
            self.precos.append(x[2])
            index=x[3]-1
            if x[4]!=None:
                self.paths.append(x[4])
            z=self.boxs[index]
            checkBox = QtWidgets.QCheckBox(z[0])
            checkBox.setObjectName("checkBox")
            checkBox.setText(self.info[i])

            spinBox = QtWidgets.QSpinBox(z[0])
            spinBox.setObjectName("spinBox")

            self.pushButton.append((checkBox,spinBox))
            z[1].setWidget(i, QtWidgets.QFormLayout.FieldRole,spinBox)
            z[1].setWidget(i, QtWidgets.QFormLayout.LabelRole, checkBox)
            self.ctrl.append(False)
            self.is_atualizando=False

    def set_buttons(self):  #seta os botoes para suas respectivas funções
        self.apaga_td.clicked.connect(self.apaga)
        self.pushButton_18.clicked.connect(self.cadastrar_prato)
        self.pushButton_19.clicked.connect(self.set_pedidos)
        self.search.clicked.connect(self.busca_pedidos_e)
        self.add_imagem.clicked.connect(self.search_imagem)
        self.ok.clicked.connect(self.pagar)

    def apaga(self): #apaga os dados da aba efetuar os dados
        self.data=''
        self.pedidos.setText('')
        self.eve=''
        self.valores.setText('')
        self.total.setText('0 R$')

    def att_data(self):
        j=0
        x=''
        while True:        #função para atualizar os dados e as imagens na aba de efetuar os pedidos
            if not self.is_atualizando:
                tam=len(self.pushButton)
                if j==tam:
                    j=0
            if self.pushButton!=[]:      #verifica se é vazia
                try:
                   x=self.pushButton[j]
                except:
                   pass

                if x[0].isChecked() and x[1].value()>0:   #ver se o pedido foi selecionado e foi colocado uma quantidade maior que 0
                   self.data=self.data+'*'+self.info[j]+'\n'  #atualiza os dados e coloca a imagem
                   self.dcount+=1
                   self.eve=self.eve+' x '+str(x[1].value())+' - '+str(self.precos[j]*x[1].value())+'\n'
                   self.tota_pg=self.tota_pg+self.precos[j]*x[1].value()
                   self.pedidos.setText(self.data)
                   self.valores.setText(self.eve)
                   st=str(self.tota_pg)+'R$'
                   self.total.setText(st)
                   x[1].setValue(0)
                   x[0].setChecked(False)
                   self.imagem.setPixmap(QtGui.QPixmap(self.paths[j]))
                j+=1

    def removeButtons(self):  #apaga todos os widgets da lista em verticalLayout
        for cnt in reversed(range(self.verticalLayout.count())):
            widget = self.verticalLayout.takeAt(cnt).widget()
            if widget is not None:
                widget.deleteLater()

    def reset(self):              #reseta todos objetos para null, inclusive listas de objetos
        self.is_atualizando=True
        self.pushButton.clear()
        self.boxs.clear()
        self.tipos.clear()
        self.info.clear()
        self.precos.clear()
        self.removeButtons()
        self.set_pratos()

    def search_imagem(self): #função para pegar a imagem no Pc
        Tk().withdraw() # Isto torna oculto a janela principal
        filename = askopenfilename() # Isto te permite selecionar um arquivo
        filename=filename[2:]
        print(filename)
        self.path=filename.replace('/','\\')
        self.imagem_2.setPixmap(QtGui.QPixmap(self.path))

    def cadastrar_prato(self): #função para cadastrar os pratos, apenas pega os parametros e envia para o BD caso todos tenham sido preenchidos
        sql='call cadastrar_prato(%s,%s,%s,%s)'
        entrada=[self.lineEdit.text(),self.lineEdit_2.text(),self.doubleSpinBox.value(),self.path]
        print(entrada)
        if self.lineEdit.text() and self.lineEdit_2.text() and self.doubleSpinBox.value():
            conn(sql,entrada)
            self.reset()
            self.showdialog('Prato cadastrado com sucesso!')
        else:
            self.showdialog('Campos não preenchidos!')

    def retranslateUi(self, MainWindow,qntd): #função padrão da pyqt5 para renomeiar os widgets
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_19.setText(_translate("MainWindow", "Confirma"))
        self.valores.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.pedidos.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.label_4.setText(_translate("MainWindow", "TOTAL = "))
        self.apaga_td.setText(_translate("MainWindow", "Apagar tudo"))
        self.total.setText(_translate("MainWindow", "0 R$"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Efetuar pedidos"))
        self.label.setText(_translate("MainWindow", "Nome do Prato"))
        self.label_2.setText(_translate("MainWindow", "Tipo"))
        self.label_3.setText(_translate("MainWindow", "Preço"))
        self.pushButton_18.setText(_translate("MainWindow", "Cadastrar"))
        self.add_imagem.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Cadastrar prato"))
        self.mesa_le.setPlaceholderText(_translate("MainWindow", "Digite o número da mesa..."))
        self.search.setText(_translate("MainWindow", "Pesquisar"))
        self.label_8.setText(_translate("MainWindow", "Valor total: "))
        self.label_9.setText(_translate("MainWindow", "Valor pago:"))
        self.ok.setText(_translate("MainWindow", "Ok"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Finalizar pedido"))
        self.label_5.setText(_translate("MainWindow", "Tio do Ramén"))



def conn(sql,entrada): #função de conexão com o BD
    con=MySQLdb.connect(host='localhost',db='restaurante_BD',user='root',passwd='c66209f7e8')
    con.select_db('restaurante_BD')
    cursor=con.cursor()

    if entrada!='': #se tiver parametros
        try:
            cursor.execute(sql,entrada)
            con.commit()
            print(cursor.rowcount,'linhas afetadas')
            dados=cursor.fetchall() #caso haja o BD retorne um dado
        except (MySQLdb.Error, MySQLdb.Warning) as e: #caso haja um erro
            print(e)
        if dados!='': #retorna os dados do BD
            return dados
    else:
        try: #caso não haja parametros
            cursor.execute(sql)
            dados=cursor.fetchall()
            print(cursor.rowcount,'linhas afetadas')
            return dados
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)
    con.close()

if __name__ == "__main__": #função padrao da pyqt5 para iniciar a interface gráfica
    import sys
    conn('show tables;','')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,5)
    MainWindow.show()
    sys.exit(app.exec_())

