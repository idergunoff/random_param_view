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
ax_zoom = figure_zoom.add_subplot(111)

figure_cb = plt.figure()
canvas_cb = FigureCanvas(figure_cb)
ui.horizontalLayout_count_bar.addWidget(canvas_cb)
ax_cb = figure_cb.add_subplot(111)


def open_file():
    global pd_data
    path = QFileDialog.getOpenFileName()[0]
    ui.lineEdit_path.setText(path)
    pd_data = parse_file(path)
    set_spin_value()
    draw_graph_all_model()



def set_spin_value():
    global pd_data

    ui.doubleSpinBox_from_result.setValue(pd_data[ui.checkBox_result.text()].min())
    ui.doubleSpinBox_to_result.setValue(pd_data[ui.checkBox_result.text()].max())

    ui.spinBox_from_param.setValue(pd_data[ui.checkBox_param.text()].min())
    ui.spinBox_to_param.setValue(pd_data[ui.checkBox_param.text()].max())


def draw_graph_all_model():
    global pd_data

    ax_am.cla()

    x = pd_data[ui.checkBox_result.text()].tolist()
    y = pd_data[ui.checkBox_param.text()].tolist()

    ax_am.scatter(x, y)

    ax_am.grid(True)
    ax_am.set_xlabel(ui.checkBox_result.text())
    ax_am.set_ylabel(ui.checkBox_param.text())

    update_rectangle()

    figure_am.tight_layout()
    canvas_am.draw()

    draw_zoom()


def draw_zoom():
    global pd_data

    ax_zoom.cla()

    x = pd_data[ui.checkBox_result.text()].loc[
        pd_data[ui.checkBox_result.text()] >= ui.doubleSpinBox_from_result.value()].loc[
        pd_data[ui.checkBox_result.text()] <= ui.doubleSpinBox_to_result.value()].loc[
        pd_data[ui.checkBox_param.text()] >= ui.spinBox_from_param.value()].loc[
        pd_data[ui.checkBox_param.text()] <= ui.spinBox_to_param.value()].tolist()
    y = pd_data[ui.checkBox_param.text()].loc[
        pd_data[ui.checkBox_result.text()] >= ui.doubleSpinBox_from_result.value()].loc[
        pd_data[ui.checkBox_result.text()] <= ui.doubleSpinBox_to_result.value()].loc[
        pd_data[ui.checkBox_param.text()] >= ui.spinBox_from_param.value()].loc[
        pd_data[ui.checkBox_param.text()] <= ui.spinBox_to_param.value()].tolist()

    ax_zoom.scatter(x, y)

    ax_zoom.grid(True)
    ax_zoom.set_xlabel(ui.checkBox_result.text())
    ax_zoom.set_ylabel(ui.checkBox_param.text())

    figure_zoom.tight_layout()
    canvas_zoom.draw()




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
ui.spinBox_to_param.valueChanged.connect(set_min_max_param)
ui.doubleSpinBox_to_result.valueChanged.connect(draw_graph_all_model)
ui.doubleSpinBox_from_result.valueChanged.connect(draw_graph_all_model)
ui.spinBox_to_param.valueChanged.connect(draw_graph_all_model)
ui.spinBox_from_param.valueChanged.connect(draw_graph_all_model)

sys.exit(app.exec_())