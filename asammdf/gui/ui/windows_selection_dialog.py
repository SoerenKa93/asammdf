# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows_selection_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowSelectionDialog(object):
    def setupUi(self, WindowSelectionDialog):
        WindowSelectionDialog.setObjectName("WindowSelectionDialog")
        WindowSelectionDialog.resize(306, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(WindowSelectionDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(WindowSelectionDialog)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.lay = QtWidgets.QVBoxLayout(self.groupBox)
        self.lay.setObjectName("lay")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 268, 220))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.selection_layout = QtWidgets.QVBoxLayout()
        self.selection_layout.setObjectName("selection_layout")
        self.verticalLayout_3.addLayout(self.selection_layout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.lay.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(WindowSelectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(WindowSelectionDialog)
        self.buttonBox.accepted.connect(WindowSelectionDialog.accept)
        self.buttonBox.rejected.connect(WindowSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(WindowSelectionDialog)

    def retranslateUi(self, WindowSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        WindowSelectionDialog.setWindowTitle(_translate("WindowSelectionDialog", "Select window type"))
        self.groupBox.setTitle(_translate("WindowSelectionDialog", "Available window types"))
