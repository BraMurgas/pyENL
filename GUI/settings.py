# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog, traduccion):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 346)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget = QtWidgets.QWidget(self.tab_3)
        self.widget.setGeometry(QtCore.QRect(10, 230, 317, 34))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fontText = QtWidgets.QFontComboBox(self.widget)
        self.fontText.setObjectName("fontText")
        self.fontText.setFontFilters(QtWidgets.QFontComboBox.MonospacedFonts)
        self.horizontalLayout.addWidget(self.fontText)
        self.sizeFont = QtWidgets.QSpinBox(self.widget)
        self.sizeFont.setMinimum(6)
        self.sizeFont.setMaximum(90)
        self.sizeFont.setProperty("value", 10)
        self.sizeFont.setObjectName("sizeFont")
        self.horizontalLayout.addWidget(self.sizeFont)
        self.widget1 = QtWidgets.QWidget(self.tab_3)
        self.widget1.setGeometry(QtCore.QRect(9, 9, 203, 206))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.format_line = QtWidgets.QLineEdit(self.widget1)
        self.format_line.setObjectName("format_line")
        self.verticalLayout_2.addWidget(self.format_line)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.temas = QtWidgets.QComboBox(self.widget1)
        self.temas.setObjectName("temas")
        self.temas.addItem("")
        self.temas.addItem("")
        self.temas.addItem("")
        self.temas.addItem("")
        self.temas.addItem("")
        self.temas.addItem("")
        self.temas.addItem("")
        self.temas.addItem("")
        self.verticalLayout_2.addWidget(self.temas)
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 247, 182))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.method_opt = QtWidgets.QComboBox(self.layoutWidget)
        self.method_opt.setObjectName("method_opt")
        self.method_opt.addItem("")
        self.method_opt.addItem("")
        self.method_opt.addItem("")
        self.method_opt.addItem("")
        self.method_opt.addItem("")
        self.method_opt.addItem("")
        self.method_opt.addItem("")
        self.method_opt.addItem("")
        self.method_opt.addItem("")
        self.method_opt.addItem("")
        self.verticalLayout_3.addWidget(self.method_opt)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.tol_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.tol_line.setObjectName("tol_line")
        self.verticalLayout_3.addWidget(self.tol_line)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.timeout_spin = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.timeout_spin.setObjectName("timeout_spin")
        self.verticalLayout_3.addWidget(self.timeout_spin)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog, traduccion)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog, traduccion):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", traduccion["Configuración"]))
        self.label.setText(_translate("Dialog", traduccion["Idioma (requiere reiniciar pyENL)"]))
        self.comboBox.setCurrentText(_translate("Dialog", traduccion["Spanish"]))
        self.comboBox.setItemText(0, _translate("Dialog", traduccion["Spanish"]))
        self.comboBox.setItemText(1, _translate("Dialog", traduccion["English"]))
        self.comboBox.setItemText(2, _translate("Dialog", traduccion["French"]))
        self.comboBox.setItemText(3, _translate("Dialog", traduccion["Portuguese"]))
        self.label_5.setText(_translate("Dialog", traduccion["Formato"]))
        self.label_6.setText(_translate("Dialog", traduccion["Tema"]))
        self.temas.setCurrentText(_translate("Dialog", traduccion["Predeterminado"]))
        self.temas.setItemText(0, _translate("Dialog", traduccion["Predeterminado"]))
        self.temas.setItemText(1, _translate("Dialog", "DarkBlack"))
        self.temas.setItemText(2, _translate("Dialog", "Dracula"))
        self.temas.setItemText(3, _translate("Dialog", "Blue"))
        self.temas.setItemText(4, _translate("Dialog", "BreezeDark"))
        self.temas.setItemText(5, _translate("Dialog", "BreezeLight"))
        self.temas.setItemText(6, _translate("Dialog", "Gray"))
        self.temas.setItemText(7, _translate("Dialog", "GrayDark"))
        self.label_7.setText(_translate("Dialog", traduccion["Fuente"]))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", traduccion["Interfaz"]))
        self.label_2.setText(_translate("Dialog", traduccion["Método"]))
        self.method_opt.setItemText(0, _translate("Dialog", "hybr"))
        self.method_opt.setItemText(1, _translate("Dialog", "lm"))
        self.method_opt.setItemText(2, _translate("Dialog", "broyden1"))
        self.method_opt.setItemText(3, _translate("Dialog", "broyden2"))
        self.method_opt.setItemText(4, _translate("Dialog", "anderson"))
        self.method_opt.setItemText(5, _translate("Dialog", "linearmixing"))
        self.method_opt.setItemText(6, _translate("Dialog", "diagbroyden"))
        self.method_opt.setItemText(7, _translate("Dialog", "excitingmixing"))
        self.method_opt.setItemText(8, _translate("Dialog", "krylov"))
        self.method_opt.setItemText(9, _translate("Dialog", "df-sane"))
        self.label_3.setText(_translate("Dialog", traduccion["Tolerancia"]))
        self.label_4.setText(_translate("Dialog", traduccion["Tiempo máximo de espera en segundos"]))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", traduccion["Solver"]))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", traduccion["Unidades"]))

