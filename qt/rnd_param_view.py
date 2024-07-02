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
        Form.resize(1463, 624)
        self.gridLayout_10 = QtWidgets.QGridLayout(Form)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.toolButton_result = QtWidgets.QToolButton(Form)
        self.toolButton_result.setStyleSheet("background-color: rgb(46, 194, 126);")
        self.toolButton_result.setObjectName("toolButton_result")
        self.gridLayout_4.addWidget(self.toolButton_result, 0, 5, 1, 1)
        self.lineEdit_path = QtWidgets.QLineEdit(Form)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.gridLayout_4.addWidget(self.lineEdit_path, 0, 0, 1, 1)
        self.toolButton_rm_check = QtWidgets.QToolButton(Form)
        self.toolButton_rm_check.setStyleSheet("background-color: rgb(220, 138, 221);")
        self.toolButton_rm_check.setText("")
        self.toolButton_rm_check.setObjectName("toolButton_rm_check")
        self.gridLayout_4.addWidget(self.toolButton_rm_check, 0, 6, 1, 1)
        self.toolButton_dict2 = QtWidgets.QToolButton(Form)
        self.toolButton_dict2.setStyleSheet("background-color: rgb(28, 113, 216);")
        self.toolButton_dict2.setObjectName("toolButton_dict2")
        self.gridLayout_4.addWidget(self.toolButton_dict2, 0, 4, 1, 1)
        self.toolButton_dict1 = QtWidgets.QToolButton(Form)
        self.toolButton_dict1.setStyleSheet("background-color: rgb(192, 28, 40);")
        self.toolButton_dict1.setObjectName("toolButton_dict1")
        self.gridLayout_4.addWidget(self.toolButton_dict1, 0, 3, 1, 1)
        self.pushButton_open_file = QtWidgets.QPushButton(Form)
        self.pushButton_open_file.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.gridLayout_4.addWidget(self.pushButton_open_file, 0, 1, 1, 1)
        self.pushButton_xlsx = QtWidgets.QPushButton(Form)
        self.pushButton_xlsx.setStyleSheet("background-color: rgb(38, 162, 105);")
        self.pushButton_xlsx.setObjectName("pushButton_xlsx")
        self.gridLayout_4.addWidget(self.pushButton_xlsx, 0, 2, 1, 1)
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
        self.gridLayout_3.setRowStretch(0, 3)
        self.gridLayout_3.setRowStretch(1, 4)
        self.gridLayout_6.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.toolButton_draw_graph = QtWidgets.QToolButton(Form)
        self.toolButton_draw_graph.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.toolButton_draw_graph.setText("")
        self.toolButton_draw_graph.setObjectName("toolButton_draw_graph")
        self.gridLayout_5.addWidget(self.toolButton_draw_graph, 0, 21, 1, 1)
        self.comboBox_z = QtWidgets.QComboBox(Form)
        self.comboBox_z.setStyleSheet("background-color: rgb(255, 159, 152);")
        self.comboBox_z.setObjectName("comboBox_z")
        self.comboBox_z.addItem("")
        self.comboBox_z.addItem("")
        self.comboBox_z.addItem("")
        self.comboBox_z.addItem("")
        self.comboBox_z.addItem("")
        self.comboBox_z.addItem("")
        self.comboBox_z.addItem("")
        self.comboBox_z.addItem("")
        self.comboBox_z.addItem("")
        self.comboBox_z.addItem("")
        self.comboBox_z.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_z, 0, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("background-color: rgb(87, 227, 137);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 14, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 8, 1, 1)
        self.doubleSpinBox_from_param = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_from_param.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.doubleSpinBox_from_param.setDecimals(4)
        self.doubleSpinBox_from_param.setObjectName("doubleSpinBox_from_param")
        self.gridLayout_5.addWidget(self.doubleSpinBox_from_param, 0, 13, 1, 1)
        self.doubleSpinBox_to_param = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_to_param.setStyleSheet("background-color: rgb(87, 227, 137);")
        self.doubleSpinBox_to_param.setDecimals(4)
        self.doubleSpinBox_to_param.setObjectName("doubleSpinBox_to_param")
        self.gridLayout_5.addWidget(self.doubleSpinBox_to_param, 0, 15, 1, 1)
        self.comboBox_x = QtWidgets.QComboBox(Form)
        self.comboBox_x.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.comboBox_x.setObjectName("comboBox_x")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_x, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setStyleSheet("background-color: rgb(255, 159, 152);")
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 7, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 2, 1, 1)
        self.doubleSpinBox_to_z = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_to_z.setStyleSheet("background-color: rgb(246, 97, 81);")
        self.doubleSpinBox_to_z.setDecimals(4)
        self.doubleSpinBox_to_z.setObjectName("doubleSpinBox_to_z")
        self.gridLayout_5.addWidget(self.doubleSpinBox_to_z, 0, 19, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 12, 1, 1)
        self.doubleSpinBox_from_result = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_from_result.setAutoFillBackground(False)
        self.doubleSpinBox_from_result.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.doubleSpinBox_from_result.setDecimals(4)
        self.doubleSpinBox_from_result.setMaximum(1.0)
        self.doubleSpinBox_from_result.setSingleStep(0.001)
        self.doubleSpinBox_from_result.setObjectName("doubleSpinBox_from_result")
        self.gridLayout_5.addWidget(self.doubleSpinBox_from_result, 0, 9, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.doubleSpinBox_to_result = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_to_result.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.doubleSpinBox_to_result.setDecimals(4)
        self.doubleSpinBox_to_result.setMaximum(1.0)
        self.doubleSpinBox_to_result.setSingleStep(0.001)
        self.doubleSpinBox_to_result.setObjectName("doubleSpinBox_to_result")
        self.gridLayout_5.addWidget(self.doubleSpinBox_to_result, 0, 11, 1, 1)
        self.comboBox_y = QtWidgets.QComboBox(Form)
        self.comboBox_y.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.comboBox_y.setObjectName("comboBox_y")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.comboBox_y.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_y, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 10, 1, 1)
        self.label_mean = QtWidgets.QLabel(Form)
        self.label_mean.setObjectName("label_mean")
        self.gridLayout_5.addWidget(self.label_mean, 0, 5, 1, 1)
        self.doubleSpinBox_from_z = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_from_z.setStyleSheet("background-color: rgb(255, 159, 152);")
        self.doubleSpinBox_from_z.setDecimals(4)
        self.doubleSpinBox_from_z.setObjectName("doubleSpinBox_from_z")
        self.gridLayout_5.addWidget(self.doubleSpinBox_from_z, 0, 17, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setStyleSheet("background-color: rgb(255, 159, 152);")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 16, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setStyleSheet("background-color: rgb(246, 97, 81);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 18, 1, 1)
        self.toolButton_3d = QtWidgets.QToolButton(Form)
        self.toolButton_3d.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.toolButton_3d.setObjectName("toolButton_3d")
        self.gridLayout_5.addWidget(self.toolButton_3d, 0, 20, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.gridLayout_6.setRowStretch(1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_6, 0, 1, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_8.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.spinBox_z_size_from = QtWidgets.QSpinBox(Form)
        self.spinBox_z_size_from.setMinimum(1)
        self.spinBox_z_size_from.setMaximum(999)
        self.spinBox_z_size_from.setSingleStep(5)
        self.spinBox_z_size_from.setProperty("value", 10)
        self.spinBox_z_size_from.setObjectName("spinBox_z_size_from")
        self.gridLayout_7.addWidget(self.spinBox_z_size_from, 0, 0, 1, 1)
        self.spinBox_z_size_to = QtWidgets.QSpinBox(Form)
        self.spinBox_z_size_to.setMinimum(1)
        self.spinBox_z_size_to.setMaximum(999)
        self.spinBox_z_size_to.setSingleStep(5)
        self.spinBox_z_size_to.setProperty("value", 350)
        self.spinBox_z_size_to.setObjectName("spinBox_z_size_to")
        self.gridLayout_7.addWidget(self.spinBox_z_size_to, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_8, 0, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_10.addWidget(self.progressBar, 0, 0, 1, 1)
        self.gridLayout_10.setColumnStretch(0, 8)
        self.gridLayout_10.setColumnStretch(1, 1)

        self.retranslateUi(Form)
        self.comboBox_y.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RandomParamView"))
        self.toolButton_result.setText(_translate("Form", "d"))
        self.toolButton_rm_check.setToolTip(_translate("Form", "очистить чекбоксы"))
        self.toolButton_dict2.setText(_translate("Form", "2"))
        self.toolButton_dict1.setText(_translate("Form", "1"))
        self.pushButton_open_file.setText(_translate("Form", "OPEN"))
        self.pushButton_xlsx.setText(_translate("Form", "xlsx"))
        self.toolButton_draw_graph.setToolTip(_translate("Form", "draw graph"))
        self.comboBox_z.setItemText(0, _translate("Form", "off"))
        self.comboBox_z.setItemText(1, _translate("Form", "ROC AUC"))
        self.comboBox_z.setItemText(2, _translate("Form", "PERCENT"))
        self.comboBox_z.setItemText(3, _translate("Form", "ALL PARAM"))
        self.comboBox_z.setItemText(4, _translate("Form", "CATEGORY"))
        self.comboBox_z.setItemText(5, _translate("Form", "sig up"))
        self.comboBox_z.setItemText(6, _translate("Form", "sig down"))
        self.comboBox_z.setItemText(7, _translate("Form", "width"))
        self.comboBox_z.setItemText(8, _translate("Form", "distr"))
        self.comboBox_z.setItemText(9, _translate("Form", "sep"))
        self.comboBox_z.setItemText(10, _translate("Form", "mfcc"))
        self.label_4.setText(_translate("Form", "to Y:"))
        self.label.setText(_translate("Form", "from X:"))
        self.comboBox_x.setItemText(0, _translate("Form", "ROC AUC"))
        self.comboBox_x.setItemText(1, _translate("Form", "PERCENT"))
        self.comboBox_x.setItemText(2, _translate("Form", "RECALL"))
        self.comboBox_x.setItemText(3, _translate("Form", "PRECISION"))
        self.comboBox_x.setItemText(4, _translate("Form", "F1"))
        self.comboBox_x.setItemText(5, _translate("Form", "sig up"))
        self.comboBox_x.setItemText(6, _translate("Form", "sig down"))
        self.comboBox_x.setItemText(7, _translate("Form", "width"))
        self.comboBox_x.setItemText(8, _translate("Form", "distr"))
        self.comboBox_x.setItemText(9, _translate("Form", "sep"))
        self.comboBox_x.setItemText(10, _translate("Form", "mfcc"))
        self.label_7.setText(_translate("Form", "Z:"))
        self.label_6.setText(_translate("Form", "Y:"))
        self.label_3.setText(_translate("Form", "from Y:"))
        self.label_5.setText(_translate("Form", "X:"))
        self.comboBox_y.setItemText(0, _translate("Form", "ALL PARAM"))
        self.comboBox_y.setItemText(1, _translate("Form", "CATEGORY"))
        self.comboBox_y.setItemText(2, _translate("Form", "ROC AUC"))
        self.comboBox_y.setItemText(3, _translate("Form", "PERCENT"))
        self.comboBox_y.setItemText(4, _translate("Form", "RECALL"))
        self.comboBox_y.setItemText(5, _translate("Form", "PRECISION"))
        self.comboBox_y.setItemText(6, _translate("Form", "F1"))
        self.comboBox_y.setItemText(7, _translate("Form", "sig up"))
        self.comboBox_y.setItemText(8, _translate("Form", "sig down"))
        self.comboBox_y.setItemText(9, _translate("Form", "width"))
        self.comboBox_y.setItemText(10, _translate("Form", "distr"))
        self.comboBox_y.setItemText(11, _translate("Form", "sep"))
        self.comboBox_y.setItemText(12, _translate("Form", "mfcc"))
        self.label_2.setText(_translate("Form", "to X:"))
        self.label_mean.setText(_translate("Form", "mean"))
        self.label_9.setText(_translate("Form", "from Z:"))
        self.label_8.setText(_translate("Form", "to Z:"))
        self.toolButton_3d.setText(_translate("Form", "3D"))
        self.label_10.setText(_translate("Form", "Z size:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
