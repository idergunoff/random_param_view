from func import *


Form.show()
Form.setAttribute(Qt.WA_DeleteOnClose)

m_width, m_height = get_width_height_monitor()
Form.resize(int(m_width/1.2), int(m_height/1.2))

def open_file():
    path = QFileDialog.getOpenFileName()[0]
    ui.lineEdit_path.setText(path)
    pd_data = parse_file(path)
    print(pd_data)






ui.pushButton_open_file.clicked.connect(open_file)
sys.exit(app.exec_())