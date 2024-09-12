import json
import os

import pandas as pd

from object import *


def get_width_height_monitor():
    for monitor in get_monitors():
        return monitor.width, monitor.height


def check_encoding(file_name):
    with open(file_name, 'rb') as f:
        return chardet.detect(f.read())['encoding']


def calc_count_all_param(list_param):
    n = 0
    for i in list_param:
        if i.startswith('sig'):
            n += (512 - int(i.split('_')[2]) - int(i.split('_')[3]))
        elif i.startswith('sep') or i.startswith('mfcc') or i.startswith('distr'):
            n += int(i.split('_')[2])
        else:
            n += 1
    return n


def get_num_param(list_param):
    n_sig_up, n_sig_down, n_distr, n_sep, n_mfcc = 0, 0, 0, 0, 0
    for i in list_param:
        if i.startswith('sig'):
            n_sig_up = int(i.split('_')[2])
            n_sig_down = int(i.split('_')[3])
        if i.startswith('distr'):
            try:
                n_distr = int(i.split('_')[2])
            except IndexError:
                print(i)
        if i.startswith('sep'):
            n_sep = int(i.split('_')[2])
        if i.startswith('mfcc'):
            n_mfcc = int(i.split('_')[2])
    return n_sig_up, n_sig_down, n_distr, n_sep, n_mfcc


def parse_file(file_path):
    enc = check_encoding(file_path)
    pd_data = pd.DataFrame(columns=['ROC AUC', 'PERCENT', 'RECALL', 'PRECISION', 'F1', 'MAE', 'MSE', 'R2',
                                    'param', 'CATEGORY', 'ALL PARAM', 'full_param'])
    result = []
    print(0)
    with open(file_path, 'r', encoding=enc) as file:
        lines = file.readlines()
        list_param = []
        ui.progressBar.setMaximum(len(lines))
        if any(line.startswith('recall mean:') for line in lines):
            n_param = 6
        elif any(line.startswith('MSE mean:') for line in lines):
            n_param = 4
        else:
            n_param = 3
        # n_param = 6 if any(line.startswith('recall mean:') for line in lines) else 3
        # n_param = 4 if any(line.startswith('MSE mean:') for line in lines) else 3
        for i in range(len(lines)):
            ui.progressBar.setValue(i)
            if lines[i].startswith("Выбранные параметры:"):
                dict_param = {}
                param_str = [str(i) for i in lines[i+1][2:-3].split("', '")]
                dict_param['param'] = param_str
                list_param.append(param_str)
            if lines[i].startswith("recall mean:"):
                recall_mean = float(lines[i].split("recall mean:")[1].strip().split()[0])
                dict_param['RECALL'] = recall_mean
                list_param.append(recall_mean)
            if lines[i].startswith("precision mean:"):
                precision_mean = float(lines[i].split("precision mean:")[1].strip().split()[0])
                dict_param['PRECISION'] = precision_mean
                list_param.append(precision_mean)
            if lines[i].startswith("f1 mean:"):
                f1_mean = float(lines[i].split("f1 mean:")[1].strip().split()[0])
                dict_param['F1'] = f1_mean
                list_param.append(f1_mean)
            if lines[i].startswith("roc mean:"):
                roc_mean = float(lines[i].split("roc mean:")[1].strip().split()[0])
                dict_param['ROC AUC'] = roc_mean
                list_param.append(roc_mean)
            if lines[i].startswith("percent mean:"):
                percent_mean = float(lines[i].split("percent mean:")[1].strip().split()[0])
                dict_param['PERCENT'] = percent_mean
                list_param.append(percent_mean)
            if lines[i].startswith("MAE mean:"):
                mae_mean = float(lines[i].split("MAE mean:")[1].strip().split()[0])
                dict_param['MAE'] = mae_mean
                list_param.append(mae_mean)
            if lines[i].startswith("MSE mean:"):
                mse_mean = float(lines[i].split("MSE mean:")[1].strip().split()[0])
                dict_param['MSE'] = mse_mean
                list_param.append(mse_mean)
            if lines[i].startswith("R2 mean:"):
                r2_mean = float(lines[i].split("R2 mean:")[1].strip().split()[0])
                dict_param['R2'] = r2_mean
                list_param.append(r2_mean)
            if len(list_param) == n_param:
                list_param = dict_param['param']
                n_sig_up, n_sig_down, n_distr, n_sep, n_mfcc = get_num_param(list_param)
                dict_param['CATEGORY'] = len(list_param)
                dict_param['ALL PARAM'] = calc_count_all_param(list_param)
                dict_param['full_param'] = '//'.join(list_param)
                dict_param['param'] = clear_list_param(list_param)
                dict_param['sig up'] = n_sig_up
                dict_param['sig down'] = n_sig_down
                dict_param['width'] = 512 - (n_sig_down + n_sig_up)
                dict_param['distr'] = n_distr
                dict_param['sep'] = n_sep
                dict_param['mfcc'] = n_mfcc

                pd_data = pd.concat([pd_data, pd.DataFrame([dict_param])], ignore_index=True)
                list_param = []
    pd_data.to_excel('test.xlsx')
    return pd_data


def parse_folder(file_path):
    pd_data = pd.DataFrame(
        columns=['ROC AUC', 'PERCENT', 'RECALL', 'PRECISION', 'F1', 'MAE', 'MSE', 'R2',
                 'param', 'CATEGORY', 'ALL PARAM', 'full_param'])
    print('parse_folder', file_path)
    dir_list = os.listdir(file_path)
    for file in dir_list:
        if not file.endswith('.txt'):
            continue
        file = file_path + '/' + file
        with open(file, 'r'):
            pd_data = pd.concat([pd_data, parse_file(file)], ignore_index=True)
    path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Excel Files (*.xlsx);;All Files (*)")
    if path == '':
        return
    print('data saving')
    try:
        pd_data.to_excel(path, index=False, engine='openpyxl')
    except:
        pd_data.to_excel(path, index=False)
    print('saved')
    return pd_data


def clear_list_param(list_param):
    new_list_param = []
    for s in list_param:
        if s in list_all_additional_features:
            new_list_param.append(s)
            continue
        parts = s.split('_')
        processed_parts = [re.sub(r'\d+', '', part) for part in parts]
        new_string = '_'.join(processed_parts)
        if new_string.endswith('__'):
            new_string = new_string[:-2]
        if new_string.endswith('_'):
            new_string = new_string[:-1]
        new_list_param.append(new_string)

    return new_list_param


def find_common_param(list_param):
    flattened_list = [item for sublist in list_param for item in sublist]
    common_param = Counter(flattened_list)
    return common_param











