# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAddDevice(object):
    def setupUi(self, DialogAddDevice):
        DialogAddDevice.setObjectName("DialogAddDevice")
        DialogAddDevice.resize(380, 197)
        self.gridLayout = QtWidgets.QGridLayout(DialogAddDevice)
        self.gridLayout.setObjectName("gridLayout")
        self.TypeLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.TypeLineEdit.setObjectName("TypeLineEdit")
        self.gridLayout.addWidget(self.TypeLineEdit, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(DialogAddDevice)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.TasteLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.TasteLineEdit.setObjectName("TasteLineEdit")
        self.gridLayout.addWidget(self.TasteLineEdit, 3, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(DialogAddDevice)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(DialogAddDevice)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.NameLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.gridLayout.addWidget(self.NameLineEdit, 0, 1, 1, 2)
        self.RoastingLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.RoastingLineEdit.setObjectName("RoastingLineEdit")
        self.gridLayout.addWidget(self.RoastingLineEdit, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(DialogAddDevice)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.PriceLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.PriceLineEdit.setObjectName("PriceLineEdit")
        self.gridLayout.addWidget(self.PriceLineEdit, 4, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(DialogAddDevice)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(DialogAddDevice)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.SizeLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.SizeLineEdit.setObjectName("SizeLineEdit")
        self.gridLayout.addWidget(self.SizeLineEdit, 5, 1, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogAddDevice)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 3)

        self.retranslateUi(DialogAddDevice)
        self.buttonBox.accepted.connect(DialogAddDevice.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogAddDevice.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogAddDevice)

    def retranslateUi(self, DialogAddDevice):
        _translate = QtCore.QCoreApplication.translate
        DialogAddDevice.setWindowTitle(_translate("DialogAddDevice", "Данные о кофе"))
        self.label_4.setText(_translate("DialogAddDevice", "Молотый/в зернах"))
        self.label_2.setText(_translate("DialogAddDevice", "Название сорта"))
        self.label_5.setText(_translate("DialogAddDevice", "Описание вкуса"))
        self.label_3.setText(_translate("DialogAddDevice", "Степень обжарки"))
        self.label_6.setText(_translate("DialogAddDevice", "Цена"))
        self.label_7.setText(_translate("DialogAddDevice", "Объем упаковки"))
