
from function import *




data = defineData('datasets/dataset_train.csv')
dataColumns = createColumns(data)
dataColumnsCourses = dataColumns[6:]
dataColumnsCourses = number_columns(dataColumnsCourses)



def pair_plot(_data, labels, filename):
    Label=labels[0][6:]
    _fig, _axes = plt.subplots(len(Label), len(Label), figsize=(20, 20))
    for i in range(len(Label)):
        for j in range(len(Label)):
            _data1, _data2 = Rectify_data(_data[i][1:], _data[j][1:])
            Scatterplot(_data1, _data2, Label[i], Label[j], Label, _axes[i][j])
    plt.show()
    
pair_plot(dataColumnsCourses, data, 'pair_plot.png')