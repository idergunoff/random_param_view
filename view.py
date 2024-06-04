import matplotlib.pyplot as plt

from func import *


Form.show()

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

figure_distr = plt.figure()
canvas_distr = FigureCanvas(figure_distr)
ui.horizontalLayout_distr.addWidget(canvas_distr)
ax_distr = figure_distr.add_subplot(111)


def on_mouse_move(event):
    if event.inaxes:
        if event.button == 1:
            x, y = event.xdata, event.ydata
            l_result = (ui.doubleSpinBox_to_result.value() - ui.doubleSpinBox_from_result.value()) / 2
            l_param = (ui.spinBox_to_param.value() - ui.spinBox_from_param.value()) / 2
            ui.doubleSpinBox_to_result.setValue(x + l_result)
            ui.doubleSpinBox_from_result.setValue(x - l_result)
            ui.spinBox_to_param.setValue(int(y + l_param))
            ui.spinBox_from_param.setValue(int(y - l_param))
        elif event.button == 3:
            x, y = event.xdata, event.ydata
            list_nearest_param = get_nearest_list_param(x, y)
            for i in ui.listWidget.findChildren(QtWidgets.QCheckBox):
                if i.text() in list_nearest_param:
                    i.setChecked(True)
                else:
                    i.setChecked(False)
            draw_graph_all_model()


def get_nearest_list_param(x, y):
    global pd_data

    pd_data_copy = pd_data.copy()
    pd_data_copy['x_norm'] = (pd_data_copy[ui.checkBox_result.text()] - pd_data_copy[ui.checkBox_result.text()].min()) / (pd_data_copy[ui.checkBox_result.text()].max() - pd_data_copy[ui.checkBox_result.text()].min())
    pd_data_copy['y_norm'] = (pd_data_copy[ui.checkBox_param.text()] - pd_data_copy[ui.checkBox_param.text()].min()) / (pd_data_copy[ui.checkBox_param.text()].max() - pd_data_copy[ui.checkBox_param.text()].min())
    x_norm = (x - pd_data_copy[ui.checkBox_result.text()].min()) / (pd_data_copy[ui.checkBox_result.text()].max() - pd_data_copy[ui.checkBox_result.text()].min())
    y_norm = (y - pd_data_copy[ui.checkBox_param.text()].min()) / (pd_data_copy[ui.checkBox_param.text()].max() - pd_data_copy[ui.checkBox_param.text()].min())

    pd_data_copy['distance'] = ((pd_data_copy['x_norm'] - x_norm) ** 2 + (pd_data_copy['y_norm'] - y_norm) ** 2) ** 0.5
    list_param = pd_data_copy['param'].loc[pd_data_copy['distance'] == pd_data_copy['distance'].min()].values[0]

    return list_param



def open_file():
    global pd_data
    path = QFileDialog.getOpenFileName()[0]
    ui.lineEdit_path.setText(path)
    pd_data = parse_file(path)

    fill_list_param(sorted(get_list_param()))

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

    update_rectangle()

    x = pd_data[ui.checkBox_result.text()].tolist()
    y = pd_data[ui.checkBox_param.text()].tolist()

    ax_am.scatter(x, y)

    if choose_param():
        x_red = get_value_contain_param(ui.checkBox_result.text())
        y_red = get_value_contain_param(ui.checkBox_param.text())

        ax_am.scatter(x_red, y_red, c='r')

        ax_distr.cla()
        sns.histplot(x_red, kde=True, ax=ax_distr, bins=50)
        ax_distr.set_xlim(pd_data[ui.checkBox_result.text()].min(), pd_data[ui.checkBox_result.text()].max())
        ax_distr.grid(True)
        figure_distr.tight_layout()
        canvas_distr.draw()

    if not ui.radioButton_off.isChecked():
        num_param = 'off'
        for i in ui.groupBox.findChildren(QtWidgets.QRadioButton):
            if i.isChecked():
                num_param = i.text()

        pd_data_copy = pd_data.copy()
        pd_data_copy = pd_data_copy.loc[pd_data_copy[num_param] != 0]

        print(pd_data_copy)

        sns.scatterplot(data=pd_data_copy, x=ui.checkBox_result.text(), y=ui.checkBox_param.text(), hue=num_param,
                        sizes=(10, 350), size=num_param, ax=ax_am, palette='rainbow')



    ax_am.grid(True)
    ax_am.set_xlabel(ui.checkBox_result.text())
    ax_am.set_ylabel(ui.checkBox_param.text())


    figure_am.tight_layout()
    canvas_am.draw()

    draw_zoom()
    draw_count_bar()


def draw_graph():
    global pd_data

    fig, ax_out = plt.subplots()

    x = pd_data[ui.checkBox_result.text()].tolist()
    y = pd_data[ui.checkBox_param.text()].tolist()

    ax_out.scatter(x, y)

    if not ui.radioButton_off.isChecked():
        num_param = 'off'
        for i in ui.groupBox.findChildren(QtWidgets.QRadioButton):
            if i.isChecked():
                num_param = i.text()

        pd_data_copy = pd_data.copy()
        pd_data_copy = pd_data_copy.loc[pd_data_copy[num_param] != 0]

        print(pd_data_copy)

        sns.scatterplot(data=pd_data_copy, x=ui.checkBox_result.text(), y=ui.checkBox_param.text(), hue=num_param,
                        sizes=(10, 350), size=num_param, ax=ax_out, palette='rainbow')



    ax_out.grid(True)
    ax_out.set_xlabel(ui.checkBox_result.text())
    ax_out.set_ylabel(ui.checkBox_param.text())


    fig.tight_layout()
    fig.show()


def draw_n_graph():
    global pd_data

    fig, ax_out = plt.subplots()

    num_param = ui.checkBox_param.text()
    if not ui.radioButton_off.isChecked():
        for i in ui.groupBox.findChildren(QtWidgets.QRadioButton):
            if i.isChecked():
                num_param = i.text()

    x = pd_data[ui.checkBox_result.text()].tolist()
    y = pd_data[num_param].tolist()

    ax_out.scatter(x, y)

    if not ui.radioButton_off.isChecked():
        pd_data_copy = pd_data.copy()
        pd_data_copy = pd_data_copy.loc[pd_data_copy[num_param] != 0]

        sns.scatterplot(data=pd_data_copy, x=ui.checkBox_result.text(), y=num_param, hue=ui.checkBox_param.text(),
                        sizes=(10, 350), size=ui.checkBox_param.text(), ax=ax_out, palette='rainbow')

    ax_out.grid(True)
    ax_out.set_xlabel(ui.checkBox_result.text())
    ax_out.set_ylabel(num_param)

    fig.tight_layout()
    fig.show()


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

    if choose_param():
        x_red = get_value_contain_param(ui.checkBox_result.text())
        y_red = get_value_contain_param(ui.checkBox_param.text())

        x_red_zoom, y_red_zoom = [], []

        for i in range(len(x_red)):
            if x_red[i] in x and y_red[i] in y:
                x_red_zoom.append(x_red[i])
                y_red_zoom.append(y_red[i])

        ax_zoom.scatter(x_red_zoom, y_red_zoom, c='r')

    ax_zoom.grid(True)
    ax_zoom.set_xlabel(ui.checkBox_result.text())
    ax_zoom.set_ylabel(ui.checkBox_param.text())

    figure_zoom.tight_layout()
    canvas_zoom.draw()


def draw_count_bar():
    global pd_data

    list_param = pd_data['param'].loc[
        pd_data[ui.checkBox_result.text()] >= ui.doubleSpinBox_from_result.value()].loc[
        pd_data[ui.checkBox_result.text()] <= ui.doubleSpinBox_to_result.value()].loc[
        pd_data[ui.checkBox_param.text()] >= ui.spinBox_from_param.value()].loc[
        pd_data[ui.checkBox_param.text()] <= ui.spinBox_to_param.value()].tolist()

    common_param = dict(find_common_param(list_param))
    common_param = sorted(common_param.items(), key=lambda x: x[1], reverse=True)

    ax_cb.cla()
    list_name_param = [elem[0] for elem in common_param]
    checked_param = choose_param()
    color_list = ['#ff9f98' if i in checked_param else '#aad5ff' for i in list_name_param]
    ax_cb.bar(list_name_param, [elem[1] for elem in common_param], color=color_list)
    ax_cb.grid(True)
    ax_cb.tick_params(axis='x', labelrotation=90, labelsize=8)
    ax_cb.set_title(f'Параметры в выделенной области по {len(list_param)} моделям.')

    figure_cb.tight_layout()
    canvas_cb.draw()



def fill_list_param(param):
    ui.listWidget.clear()
    for i in param:
        checkBox_new = QtWidgets.QCheckBox()
        # Задать текст для флажка и радиокнопки
        checkBox_new.setText(i)
        checkBox_new.clicked.connect(draw_graph_all_model)
        listWidgetItem = QtWidgets.QListWidgetItem(ui.listWidget)
        ui.listWidget.setItemWidget(listWidgetItem, checkBox_new)


def get_list_param():
    global pd_data
    common_param = dict(find_common_param(pd_data['param'].tolist()))
    common_param = sorted(common_param.items(), key=lambda x: x[1], reverse=True)

    list_name_param = [elem[0] for elem in common_param]

    return list_name_param


def calc_freq_param(list_param):
    list_all_param = [item for sublist in list_param for item in sublist]
    common_param = dict(find_common_param(list_param))
    for key, value in common_param.items():
        common_param[key] = round(value / len(list_all_param), 5)
    return common_param


def calc_freq_param_in_area():

    global pd_data

    list_param = pd_data['param'].loc[
        pd_data[ui.checkBox_result.text()] >= ui.doubleSpinBox_from_result.value()].loc[
        pd_data[ui.checkBox_result.text()] <= ui.doubleSpinBox_to_result.value()].loc[
        pd_data[ui.checkBox_param.text()] >= ui.spinBox_from_param.value()].loc[
        pd_data[ui.checkBox_param.text()] <= ui.spinBox_to_param.value()].tolist()

    return calc_freq_param(list_param)


def calc_freq_param_in_area1():
    global dict1
    dict1 = calc_freq_param_in_area()


def calc_freq_param_in_area2():
    global dict2
    dict2 = calc_freq_param_in_area()


def calc_freq_param_result():
    global dict1, dict2

    dict_result = {}
    for key, value in dict1.items():
        try:
            dict_result[key] = value - dict2[key]
        except KeyError:
            dict_result[key] = value

    dict_result = sorted(dict_result.items(), key=lambda x: x[1], reverse=True)


    ax_distr.cla()
    ax_distr.bar([elem[0] for elem in dict_result], [elem[1] for elem in dict_result])
    ax_distr.tick_params(axis='x', labelrotation=90)
    ax_distr.grid(True)
    figure_distr.tight_layout()
    canvas_distr.draw()


def choose_param():
    list_checked = []
    for i in ui.listWidget.findChildren(QtWidgets.QCheckBox):
        if i.isChecked():
            list_checked.append(i.text())
    return list_checked


def get_value_contain_param(column_name):
    global pd_data
    list_param = choose_param()
    list_value = []
    for i in pd_data.index:
        if check_contain_param(pd_data['param'][i], list_param):
            list_value.append(pd_data[column_name][i])

    return list_value

def check_contain_param(list_all_param, list_curr_param):
    for i in list_curr_param:
        if i not in list_all_param:
            return False
    return True

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


def set_min_result():
    # ui.doubleSpinBox_to_result.setMinimum(ui.doubleSpinBox_from_result.value())
    draw_graph_all_model()

def set_max_result():
    # ui.doubleSpinBox_from_result.setMaximum(ui.doubleSpinBox_to_result.value())
    draw_graph_all_model()


def set_min_param():
    # ui.spinBox_to_param.setMinimum(ui.spinBox_from_param.value())
    draw_graph_all_model()


def set_max_param():
    # ui.spinBox_from_param.setMaximum(ui.spinBox_to_param.value())
    draw_graph_all_model()


def rm_check():
    for i in ui.listWidget.findChildren(QtWidgets.QCheckBox):
        i.setChecked(False)
    draw_graph_all_model()






ui.checkBox_result.stateChanged.connect(click_checkbox_result)
ui.checkBox_param.stateChanged.connect(click_checkbox_param)
ui.pushButton_open_file.clicked.connect(open_file)

# ui.doubleSpinBox_to_result.valueChanged.connect(draw_graph_all_model)
# ui.doubleSpinBox_from_result.valueChanged.connect(draw_graph_all_model)
# ui.spinBox_to_param.valueChanged.connect(draw_graph_all_model)
# ui.spinBox_from_param.valueChanged.connect(draw_graph_all_model)

ui.doubleSpinBox_from_result.valueChanged.connect(set_min_result)
ui.doubleSpinBox_to_result.valueChanged.connect(set_max_result)
ui.spinBox_from_param.valueChanged.connect(set_min_param)
ui.spinBox_to_param.valueChanged.connect(set_max_param)
ui.toolButton_rm_check.clicked.connect(rm_check)

ui.toolButton_dict1.clicked.connect(calc_freq_param_in_area1)
ui.toolButton_dict2.clicked.connect(calc_freq_param_in_area2)
ui.toolButton_result.clicked.connect(calc_freq_param_result)

ui.radioButton_off.clicked.connect(draw_graph_all_model)
ui.radioButton_distr.clicked.connect(draw_graph_all_model)
ui.radioButton_sep.clicked.connect(draw_graph_all_model)
ui.radioButton_mfcc.clicked.connect(draw_graph_all_model)
ui.radioButton_sig_up.clicked.connect(draw_graph_all_model)
ui.radioButton_sig_down.clicked.connect(draw_graph_all_model)

ui.toolButton_draw_graph.clicked.connect(draw_graph)
ui.pushButton_n_graph.clicked.connect(draw_n_graph)

figure_am.canvas.mpl_connect('button_press_event', on_mouse_move)

sys.exit(app.exec_())