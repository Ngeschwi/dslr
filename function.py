
import matplotlib.pyplot as plt


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


def number_columns(_data):
    for _i in range(len(_data)):
        for _j in range(1, len(_data[_i])):
            try:
                _data[_i][_j] = float(_data[_i][_j])
            except ValueError:
                pass
    return _data


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
    
def Scatterplot(_data1, _data2, _label1, _label2, Label, axes):
    if _label1 == _label2:
        axes.hist(_data1, bins=50, alpha=0.5, label=_label1)
        axes.set_title(_label1)
    else:
        axes.scatter(_data1, _data2, alpha=0.5)
        axes.set_xlabel(_label1)
        axes.set_ylabel(_label2)
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    
def Rectify_data(_data1,_data2):
    delete_index=[]
    for i in range(len(_data1)):
        if _data1[i] == '' or _data2[i] == '':
            delete_index.append(i)
    for i in range(len(delete_index)):
        del _data1[delete_index[i]]
        del _data2[delete_index[i]]
        delete_index = [x - 1 for x in delete_index]
            

    return _data1,_data2