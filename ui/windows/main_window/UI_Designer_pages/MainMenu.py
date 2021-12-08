# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MainMenuView(object):
    def setupUi(self, Form, widgetName:str):
        Form.setObjectName(widgetName)
        Form.resize(1255, 628)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(70, 70, 1236, 582))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.pushButton__home_iv = QtWidgets.QPushButton(self.frame_7)
        self.pushButton__home_iv.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(1,115,164);   \n"
"    text-align: center;\n"
"    color: rgb(255,255,255);\n"
"    padding: 8px;\n"
"    padding-left: 15 px;\n"
"    padding-right: 15 px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(1,133,177);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,115,164);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Andreas/PycharmProjects/TarifSimulator_WE/GUI/icons/16x16/cil-loop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton__home_iv.setIcon(icon)
        self.pushButton__home_iv.setObjectName("pushButton__home_iv")
        self.gridLayout_35.addWidget(self.pushButton__home_iv, 2, 3, 1, 1)
        self.pushButton__home_tv = QtWidgets.QPushButton(self.frame_7)
        self.pushButton__home_tv.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(1,115,164);   \n"
"    text-align: center;\n"
"    color: rgb(255,255,255);\n"
"    padding: 8px;\n"
"    padding-left: 15 px;\n"
"    padding-right: 15 px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(1,133,177);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,115,164);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Andreas/PycharmProjects/TarifSimulator_WE/GUI/icons/16x16/cil-library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton__home_tv.setIcon(icon1)
        self.pushButton__home_tv.setObjectName("pushButton__home_tv")
        self.gridLayout_35.addWidget(self.pushButton__home_tv, 2, 2, 1, 1)
        self.pushButton_home_pfz = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_home_pfz.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(1,115,164);   \n"
"    text-align: center;\n"
"    color: rgb(255,255,255);\n"
"    padding: 8px;\n"
"    padding-left: 15 px;\n"
"    padding-right: 15 px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(1,133,177);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,115,164);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Andreas/PycharmProjects/TarifSimulator_WE/GUI/icons/16x16/cil-folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home_pfz.setIcon(icon2)
        self.pushButton_home_pfz.setObjectName("pushButton_home_pfz")
        self.gridLayout_35.addWidget(self.pushButton_home_pfz, 2, 4, 1, 1)
        self.pushButton__home_is = QtWidgets.QPushButton(self.frame_7)
        self.pushButton__home_is.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(1,115,164);   \n"
"    text-align: center;\n"
"    color: rgb(255,255,255);\n"
"    padding: 8px;\n"
"    padding-left: 15 px;\n"
"    padding-right: 15 px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(1,133,177);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,115,164);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Andreas/PycharmProjects/TarifSimulator_WE/GUI/icons/16x16/cil-3d.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton__home_is.setIcon(icon3)
        self.pushButton__home_is.setObjectName("pushButton__home_is")
        self.gridLayout_35.addWidget(self.pushButton__home_is, 2, 1, 1, 1)
        self.pushButton__home_ts = QtWidgets.QPushButton(self.frame_7)
        self.pushButton__home_ts.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(1,115,164);   \n"
"    text-align: center;\n"
"    color: rgb(255,255,255);\n"
"    padding: 8px;\n"
"    padding-left: 15 px;\n"
"    padding-right: 15 px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(1,133,177);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,115,164);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/Andreas/PycharmProjects/TarifSimulator_WE/GUI/icons/16x16/cil-chart-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton__home_ts.setIcon(icon4)
        self.pushButton__home_ts.setObjectName("pushButton__home_ts")
        self.gridLayout_35.addWidget(self.pushButton__home_ts, 2, 0, 1, 1)
        self.gridLayout_30.addWidget(self.frame_7, 1, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_34.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        self.label_14.setMaximumSize(QtCore.QSize(400, 100))
        self.label_14.setStyleSheet("QLabel {\n"
"    color: rgb(235, 102, 38);\n"
"}")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setIndent(0)
        self.label_14.setObjectName("label_14")
        self.gridLayout_34.addWidget(self.label_14, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        self.label_15.setMaximumSize(QtCore.QSize(100, 100))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("C:/Users/Andreas/PycharmProjects/TarifSimulator_WE/GUI/Visuals/WE_icon_bearbeitet.png"))
        self.label_15.setObjectName("label_15")
        self.gridLayout_34.addWidget(self.label_15, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout_30.addWidget(self.frame_6, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 170))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 170))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setMaximumSize(QtCore.QSize(16777215, 150))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Andreas/PycharmProjects/TarifSimulator_WE/GUI/Visuals/Banner_Tariflinge.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_27.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_30.addWidget(self.frame_5, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton__home_iv.setText(_translate("Form", "Indexvergleich"))
        self.pushButton__home_tv.setText(_translate("Form", "Tarifvergleich"))
        self.pushButton_home_pfz.setText(_translate("Form", "Portfoliozusammenfassung"))
        self.pushButton__home_is.setText(_translate("Form", "Indexsimulation"))
        self.pushButton__home_ts.setText(_translate("Form", "Tarifsimulation"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt;\">TARIFSIMULATOR</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MainMenuView()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
