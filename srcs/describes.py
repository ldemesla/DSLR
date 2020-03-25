import csv
import math

def get_mean(data):
    sum_data = 0
    for val in data:
        sum_data += float(val)
    mean = sum_data / len(data)
    return str(mean)

def get_std(data, mean):
    sum_data = 0
    for val in data:
        try:
            sum_data += (float(val) - float(mean)) ** 2
        except:
            pass
    std = math.sqrt(sum_data / len(data))
    return str(std)

def get_min(data):
    minimum = float(data[0])
    for val in data:
        value = float(val)
        if (value < minimum):
            minimum = value
    return str(minimum)

def get_max(data):
    maximum = float(data[0])
    for val in data:
        value = float(val)
        if (value > maximum):
            maximum = value
    return str(maximum)

def get_first(data):
    first = int(len(data) * 0.25)
    return data[first]

def get_second(data):
    second = int(len(data) * 0.5)
    return data[second]

def get_third(data):
    third = int(len(data) * 0.75)
    return data[third]

def join_padding(liste, padding):
    for i in range(len(liste)):
        pad = int((padding - len(liste[i])) / 2)
        for a in range (pad):
            print(" ", end="")
        print(liste[i], end="")
        for b in range(pad):
            print(" ", end="")
    print("\n")

data_dict = {}

with open("../datasets/dataset_train.csv") as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    headers = next(file)
    data = next(file)
    for i in range(len(data)):
        if (i == 0):
            continue
        try:
            float(data[i])
            data_dict[headers[i]] = []
        except:
            pass

with open("../datasets/dataset_train.csv") as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    is_header = True
    for row in file:
        if (is_header):
            is_header = False
        else:
            for i in range(len(row)):
                if headers[i] in data_dict:
                    data_dict[headers[i]].append(row[i])

headers = [""]
for key in data_dict:
    headers.append(key)
    for i in range(len(data_dict[key])):
        if (len(data_dict[key][i]) == 0):
            data_dict[key][i] = 0
        else:
            data_dict[key][i] = float(data_dict[key][i])

final = []
mean = ["mean"]
count = ["count"]
std = ["std"]
min_data = ["min"]
max_data = ["max"]
first = ["25%"]
second = ["50%"]
third = ["75%"]
index = True
i = 0
for key in data_dict:
    data_dict[key].sort()
    count.append(str(len(data_dict[key])))
    mean.append(get_mean(data_dict[key]))
    std.append(get_std(data_dict[key], mean[i]))
    min_data.append(data_dict[key][0])
    max_data.append(data_dict[key][-1])
    first.append(get_first(data_dict[key]))
    second.append(get_second(data_dict[key]))
    third.append(get_third(data_dict[key]))
    i += 1

i = 0
padding = []
for key in headers:
    max_len = 0
    if (len(key) > max_len):
        max_len = len(key)
    if (len(str(mean[i])) > max_len):
        max_len = len(str(mean[i]))
    if (len(str(std[i])) > max_len):
        max_len = len(str(std[i]))
    if (len(str(min_data[i])) > max_len):
        max_len = len(str(min_data[i]))
    if (len(str(max_data[i])) > max_len):
        max_len = len(str(max_data[i]))
    if (len(str(first[i])) > max_len):
        max_len = len(str(first[i]))
    if (len(str(second[i])) > max_len):
        max_len = len(str(second[i]))
    if (len(str(third[i])) > max_len):
        max_len = len(str(third[i]))
    padding.append(max_len + 2)
    i += 1

final.append(headers)
final.append(count)
final.append(mean)
final.append(std)
final.append(min_data)
final.append(max_data)
final.append(first)
final.append(second)
final.append(third)

for i in range(len(final)):
    for j in range(len(final[i])):
        if (j == 0):
            print(final[i][j], end="")
            pad = padding[j] - len(str(final[i][j]))
            for k in range(pad):
                print(" ", end="")
        else:
            pad = padding[j] - len(str(final[i][j]))
            for k in range(pad):
                print(" ", end="")
            print(final[i][j], end="")
    print("\n")
        



