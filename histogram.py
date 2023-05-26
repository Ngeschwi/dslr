
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


data = defineData('datasets/dataset_train.csv')
dataColumns = createColumns(data)
dataColumnsCourses = dataColumns[6:]
dataColumnsCourses = number_columns(dataColumnsCourses)


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
            _axes[_count, _i - _count * 5].hist(_data[_i][_j], bins=50, alpha=0.5, label=houses[_j], color=_colors[_j])
        _axes[_count, _i - _count * 5].set_title(_courses[_i])
    #_fig.legend(loc='upper left')
    plt.tight_layout()
    plt.show()


colors = ['red', 'blue', 'green', 'yellow']
houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
dataHouses = dataColumns[1]
dataGradesByHousesInAllCourses = defineDataGradesByHousesInAllCourses(dataColumnsCourses, dataHouses)

printAllHistogram(dataGradesByHousesInAllCourses, colors, houses, data[0][6:])
