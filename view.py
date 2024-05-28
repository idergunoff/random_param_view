from func import *


Form.show()
Form.setAttribute(Qt.WA_DeleteOnClose)

m_width, m_height = get_width_height_monitor()
Form.resize(int(m_width/1.2), int(m_height/1.2))

def open_file():
    path = QFileDialog.getOpenFileName()[0]
    ui.lineEdit_path.setText(path)
    pd_data = parse_file(path)
    print(pd_data['param'])

def click_checkbox_result():
    if ui.checkBox_result.isChecked():
        ui.checkBox_result.setText('PERCENT')
    else:
        ui.checkBox_result.setText('ROC AUC')


def click_checkbox_param():
    if ui.checkBox_param.isChecked():
        ui.checkBox_param.setText('CATEGORY')
    else:
        ui.checkBox_param.setText('ALL PARAM')



ui.checkBox_result.stateChanged.connect(click_checkbox_result)
ui.checkBox_param.stateChanged.connect(click_checkbox_param)
ui.pushButton_open_file.clicked.connect(open_file)
sys.exit(app.exec_())