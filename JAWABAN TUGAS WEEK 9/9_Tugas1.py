from array import array

data_list = [100, 200, 300, 400]
data_array = array('i', data_list)

data_list.append(500)
data_array.append(600)

data_array[0] = "Seratus"