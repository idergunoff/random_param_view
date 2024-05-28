from func import *


Form.show()
Form.setAttribute(Qt.WA_DeleteOnClose)

m_width, m_height = get_width_height_monitor()
Form.resize(int(m_width/1.2), int(m_height/1.2))

figure_am = plt.figure()
canvas_am = FigureCanvas(figure_am)
ui.horizontalLayout_all_model.addWidget(canvas_am)
ax_am = figure_am.add_subplot(111)

figure_zoom = plt.figure()
canvas_zoom = FigureCanvas(figure_zoom)
ui.horizontalLayout_zoom.addWidget(canvas_zoom)

figure_cb = plt.figure()
canvas_cb = FigureCanvas(figure_cb)
ui.horizontalLayout_count_bar.addWidget(canvas_cb)


def open_file():
    global pd_data
    path = QFileDialog.getOpenFileName()[0]
    ui.lineEdit_path.setText(path)
    pd_data = parse_file(path)
    print(pd_data['param'])
    set_spin_value()
    draw_graph_all_model()



def set_spin_value():
    global pd_data
    if ui.checkBox_result.isChecked():
        ui.doubleSpinBox_from_result.setValue(pd_data['percent_mean'].min())
        ui.doubleSpinBox_to_result.setValue(pd_data['percent_mean'].max())
    else:
        ui.doubleSpinBox_from_result.setValue(pd_data['roc_mean'].min())
        ui.doubleSpinBox_to_result.setValue(pd_data['roc_mean'].max())
    if ui.checkBox_param.isChecked():
        ui.spinBox_from_param.setValue(pd_data['count_cat'].min())
        ui.spinBox_to_param.setValue(pd_data['count_cat'].max())
    else:
        ui.spinBox_from_param.setValue(pd_data['count_param'].min())
        ui.spinBox_to_param.setValue(pd_data['count_param'].max())




def draw_graph_all_model():
    global pd_data

    ax_am.cla()

    x = pd_data['percent_mean'].tolist() if ui.checkBox_result.isChecked() else pd_data['roc_mean'].tolist()
    y = pd_data['count_cat'].tolist() if ui.checkBox_param.isChecked() else pd_data['count_param'].tolist()

    ax_am.scatter(x, y)

    ax_am.grid(True)
    ax_am.set_xlabel(ui.checkBox_result.text())
    ax_am.set_ylabel(ui.checkBox_param.text())

    update_rectangle()

    figure_am.tight_layout()
    canvas_am.draw()



def update_rectangle():
    rect = (patches.Rectangle((ui.doubleSpinBox_from_result.value(), ui.spinBox_from_param.value()),
                              ui.doubleSpinBox_to_result.value() - ui.doubleSpinBox_from_result.value(),
                              ui.spinBox_to_param.value() - ui.spinBox_from_param.value(), linewidth=1, edgecolor='r',
                              facecolor='#ffc673', alpha=0.2))

    ax_am.add_patch(rect)

def click_checkbox_result():
    if ui.checkBox_result.isChecked():
        ui.checkBox_result.setText('PERCENT')
    else:
        ui.checkBox_result.setText('ROC AUC')
    set_spin_value()
    draw_graph_all_model()


def click_checkbox_param():
    if ui.checkBox_param.isChecked():
        ui.checkBox_param.setText('CATEGORY')
        ui.spinBox_from_param.setSingleStep(1)
        ui.spinBox_to_param.setSingleStep(1)
    else:
        ui.checkBox_param.setText('ALL PARAM')
        ui.spinBox_from_param.setSingleStep(10)
        ui.spinBox_to_param.setSingleStep(10)
    set_spin_value()
    draw_graph_all_model()

def set_min_max_result():
    ui.doubleSpinBox_to_result.setMinimum(ui.doubleSpinBox_from_result.value())
    ui.doubleSpinBox_from_result.setMaximum(ui.doubleSpinBox_to_result.value())


def set_min_max_param():
    ui.spinBox_to_param.setMinimum(ui.spinBox_from_param.value())
    ui.spinBox_from_param.setMaximum(ui.spinBox_to_param.value())



ui.checkBox_result.stateChanged.connect(click_checkbox_result)
ui.checkBox_param.stateChanged.connect(click_checkbox_param)
ui.pushButton_open_file.clicked.connect(open_file)
ui.doubleSpinBox_from_result.valueChanged.connect(set_min_max_result)
ui.doubleSpinBox_to_result.valueChanged.connect(set_min_max_result)
ui.spinBox_from_param.valueChanged.connect(set_min_max_param)
ui.spinBox_to_param.valueChanged.connect(set_min_max_param)i
ui.doubleSpinBox_to_result.valueChanged.connect(draw_graph_all_model)
ui.doubleSpinBox_from_result.valueChanged.connect(draw_graph_all_model)
ui.spinBox_to_param.valueChanged.connect(draw_graph_all_model)
ui.spinBox_from_param.valueChanged.connect(draw_graph_all_model)

sys.exit(app.exec_())