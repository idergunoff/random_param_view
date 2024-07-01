import matplotlib.pyplot as plt
import pandas as pd

from func import *


Form.show()

ui.label_8.hide()
ui.label_9.hide()
ui.doubleSpinBox_from_z.hide()
ui.doubleSpinBox_to_z.hide()

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
            l_param = (ui.doubleSpinBox_to_param.value() - ui.doubleSpinBox_from_param.value()) / 2
            ui.doubleSpinBox_to_result.setValue(x + l_result)
            ui.doubleSpinBox_from_result.setValue(x - l_result)
            ui.doubleSpinBox_to_param.setValue(y + l_param)
            ui.doubleSpinBox_from_param.setValue(y - l_param)
        elif event.button == 3:
            x, y = event.xdata, event.ydata
            list_nearest_param, str_param = get_nearest_list_param(x, y)
            ui.lineEdit_path.setText(str_param)
            for i in ui.listWidget.findChildren(QtWidgets.QCheckBox):
                if i.text() in list_nearest_param:
                    i.setChecked(True)
                else:
                    i.setChecked(False)
            draw_graph_all_model()


def on_mouse_move_zoom(event):
    if event.inaxes:
        if event.button == 3:
            x, y = event.xdata, event.ydata
            list_nearest_param, str_param = get_nearest_list_param(x, y)
            ui.lineEdit_path.setText(str_param)
            for i in ui.listWidget.findChildren(QtWidgets.QCheckBox):
                if i.text() in list_nearest_param:
                    i.setChecked(True)
                else:
                    i.setChecked(False)
            draw_graph_all_model()

def get_nearest_list_param(x, y):
    global pd_data

    pd_data_copy = pd_data.copy()
    pd_data_copy['x_norm'] = (pd_data_copy[ui.comboBox_x.currentText()] - pd_data_copy[ui.comboBox_x.currentText()].min()) / (pd_data_copy[ui.comboBox_x.currentText()].max() - pd_data_copy[ui.comboBox_x.currentText()].min())
    pd_data_copy['y_norm'] = (pd_data_copy[ui.comboBox_y.currentText()] - pd_data_copy[ui.comboBox_y.currentText()].min()) / (pd_data_copy[ui.comboBox_y.currentText()].max() - pd_data_copy[ui.comboBox_y.currentText()].min())
    x_norm = (x - pd_data_copy[ui.comboBox_x.currentText()].min()) / (pd_data_copy[ui.comboBox_x.currentText()].max() - pd_data_copy[ui.comboBox_x.currentText()].min())
    y_norm = (y - pd_data_copy[ui.comboBox_y.currentText()].min()) / (pd_data_copy[ui.comboBox_y.currentText()].max() - pd_data_copy[ui.comboBox_y.currentText()].min())

    pd_data_copy['distance'] = ((pd_data_copy['x_norm'] - x_norm) ** 2 + (pd_data_copy['y_norm'] - y_norm) ** 2) ** 0.5
    list_param = pd_data_copy['param'].loc[pd_data_copy['distance'] == pd_data_copy['distance'].min()].values[0]
    str_param = pd_data_copy['full_param'].loc[pd_data_copy['distance'] == pd_data_copy['distance'].min()].values[0]

    return list_param, str_param



def open_file():
    global pd_data
    path = QFileDialog.getOpenFileName()[0]
    if path == '':
        return
    ui.lineEdit_path.setText(path)
    pd_data = parse_file(path)

    fill_list_param(sorted(get_list_param()))

    set_spin_value()
    draw_graph_all_model()



def set_spin_value():
    global pd_data

    if ui.comboBox_x.currentText() in ['sig up', 'sig down', 'distr', 'sep', 'mfcc', 'width']:
        ui.doubleSpinBox_from_result.setMaximum(1000)
        ui.doubleSpinBox_to_result.setMaximum(1000)
    else:
        ui.doubleSpinBox_from_result.setMaximum(1)
        ui.doubleSpinBox_to_result.setMaximum(1)

    if ui.comboBox_y.currentText() in ['sig up', 'sig down', 'distr', 'sep', 'mfcc', 'ALL PARAM', 'CATEGORY', 'width']:
        ui.doubleSpinBox_from_param.setMaximum(5000)
        ui.doubleSpinBox_to_param.setMaximum(5000)
    else:
        ui.doubleSpinBox_from_param.setMaximum(1)
        ui.doubleSpinBox_to_param.setMaximum(1)

    if ui.comboBox_y.currentText() in ['sig up', 'sig down', 'distr', 'sep', 'mfcc', 'CATEGORY', 'width']:
        ui.doubleSpinBox_from_param.setSingleStep(1)
        ui.doubleSpinBox_to_param.setSingleStep(1)
    elif ui.comboBox_y.currentText() in ['ALL PARAM']:
        ui.doubleSpinBox_from_param.setSingleStep(10)
        ui.doubleSpinBox_to_param.setSingleStep(10)
    else:
        ui.doubleSpinBox_from_param.setSingleStep(0.001)
        ui.doubleSpinBox_to_param.setSingleStep(0.001)

    if ui.comboBox_z.currentText() != 'off':
        ui.doubleSpinBox_from_z.setMaximum(pd_data[ui.comboBox_z.currentText()].max())
        ui.doubleSpinBox_to_z.setMaximum(pd_data[ui.comboBox_z.currentText()].max())


        if ui.comboBox_z.currentText() in ['sig up', 'sig down', 'distr', 'sep', 'mfcc', 'CATEGORY', 'width']:
            ui.doubleSpinBox_from_z.setSingleStep(1)
            ui.doubleSpinBox_to_z.setSingleStep(1)
        elif ui.comboBox_z.currentText() in ['ALL PARAM']:
            ui.doubleSpinBox_from_z.setSingleStep(10)
            ui.doubleSpinBox_to_z.setSingleStep(10)
        else:
            ui.doubleSpinBox_from_z.setSingleStep(0.001)
            ui.doubleSpinBox_to_z.setSingleStep(0.001)

        ui.doubleSpinBox_from_z.setValue(pd_data[ui.comboBox_z.currentText()].min())
        ui.doubleSpinBox_to_z.setValue(pd_data[ui.comboBox_z.currentText()].max())

    ui.doubleSpinBox_from_result.setValue(pd_data[ui.comboBox_x.currentText()].min())
    ui.doubleSpinBox_to_result.setValue(pd_data[ui.comboBox_x.currentText()].max())

    ui.doubleSpinBox_from_param.setValue(pd_data[ui.comboBox_y.currentText()].min())
    ui.doubleSpinBox_to_param.setValue(pd_data[ui.comboBox_y.currentText()].max())


def draw_graph_all_model():
    global pd_data

    ax_am.cla()

    update_rectangle()

    if ui.comboBox_z.currentText() != 'off':

        pd_data_copy = pd_data.copy()
        pd_data_copy = pd_data_copy.loc[pd_data_copy[ui.comboBox_z.currentText()] != 0]

        sns.scatterplot(data=pd_data_copy, x=ui.comboBox_x.currentText(), y=ui.comboBox_y.currentText(),
                        hue=ui.comboBox_z.currentText(), sizes=(ui.spinBox_z_size_from.value(), ui.spinBox_z_size_to.value()), size=ui.comboBox_z.currentText(), ax=ax_am,
                        palette='rainbow')

        ui.label_8.show()
        ui.label_9.show()
        ui.doubleSpinBox_from_z.show()
        ui.doubleSpinBox_to_z.show()

    else:
        x = pd_data[ui.comboBox_x.currentText()].tolist()
        y = pd_data[ui.comboBox_y.currentText()].tolist()

        ax_am.scatter(x, y)

        ui.label_8.hide()
        ui.label_9.hide()
        ui.doubleSpinBox_from_z.hide()
        ui.doubleSpinBox_to_z.hide()

    if choose_param():
        x_green = get_value_contain_param(ui.comboBox_x.currentText())
        y_green = get_value_contain_param(ui.comboBox_y.currentText())

        ax_am.scatter(x_green, y_green, c='g')

        x_red = get_value_match_param(ui.comboBox_x.currentText())
        y_red = get_value_match_param(ui.comboBox_y.currentText())

        ax_am.scatter(x_red, y_red, c='r')

        ax_distr.cla()
        sns.histplot(x_green, kde=True, ax=ax_distr, bins=50)
        ax_distr.set_xlim(pd_data[ui.comboBox_x.currentText()].min(), pd_data[ui.comboBox_x.currentText()].max())
        ax_distr.grid(True)
        figure_distr.tight_layout()
        canvas_distr.draw()

    ax_am.grid(True)
    ax_am.set_xlabel(ui.comboBox_x.currentText())
    ax_am.set_ylabel(ui.comboBox_y.currentText())


    figure_am.tight_layout()
    canvas_am.draw()

    draw_zoom()
    draw_count_bar()


def draw_graph():
    global pd_data

    fig, ax_out = plt.subplots()

    # x = pd_data[ui.comboBox_x.currentText()].tolist()
    # y = pd_data[ui.comboBox_y.currentText()].tolist()
    if ui.comboBox_z.currentText() == 'off':

        x = pd_data[ui.comboBox_x.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].tolist()
        y = pd_data[ui.comboBox_y.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].tolist()

        ax_out.scatter(x, y)

    # if ui.comboBox_z.currentText() != 'off':
    #
    #     pd_data_copy = pd_data.copy()
    #     pd_data_copy = pd_data_copy.loc[pd_data_copy[ui.comboBox_z.currentText()] != 0]
    else:

        x = pd_data[ui.comboBox_x.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
            pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
            pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()

        y = pd_data[ui.comboBox_y.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
            pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
            pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()

        z = pd_data[ui.comboBox_z.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
            pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
            pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()

        pd_data_copy = pd.DataFrame({ui.comboBox_x.currentText(): x, ui.comboBox_y.currentText(): y, ui.comboBox_z.currentText(): z})

        sns.scatterplot(data=pd_data_copy, x=ui.comboBox_x.currentText(), y=ui.comboBox_y.currentText(),
                        hue=ui.comboBox_z.currentText(), sizes=(ui.spinBox_z_size_from.value(), ui.spinBox_z_size_to.value()), size=ui.comboBox_z.currentText(), ax=ax_out,
                        palette='rainbow')


    ax_out.grid(True)
    ax_out.set_xlabel(ui.comboBox_x.currentText())
    ax_out.set_ylabel(ui.comboBox_y.currentText())

    fig.tight_layout()
    fig.show()


def draw_3d():
    global pd_data

    if ui.comboBox_z.currentText() == 'off':
        return

    x = pd_data[ui.comboBox_x.currentText()].loc[
        pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
        pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
        pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
        pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
        pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
        pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()

    y = pd_data[ui.comboBox_y.currentText()].loc[
        pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
        pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
        pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
        pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
        pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
        pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()

    z = pd_data[ui.comboBox_z.currentText()].loc[
        pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
        pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
        pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
        pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
        pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
        pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()


    fig3d = plt.figure()
    ax3d = fig3d.add_subplot(projection='3d')
    ax3d.scatter(x, y, z, c=z, s=100, cmap='rainbow', alpha=0.6)
    ax3d.set_xlabel(ui.comboBox_x.currentText())
    ax3d.set_ylabel(ui.comboBox_y.currentText())
    ax3d.set_zlabel(ui.comboBox_z.currentText())

    fig3d.tight_layout()
    fig3d.show()


def draw_zoom():
    global pd_data

    ax_zoom.cla()
    if ui.comboBox_z.currentText() == 'off':
        x = pd_data[ui.comboBox_x.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].tolist()
        y = pd_data[ui.comboBox_y.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].tolist()

    else:
        x = pd_data[ui.comboBox_x.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
            pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
            pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()

        y = pd_data[ui.comboBox_y.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
            pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
            pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()


    ax_zoom.scatter(x, y)

    if choose_param():
        x_red = get_value_match_param(ui.comboBox_x.currentText())
        y_red = get_value_match_param(ui.comboBox_y.currentText())

        x_green = get_value_contain_param(ui.comboBox_x.currentText())
        y_green = get_value_contain_param(ui.comboBox_y.currentText())

        x_red_zoom, y_red_zoom, x_green_zoom, y_green_zoom = [], [], [], []

        for i in range(len(x_red)):
            if x_red[i] in x and y_red[i] in y:
                x_red_zoom.append(x_red[i])
                y_red_zoom.append(y_red[i])

        for i in range(len(x_green)):
            if x_green[i] in x and y_green[i] in y:
                x_green_zoom.append(x_green[i])
                y_green_zoom.append(y_green[i])

        ax_zoom.scatter(x_green_zoom, y_green_zoom, c='g')
        ax_zoom.scatter(x_red_zoom, y_red_zoom, c='r')

    if ui.comboBox_z.currentText() != 'off':
        x = pd_data[ui.comboBox_x.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
            pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
            pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()

        y = pd_data[ui.comboBox_y.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
            pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
            pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()

        z = pd_data[ui.comboBox_z.currentText()].loc[
            pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
            pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
            pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
            pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].loc[
            pd_data[ui.comboBox_z.currentText()] >= ui.doubleSpinBox_from_z.value()].loc[
            pd_data[ui.comboBox_z.currentText()] <= ui.doubleSpinBox_to_z.value()].tolist()

        pd_zoom = pd.DataFrame({ui.comboBox_x.currentText(): x, ui.comboBox_y.currentText(): y, ui.comboBox_z.currentText(): z})
        sns.scatterplot(data=pd_zoom, x=ui.comboBox_x.currentText(), y=ui.comboBox_y.currentText(),
                        hue=ui.comboBox_z.currentText(), sizes=(ui.spinBox_z_size_from.value(), ui.spinBox_z_size_to.value()), size=ui.comboBox_z.currentText(),
                        ax=ax_zoom, palette='rainbow')
        ui.label_mean.setText(str(round(np.mean(z), 2)))

    ax_zoom.grid(True)
    ax_zoom.set_xlabel(ui.comboBox_x.currentText())
    ax_zoom.set_ylabel(ui.comboBox_y.currentText())

    figure_zoom.tight_layout()
    canvas_zoom.draw()


def draw_count_bar():
    global pd_data

    list_param = pd_data['param'].loc[
        pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
        pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
        pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
        pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].tolist()

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
        pd_data[ui.comboBox_x.currentText()] >= ui.doubleSpinBox_from_result.value()].loc[
        pd_data[ui.comboBox_x.currentText()] <= ui.doubleSpinBox_to_result.value()].loc[
        pd_data[ui.comboBox_y.currentText()] >= ui.doubleSpinBox_from_param.value()].loc[
        pd_data[ui.comboBox_y.currentText()] <= ui.doubleSpinBox_to_param.value()].tolist()

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
    ax_distr.tick_params(axis='x', labelrotation=90, labelsize=8)
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


def get_value_match_param(column_name):
    global pd_data
    list_param = choose_param()
    list_value = []
    for i in pd_data.index:
        if set(pd_data['param'][i]) == set(list_param):
            list_value.append(pd_data[column_name][i])

    return list_value


def check_contain_param(list_all_param, list_curr_param):
    for i in list_curr_param:
        if i not in list_all_param:
            return False
    return True



def update_rectangle():
    rect = (patches.Rectangle((ui.doubleSpinBox_from_result.value(), ui.doubleSpinBox_from_param.value()),
                              ui.doubleSpinBox_to_result.value() - ui.doubleSpinBox_from_result.value(),
                              ui.doubleSpinBox_to_param.value() - ui.doubleSpinBox_from_param.value(), linewidth=1, edgecolor='r',
                              facecolor='#ffc673', alpha=0.2))
    ax_am.add_patch(rect)




def set_min_result():
    # ui.doubleSpinBox_to_result.setMinimum(ui.doubleSpinBox_from_result.value())
    draw_graph_all_model()

def set_max_result():
    # ui.doubleSpinBox_from_result.setMaximum(ui.doubleSpinBox_to_result.value())
    draw_graph_all_model()


def set_min_param():
    # ui.doubleSpinBox_to_param.setMinimum(ui.doubleSpinBox_from_param.value())
    draw_graph_all_model()


def set_max_param():
    # ui.doubleSpinBox_from_param.setMaximum(ui.doubleSpinBox_to_param.value())
    draw_graph_all_model()


def rm_check():
    for i in ui.listWidget.findChildren(QtWidgets.QCheckBox):
        i.setChecked(False)
    draw_graph_all_model()


def save_to_xlsx():
    path = QFileDialog.getSaveFileName()[0]
    if path == '':
        return
    pd_data.to_excel(path, index=False)


def update_z_size():
    if ui.doubleSpinBox_from_z.isVisible():
        draw_graph_all_model()
        draw_zoom()




ui.comboBox_x.currentTextChanged.connect(set_spin_value)
ui.comboBox_y.currentTextChanged.connect(set_spin_value)
ui.comboBox_z.currentTextChanged.connect(set_spin_value)
ui.comboBox_x.currentTextChanged.connect(draw_graph_all_model)
ui.comboBox_y.currentTextChanged.connect(draw_graph_all_model)
ui.comboBox_z.currentTextChanged.connect(draw_graph_all_model)

ui.pushButton_open_file.clicked.connect(open_file)

ui.doubleSpinBox_from_result.valueChanged.connect(set_min_result)
ui.doubleSpinBox_to_result.valueChanged.connect(set_max_result)
ui.doubleSpinBox_from_param.valueChanged.connect(set_min_param)
ui.doubleSpinBox_to_param.valueChanged.connect(set_max_param)
ui.doubleSpinBox_from_z.valueChanged.connect(draw_graph_all_model)
ui.doubleSpinBox_to_z.valueChanged.connect(draw_graph_all_model)

ui.spinBox_z_size_from.valueChanged.connect(update_z_size)
ui.spinBox_z_size_to.valueChanged.connect(update_z_size)

ui.toolButton_rm_check.clicked.connect(rm_check)

ui.toolButton_dict1.clicked.connect(calc_freq_param_in_area1)
ui.toolButton_dict2.clicked.connect(calc_freq_param_in_area2)
ui.toolButton_result.clicked.connect(calc_freq_param_result)

ui.toolButton_draw_graph.clicked.connect(draw_graph)
ui.toolButton_3d.clicked.connect(draw_3d)

ui.pushButton_xlsx.clicked.connect(save_to_xlsx)

figure_am.canvas.mpl_connect('button_press_event', on_mouse_move)
figure_zoom.canvas.mpl_connect('button_press_event', on_mouse_move_zoom)

sys.exit(app.exec_())