from function import *


data = defineData('datasets/dataset_train.csv')
dataColumns = createColumns(data)
dataColumnsCourses = dataColumns[6:]
dataColumnsCourses = number_columns(dataColumnsCourses)







colors = ['red', 'blue', 'green', 'yellow']
houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
dataHouses = dataColumns[1]
dataGradesByHousesInAllCourses = defineDataGradesByHousesInAllCourses(dataColumnsCourses, dataHouses)

printAllHistogram(dataGradesByHousesInAllCourses, colors, houses, data[0][6:])
