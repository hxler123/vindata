# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataProcess.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(433, 774)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.mubansheet_textEdit = QtWidgets.QTextEdit(Form)
        self.mubansheet_textEdit.setGeometry(QtCore.QRect(30, 50, 381, 31))
        self.mubansheet_textEdit.setObjectName("mubansheet_textEdit")
        self.mubansheet_label = QtWidgets.QLabel(Form)
        self.mubansheet_label.setGeometry(QtCore.QRect(30, 20, 381, 21))
        self.mubansheet_label.setObjectName("mubansheet_label")
        self.mubanwenjian_textEdit = QtWidgets.QTextEdit(Form)
        self.mubanwenjian_textEdit.setGeometry(QtCore.QRect(30, 130, 381, 31))
        self.mubanwenjian_textEdit.setObjectName("mubanwenjian_textEdit")
        self.muban_label = QtWidgets.QLabel(Form)
        self.muban_label.setGeometry(QtCore.QRect(30, 100, 371, 21))
        self.muban_label.setObjectName("muban_label")
        self.zonshuju_textEdit = QtWidgets.QTextEdit(Form)
        self.zonshuju_textEdit.setGeometry(QtCore.QRect(30, 230, 381, 31))
        self.zonshuju_textEdit.setObjectName("zonshuju_textEdit")
        self.zonshuju_label = QtWidgets.QLabel(Form)
        self.zonshuju_label.setGeometry(QtCore.QRect(30, 200, 371, 21))
        self.zonshuju_label.setObjectName("zonshuju_label")
        self.zonshujusheet_textEdit = QtWidgets.QTextEdit(Form)
        self.zonshujusheet_textEdit.setGeometry(QtCore.QRect(30, 320, 381, 31))
        self.zonshujusheet_textEdit.setObjectName("zonshujusheet_textEdit")
        self.zonshujusheet_label = QtWidgets.QLabel(Form)
        self.zonshujusheet_label.setGeometry(QtCore.QRect(30, 290, 271, 21))
        self.zonshujusheet_label.setObjectName("zonshujusheet_label")
        self.confirm_Button = QtWidgets.QPushButton(Form)
        self.confirm_Button.setGeometry(QtCore.QRect(340, 580, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Adobe Fan Heiti Std")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.confirm_Button.setFont(font)
        self.confirm_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.confirm_Button.setObjectName("confirm_Button")
        self.mubandakai_pushButton = QtWidgets.QPushButton(Form)
        self.mubandakai_pushButton.setGeometry(QtCore.QRect(330, 170, 75, 23))
        self.mubandakai_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.mubandakai_pushButton.setObjectName("mubandakai_pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 270, 75, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setGeometry(QtCore.QRect(20, 660, 291, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.date_label = QtWidgets.QLabel(Form)
        self.date_label.setGeometry(QtCore.QRect(30, 380, 291, 16))
        self.date_label.setObjectName("date_label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 400, 271, 31))
        self.textEdit.setObjectName("textEdit")
        self.type_ComboBox = QtWidgets.QComboBox(Form)
        self.type_ComboBox.setGeometry(QtCore.QRect(190, 590, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.type_ComboBox.setFont(font)
        self.type_ComboBox.setObjectName("type_ComboBox")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.qunianfile_textEdit = QtWidgets.QTextEdit(Form)
        self.qunianfile_textEdit.setGeometry(QtCore.QRect(30, 480, 381, 41))
        self.qunianfile_textEdit.setObjectName("qunianfile_textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 452, 321, 20))
        self.label.setObjectName("label")
        self.quniansheet_textEdit = QtWidgets.QTextEdit(Form)
        self.quniansheet_textEdit.setGeometry(QtCore.QRect(30, 570, 104, 41))
        self.quniansheet_textEdit.setObjectName("quniansheet_textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 540, 251, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 545, 121, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mubansheet_label.setText(_translate("Form", "模板sheet"))
        self.muban_label.setText(_translate("Form", "模板文件路径,支持拖文件/手动选择文件"))
        self.zonshuju_label.setText(_translate("Form", "总数据文件路径，支持拖文件/手动选择文件"))
        self.zonshujusheet_label.setText(_translate("Form", "总数据sheet"))
        self.confirm_Button.setText(_translate("Form", "开始"))
        self.mubandakai_pushButton.setText(_translate("Form", "open file"))
        self.pushButton_2.setText(_translate("Form", "open file"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Adobe 黑体 Std R\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">数据已完成,记得亲下木木呦 ^-^</span></p></body></html>"))
        self.date_label.setText(_translate("Form", "指定年份，如果是今年,可以不填写"))
        self.type_ComboBox.setItemText(0, _translate("Form", "sku"))
        self.type_ComboBox.setItemText(1, _translate("Form", "品系"))
        self.type_ComboBox.setItemText(2, _translate("Form", "业态品类"))
        self.label.setText(_translate("Form", "去年数据文件路径"))
        self.label_2.setText(_translate("Form", "去年数据Sheet"))
        self.label_3.setText(_translate("Form", "数据处理类型"))
