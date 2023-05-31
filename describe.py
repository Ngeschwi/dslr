
import sys
from utils import *
from utilsData import *

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