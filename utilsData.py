

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


def initDescribe(_data):
    _dataDescribe = [[] for _i in range(len(_data[0]) + 1 - 6)]

    for _i in range(len(_dataDescribe)):
        _dataDescribe[_i] = [0 for _j in range(9)]

    for _i in range(len(_dataDescribe)):
        if _i != 0:
            _dataDescribe[_i][0] = _data[0][_i + 6 - 1]

    _mapname = ['Feature', 'Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']
    for _i in range(len(_dataDescribe[0])):
        _dataDescribe[0][_i] = _mapname[_i]

    return _dataDescribe


def stringToFloat(_data):
    for _i in range(len(_data)):
        for _j in range(1, len(_data[_i])):
            try:
                _data[_i][_j] = float(_data[_i][_j])
            except ValueError:
                pass
    return _data
