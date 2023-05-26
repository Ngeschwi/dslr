
import sys
import matplotlib.pyplot


def defineData(_dataPath):
    _data = open(_dataPath, 'r')
    _data = _data.read()
    _data = _data.split('\n')

    for _i in range(len(_data)):
        _data[_i] = _data[_i].split(',')
    return _data


def createColumns(_data):
    _dataColumns = [[] for _i in range(len(_data[0]))]

    for _i in range(len(_data)):
        for _j in range(len(_data[_i])):
            _dataColumns[_j].append(_data[_i][_j])

    return _dataColumns


data = defineData('datasets/dataset_train.csv')
dataColumns = createColumns(data)
dataColumnsCourses = dataColumns[6:]
