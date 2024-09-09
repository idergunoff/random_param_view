import sys
from screeninfo import get_monitors
import chardet
import pandas as pd
import numpy as np
import re
from collections import Counter

from qt.rnd_param_view import *

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QFileDialog, QCheckBox, QListWidgetItem, QApplication, QMessageBox, QColorDialog
from PyQt5.QtGui import QBrush, QColor, QCursor

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.patches as patches
import seaborn as sns

list_wavelet_features = [
    'wvt_energ_D1', 'wvt_energ_D2', 'wvt_energ_D3', 'wvt_energ_D4', 'wvt_energ_D5', 'wvt_energ_A5',
    'wvt_mean_D1', 'wvt_mean_D2', 'wvt_mean_D3', 'wvt_mean_D4', 'wvt_mean_D5', 'wvt_mean_A5',
    'wvt_max_D1', 'wvt_max_D2', 'wvt_max_D3', 'wvt_max_D4', 'wvt_max_D5', 'wvt_max_A5',
    'wvt_min_D1', 'wvt_min_D2', 'wvt_min_D3', 'wvt_min_D4', 'wvt_min_D5', 'wvt_min_A5',
    'wvt_std_D1', 'wvt_std_D2', 'wvt_std_D3', 'wvt_std_D4', 'wvt_std_D5', 'wvt_std_A5',
    'wvt_skew_D1', 'wvt_skew_D2', 'wvt_skew_D3', 'wvt_skew_D4', 'wvt_skew_D5', 'wvt_skew_A5',
    'wvt_kurt_D1', 'wvt_kurt_D2', 'wvt_kurt_D3', 'wvt_kurt_D4', 'wvt_kurt_D5', 'wvt_kurt_A5',
    'wvt_entr_D1', 'wvt_entr_D2', 'wvt_entr_D3', 'wvt_entr_D4', 'wvt_entr_D5', 'wvt_entr_A5',
    'wvt_energ_D1D2', 'wvt_energ_D2D3', 'wvt_energ_D3D4', 'wvt_energ_D4D5', 'wvt_energ_D5A5',
    'wvt_HfLf_Ratio', 'wvt_HfLf_D1', 'wvt_HfLf_D2', 'wvt_HfLf_D3', 'wvt_HfLf_D4', 'wvt_HfLf_D5'
]


list_fractal_features = [
    'fractal_dim','hurst_exp', 'lacunarity', 'mf_width', 'mf_max_position', 'mf_asymmetry', 'mf_max_height',
    'mf_mean_alpha', 'mf_mean_f_alpha', 'mf_std_alpha', 'mf_std_f_alpha'
]

list_entropy_features = [
    'ent_sh', 'ent_perm', 'ent_appr', 'ent_sample1', 'ent_sample2', 'ent_ms1', 'ent_ms2', 'ent_ms3', 'ent_ms4',
    'ent_ms5', 'ent_ms6', 'ent_ms7', 'ent_ms8', 'ent_ms9', 'ent_ms10', 'ent_fft'
]

list_nonlinear_features = [
    'nln_corr_dim', 'nln_rec_rate', 'nln_determin', 'nln_avg_diag', 'nln_hirsh'
]

list_morphology_feature = [
    'mph_peak_num', 'mph_peak_width', 'mph_peak_amp_ratio', 'mph_peak_asymm', 'mph_peak_steep', 'mph_erosion', 'mph_dilation'
]

list_frequency_feature = [
    'frq_central', 'frq_bandwidth', 'frq_hl_ratio', 'frq_spec_centroid', 'frq_spec_slope', 'frq_spec_entr', 'frq_dom1',
    'frq_dom2', 'frq_dom3', 'frq_mmt1', 'frq_mmt2', 'frq_mmt3', 'frq_attn_coef'
]

list_envelope_feature = [
    'env_area', 'env_max', 'env_t_max', 'env_mean', 'env_std', 'env_skew', 'env_kurt', 'env_max_mean_ratio',
    'env_peak_width', 'env_energy_win1', 'env_energy_win2', 'env_energy_win3'
]

list_autocorr_feature = [
    'acf_first_min', 'acf_lag_10', 'acf_decay', 'acf_integral', 'acf_peak_width', 'acf_ratio'
]

list_emd_feature = [
    'emd_num_imfs',
    'emd_energ_mean', 'emd_energ_med', 'emd_energ_max', 'emd_energ_min', 'emd_energ_std',
    'emd_rel_energ_mean', 'emd_rel_energ_med', 'emd_rel_energ_max', 'emd_rel_energ_min', 'emd_rel_energ_std',
    'emd_dom_freqs_mean', 'emd_dom_freqs_med', 'emd_dom_freqs_max', 'emd_dom_freqs_min', 'emd_dom_freqs_std',
    'emd_mean_corr', 'emd_median_corr', 'emd_max_corr', 'emd_min_corr', 'emd_std_corr',
    'emd_corr_25', 'emd_corr_50', 'emd_corr_75',
    'emd_energ_entropy', 'emd_oi', 'emd_hi'
]

list_hht_feature = [
    'hht_inst_freq_mean', 'hht_inst_freq_med', 'hht_inst_freq_max', 'hht_inst_freq_min', 'hht_inst_freq_std',
    'hht_inst_amp_mean', 'hht_inst_amp_med', 'hht_inst_amp_max', 'hht_inst_amp_min', 'hht_inst_amp_std',
    'hht_mean_freq_mean', 'hht_mean_freq_med', 'hht_mean_freq_max', 'hht_mean_freq_min', 'hht_mean_freq_std',
    'hht_mean_amp_mean', 'hht_mean_amp_med', 'hht_mean_amp_max', 'hht_mean_amp_min', 'hht_mean_amp_std',
    'hht_marg_spec_mean', 'hht_marg_spec_med', 'hht_marg_spec_max', 'hht_marg_spec_min', 'hht_marg_spec_std',
    'hht_teager_energ_mean', 'hht_teager_energ_med', 'hht_teager_energ_max', 'hht_teager_energ_min', 'hht_teager_energ_std',
    'hht_hi',
    'hht_dos_mean', 'hht_dos_med', 'hht_dos_max', 'hht_dos_min', 'hht_dos_std',
    'hht_oi',
    'hht_hsd_mean', 'hht_hsd_med', 'hht_hsd_max', 'hht_hsd_min', 'hht_hsd_std',
    'hht_ci'
]

list_all_additional_features = (list_wavelet_features + list_fractal_features + list_entropy_features +
                                list_nonlinear_features + list_morphology_feature + list_frequency_feature +
                                list_envelope_feature + list_autocorr_feature + list_emd_feature + list_hht_feature)


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
