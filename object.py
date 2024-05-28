import sys
from screeninfo import get_monitors
import chardet
import pandas as pd
import re
from collections import Counter

from qt.rnd_param_view import *

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QFileDialog, QCheckBox, QListWidgetItem, QApplication, QMessageBox, QColorDialog
from PyQt5.QtGui import QBrush, QColor, QCursor

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.patches as patches



app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
