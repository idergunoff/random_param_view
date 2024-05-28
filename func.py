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


def parse_file(file_path):
    enc = check_encoding(file_path)
    pd_data = pd.DataFrame(columns=['ROC AUC', 'PERCENT', 'param', 'CATEGORY', 'ALL PARAM'])
    result = []
    with open(file_path, 'r', encoding=enc) as file:
        lines = file.readlines()
        list_param = []
        for i in range(len(lines)):
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
                dict_param['CATEGORY'] = len(list_param)
                dict_param['ALL PARAM'] = calc_count_all_param(list_param)

                pd_data = pd.concat([pd_data, pd.DataFrame([dict_param])], ignore_index=True)

                list_param = []
    return pd_data
