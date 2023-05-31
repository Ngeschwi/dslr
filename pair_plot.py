
import matplotlib.pyplot as plt
from utils import *
from utilsData import *


def pairPlot(_dataColumnsInfo, _data, _coursesName):
    _fig, _axes = plt.subplots(len(_coursesName), len(_coursesName), figsize=(20, 20))
    for i in range(len(_coursesName)):
        for j in range(len(_coursesName)):
            _dataColumnsInfo1, _dataColumnsInfo2 = RectifyData(_dataColumnsInfo[i][1:], _dataColumnsInfo[j][1:])
            printPairPlot(_dataColumnsInfo1, _dataColumnsInfo2, _data[i], _data[j], _axes[i][j])
            if i == 0:
                _axes[i][j].set_title(_coursesName[j])
            if j == 0:
                _axes[i][j].set_ylabel(_coursesName[i])
            else:
                _axes[i][j].get_yaxis().set_visible(False)
    plt.tight_layout()
    plt.show()


data = defineData('datasets/dataset_train.csv')
dataColumns = createColumns(data)
dataColumnsCourses = dataColumns[6:]
dataColumnsCourses = stringToFloat(dataColumnsCourses)

pairPlot(dataColumns[6:], data, data[0][6:])
