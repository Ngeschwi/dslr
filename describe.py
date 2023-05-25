
import sys


def defineData(_dataPath):
    _data = open(_dataPath, 'r')
    _data = _data.read()
    _data = _data.split('\n')
    
    for i in range(len(_data)):
        _data[i] = _data[i].split(',')
    return _data

def createColumns(_data):
    _dataColumns = [[] for i in range(len(_data[0]))]

    for i in range(len(_data)):
        for j in range(len(_data[i])):
            _dataColumns[j].append(_data[i][j])

    return _dataColumns


def initDescribe(_data):
    _dataDescribe = [[] for i in range(len(_data[0]) + 1 - 6)]

    for i in range(len(_dataDescribe)):
        _dataDescribe[i] = [0 for j in range(9)]

    for i in range(len(_dataDescribe)):
        if i != 0:
            _dataDescribe[i][0] = _data[0][i + 6 - 1]

    _mapname = ['Feature', 'Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']
    for i in range(len(_dataDescribe[0])):
        _dataDescribe[0][i] = _mapname[i]

    return _dataDescribe


def getCount(_dataColumnsCourses, _index):
    return len(_dataColumnsCourses[_index]) - 1
    

def getMean(_dataColumnsCourses, _index):
    _sum = 0
    _count = 0
    for j in range(len(_dataColumnsCourses[_index])):
        if j != 0:
            if _dataColumnsCourses[_index][j] != '':
                _sum += float(_dataColumnsCourses[_index][j])
                _count += 1

    return _sum / _count


def getStd(_dataColumnsCourses, _index):
    _sum = 0
    _count = 0
    _mean = getMean(_dataColumnsCourses, _index)
    for j in range(1, len(_dataColumnsCourses[_index])):
        if _dataColumnsCourses[_index][j] != '':
            _sum += (float(_dataColumnsCourses[_index][j]) - _mean) ** 2
            _count += 1
    return abs((_sum / _count - 1) ** 0.5)


def getMin(_dataColumnsCourses, _index):
    _i = 1
    while _dataColumnsCourses[_index][_i] == '':
        _i += 1
    _min = float(_dataColumnsCourses[_index][_i])

    for j in range(len(_dataColumnsCourses[_index])):
        if j != 0:
            if _dataColumnsCourses[_index][j] != '':
                if float(_dataColumnsCourses[_index][j]) < _min:
                    _min = float(_dataColumnsCourses[_index][j])

    return _min


def get25(_dataColumnsCourses, _index):
    _list = []
    for j in range(len(_dataColumnsCourses[_index])):
        if j != 0:
            if _dataColumnsCourses[_index][j] != '':
                _list.append(float(_dataColumnsCourses[_index][j]))

    _list.sort()
    return _list[int(len(_list) * 0.25)]


def get50(_dataColumnsCourses, _index):
    _list = []
    for j in range(len(_dataColumnsCourses[_index])):
        if j != 0:
            if _dataColumnsCourses[_index][j] != '':
                _list.append(float(_dataColumnsCourses[_index][j]))

    _list.sort()
    return _list[int(len(_list) * 0.5)]


def get75(_dataColumnsCourses, _index):
    _list = []
    for j in range(len(_dataColumnsCourses[_index])):
        if j != 0:
            if _dataColumnsCourses[_index][j] != '':
                _list.append(float(_dataColumnsCourses[_index][j]))

    _list.sort()
    return _list[int(len(_list) * 0.75)]


def getMax(_dataColumnsCourses, _index):
    _i = 1
    while _dataColumnsCourses[_index][_i] == '':
        _i += 1
    _max = float(_dataColumnsCourses[_index][_i])

    for j in range(len(_dataColumnsCourses[_index])):
        if j != 0:
            if _dataColumnsCourses[_index][j] != '':
                if float(_dataColumnsCourses[_index][j]) > _max:
                    _max = float(_dataColumnsCourses[_index][j])

    return _max


if len(sys.argv) != 2:
    print("Usage: python describe.py <datafile>")
    sys.exit(1)
else:
    dataPath = sys.argv[1]

data = defineData(dataPath)
dataColumns = createColumns(data)
dataColumnsCourses = dataColumns[6:]
dataDescribe = initDescribe(data)

for i in range(len(dataDescribe)):
    if i != 0:
        dataDescribe[i][1] = getCount(dataColumnsCourses, i - 1)
        dataDescribe[i][2] = getMean(dataColumnsCourses, i - 1)
        dataDescribe[i][3] = getStd(dataColumnsCourses, i - 1)
        dataDescribe[i][4] = getMin(dataColumnsCourses, i - 1)
        dataDescribe[i][5] = get25(dataColumnsCourses, i - 1)
        dataDescribe[i][6] = get50(dataColumnsCourses, i - 1)
        dataDescribe[i][7] = get75(dataColumnsCourses, i - 1)
        dataDescribe[i][8] = getMax(dataColumnsCourses, i - 1)

finalDataDescribe = createColumns(dataDescribe)

for i in range(len(finalDataDescribe)):
    print(finalDataDescribe[i])