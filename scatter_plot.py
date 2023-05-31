
import matplotlib.pyplot as plt
from utils import *
from utilsData import *

data = defineData('datasets/dataset_train.csv')
dataColumns = createColumns(data)
dataColumnsCourses = dataColumns[6:]
dataColumnsCourses = stringToFloat(dataColumnsCourses)

data1, data2 = RectifyData(dataColumnsCourses[7][1:], dataColumnsCourses[9][1:])

printScatterPlot(data1, data2, data[0][7], data[0][9])
printScatterPlot(data2, data1, data[0][9], data[0][7])
