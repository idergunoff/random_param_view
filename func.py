import json

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
    pd_data = pd.DataFrame(columns=['ROC AUC', 'PERCENT', 'param', 'CATEGORY', 'ALL PARAM', 'full_param'])
    result = []
    with open(file_path, 'r', encoding=enc) as file:
        lines = file.readlines()
        list_param = []
        ui.progressBar.setMaximum(len(lines))
        for i in range(len(lines)):
            ui.progressBar.setValue(i)
            if lines[i].startswith("Выбранные параметры:"):
                dict_param = {}
                param_str = [str(i) for i in lines[i+1][2:-3].split("', '")]
                dict_param['param'] = param_str
                list_param.append(param_str)
            if lines[i].startswith("roc mean:"):
                roc_mean = float(lines[i].split("roc mean:")[1].strip().split()[0])
                dict_param['ROC AUC'] = roc_mean
                list_param.append(roc_mean)
            if lines[i].startswith("percent mean:"):
                percent_mean = float(lines[i].split("percent mean:")[1].strip().split()[0])
                dict_param['PERCENT'] = percent_mean
                list_param.append(percent_mean)
            if len(list_param) == 3:
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
    return pd_data


def clear_list_param(list_param):
    new_list_param = []
    for s in list_param:
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















