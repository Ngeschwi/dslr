
import matplotlib.pyplot as plt

#
#
#  Describe
#
#


def getCount(_dataColumnsCourses, _index):
    return len(_dataColumnsCourses[_index]) - 1


def getMean(_dataColumnsCourses, _index):
    _sum = 0
    _count = 0
    for _j in range(len(_dataColumnsCourses[_index])):
        if _j != 0:
            if _dataColumnsCourses[_index][_j] != '':
                _sum += float(_dataColumnsCourses[_index][_j])
                _count += 1

    return _sum / _count


def getStd(_dataColumnsCourses, _index):
    _sum = 0
    _count = 0
    _mean = getMean(_dataColumnsCourses, _index)
    for _j in range(1, len(_dataColumnsCourses[_index])):
        if _dataColumnsCourses[_index][_j] != '':
            _sum += (float(_dataColumnsCourses[_index][_j]) - _mean) ** 2
            _count += 1
    return abs((_sum / _count - 1) ** 0.5)


def getMin(_dataColumnsCourses, _index):
    _i = 1
    while _dataColumnsCourses[_index][_i] == '':
        _i += 1
    _min = float(_dataColumnsCourses[_index][_i])

    for _j in range(len(_dataColumnsCourses[_index])):
        if _j != 0:
            if _dataColumnsCourses[_index][_j] != '':
                if float(_dataColumnsCourses[_index][_j]) < _min:
                    _min = float(_dataColumnsCourses[_index][_j])

    return _min


def getList(_dataColumnsCourses, _index):
    _list = []
    for _j in range(len(_dataColumnsCourses[_index])):
        if _j != 0:
            if _dataColumnsCourses[_index][_j] != '':
                _list.append(float(_dataColumnsCourses[_index][_j]))

    _list.sort()
    return _list


def get25(_dataColumnsCourses, _index):
    _list = getList(_dataColumnsCourses, _index)
    return _list[int(len(_list) * 0.25)]


def get50(_dataColumnsCourses, _index):
    _list = getList(_dataColumnsCourses, _index)
    return _list[int(len(_list) * 0.5)]


def get75(_dataColumnsCourses, _index):
    _list = getList(_dataColumnsCourses, _index)
    return _list[int(len(_list) * 0.75)]


def getMax(_dataColumnsCourses, _index):
    _i = 1
    while _dataColumnsCourses[_index][_i] == '':
        _i += 1
    _max = float(_dataColumnsCourses[_index][_i])

    for _j in range(len(_dataColumnsCourses[_index])):
        if _j != 0:
            if _dataColumnsCourses[_index][_j] != '':
                if float(_dataColumnsCourses[_index][_j]) > _max:
                    _max = float(_dataColumnsCourses[_index][_j])

    return _max


#
#
#  Histogram
#
#


def defineDataGradesByHousesInAllCourses(_dataColumnsCourses, _dataHouses):
    _dataGradesByHousesInAllCourses = [[] for _i in range(len(_dataColumnsCourses))]

    for _i in range(len(_dataGradesByHousesInAllCourses)):
        _dataGradesByHousesInAllCourses[_i] = [[] for _ in range(4)]

    for _i in range(len(_dataColumnsCourses)):
        for _j in range(len(_dataColumnsCourses[_i])):
            if _j != 0:
                if _dataColumnsCourses[_i][_j] != '':
                    if _dataHouses[_j] == 'Gryffindor':
                        _dataGradesByHousesInAllCourses[_i][0].append(_dataColumnsCourses[_i][_j])
                    elif _dataHouses[_j] == 'Hufflepuff':
                        _dataGradesByHousesInAllCourses[_i][1].append(_dataColumnsCourses[_i][_j])
                    elif _dataHouses[_j] == 'Ravenclaw':
                        _dataGradesByHousesInAllCourses[_i][2].append(_dataColumnsCourses[_i][_j])
                    elif _dataHouses[_j] == 'Slytherin':
                        _dataGradesByHousesInAllCourses[_i][3].append(_dataColumnsCourses[_i][_j])

    return _dataGradesByHousesInAllCourses


#
#
# print histogram
#
#


def printAllHistogram(_data, _colors, _houses, _courses):
    _fig, _axes = plt.subplots(4, 4)
    _fig.suptitle('Grades by houses in all courses')
    _count = 0

    for _i in range(len(_data)):
        if _i >= 12:
            _count = 3
        elif _i >= 8:
            _count = 2
        elif _i >= 4:
            _count = 1
        for _j in range(len(_data[_i])):
            _axes[_count, _i - _count * 5].hist(_data[_i][_j], bins=50, alpha=0.5, label=_houses[_j], color=_colors[_j])
        _axes[_count, _i - _count * 5].set_title(_courses[_i])
    #_fig.legend(loc='upper left')
    plt.tight_layout()
    plt.show()


#
#
#  Rectify Data
#
#


def RectifyData(_data1, _data2):
    _deletedIndex = []
    for i in range(len(_data1)):
        if _data1[i] == '' or _data2[i] == '':
            _deletedIndex.append(i)

    for i in range(len(_deletedIndex)):
        del _data1[_deletedIndex[i]]
        del _data2[_deletedIndex[i]]
        _deletedIndex = [_i - 1 for _i in _deletedIndex]

    return _data1, _data2


#
#
#  Scatter plot
#
#

def printScatterPlot(_data1, _data2, _label1, _label2):
    plt.scatter(_data1, _data2, alpha=0.5)
    plt.xlabel(_label1)
    plt.ylabel(_label2)
    plt.show()

#
#
#  Pair plot
#
#


def printPairPlot(_data1, _data2, _label1, _label2, _axes):
    if _label1 == _label2:
        _axes.hist(_data1, bins=50, alpha=0.5)
    else:
        _axes.scatter(_data1, _data2, alpha=0.5)
    _axes.get_xaxis().set_visible(False)
