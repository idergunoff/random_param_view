# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/rnd_param_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(957, 624)
        self.gridLayout_7 = QtWidgets.QGridLayout(Form)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_path = QtWidgets.QLineEdit(Form)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.gridLayout_4.addWidget(self.lineEdit_path, 0, 0, 1, 1)
        self.pushButton_open_file = QtWidgets.QPushButton(Form)
        self.pushButton_open_file.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.gridLayout_4.addWidget(self.pushButton_open_file, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_all_model = QtWidgets.QHBoxLayout()
        self.horizontalLayout_all_model.setObjectName("horizontalLayout_all_model")
        self.gridLayout.addLayout(self.horizontalLayout_all_model, 0, 0, 1, 1)
        self.horizontalLayout_zoom = QtWidgets.QHBoxLayout()
        self.horizontalLayout_zoom.setObjectName("horizontalLayout_zoom")
        self.gridLayout.addLayout(self.horizontalLayout_zoom, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_count_bar = QtWidgets.QHBoxLayout()
        self.horizontalLayout_count_bar.setObjectName("horizontalLayout_count_bar")
        self.gridLayout_2.addLayout(self.horizontalLayout_count_bar, 0, 0, 1, 1)
        self.horizontalLayout_distr = QtWidgets.QHBoxLayout()
        self.horizontalLayout_distr.setObjectName("horizontalLayout_distr")
        self.gridLayout_2.addLayout(self.horizontalLayout_distr, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.spinBox_from_param = QtWidgets.QSpinBox(Form)
        self.spinBox_from_param.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.spinBox_from_param.setMaximum(100000)
        self.spinBox_from_param.setSingleStep(10)
        self.spinBox_from_param.setObjectName("spinBox_from_param")
        self.gridLayout_5.addWidget(self.spinBox_from_param, 0, 8, 1, 1)
        self.doubleSpinBox_from_result = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_from_result.setAutoFillBackground(False)
        self.doubleSpinBox_from_result.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.doubleSpinBox_from_result.setDecimals(4)
        self.doubleSpinBox_from_result.setMaximum(1.0)
        self.doubleSpinBox_from_result.setSingleStep(0.001)
        self.doubleSpinBox_from_result.setObjectName("doubleSpinBox_from_result")
        self.gridLayout_5.addWidget(self.doubleSpinBox_from_result, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 7, 1, 1)
        self.checkBox_result = QtWidgets.QCheckBox(Form)
        self.checkBox_result.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.checkBox_result.setObjectName("checkBox_result")
        self.gridLayout_5.addWidget(self.checkBox_result, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("background-color: rgb(87, 227, 137);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 9, 1, 1)
        self.spinBox_to_param = QtWidgets.QSpinBox(Form)
        self.spinBox_to_param.setStyleSheet("background-color: rgb(87, 227, 137);")
        self.spinBox_to_param.setMaximum(100000)
        self.spinBox_to_param.setSingleStep(10)
        self.spinBox_to_param.setObjectName("spinBox_to_param")
        self.gridLayout_5.addWidget(self.spinBox_to_param, 0, 10, 1, 1)
        self.doubleSpinBox_to_result = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_to_result.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.doubleSpinBox_to_result.setDecimals(4)
        self.doubleSpinBox_to_result.setMaximum(1.0)
        self.doubleSpinBox_to_result.setSingleStep(0.001)
        self.doubleSpinBox_to_result.setObjectName("doubleSpinBox_to_result")
        self.gridLayout_5.addWidget(self.doubleSpinBox_to_result, 0, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 5, 1, 1)
        self.checkBox_param = QtWidgets.QCheckBox(Form)
        self.checkBox_param.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.checkBox_param.setObjectName("checkBox_param")
        self.gridLayout_5.addWidget(self.checkBox_param, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.gridLayout_6.setRowStretch(1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RandomParamView"))
        self.pushButton_open_file.setText(_translate("Form", "OPEN"))
        self.label.setText(_translate("Form", "from result:"))
        self.label_3.setText(_translate("Form", "from N param:"))
        self.checkBox_result.setText(_translate("Form", "ROC AUC"))
        self.label_4.setText(_translate("Form", "to N param:"))
        self.label_2.setText(_translate("Form", "to result:"))
        self.checkBox_param.setText(_translate("Form", "ALL PARAM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
