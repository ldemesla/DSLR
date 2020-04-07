import csv
import math
import sys
import pandas as pd

def get_count(data):
    data = data.dropna()
    count = 0
    for x in data:
        count += 1

def get_mean(data):
    sum_data = 0
    for val in data:
        sum_data += float(val)
    mean = sum_data / len(data)
    return mean

def get_std(data, mean):
    total = 0
    for val in data:
        total = total + (val - mean) ** 2
    return (total / len(data)) ** 0.5

def get_first(data):
    first = int(len(data) * 0.25)
    return data[first]

def get_second(data):
    first = int(len(data) * 0.5)
    return data[first]

def get_third(data):
    first = int(len(data) * 0.75)
    return data[first]

def describes(file_input):
    data_dict = {}
    df = pd.read_csv(file_input)
    df = df.select_dtypes(include='float')
    final = {}
    columns = list(df.columns.values)
    final[' '] = ['count', 'mean', 'std', 'min', 'max', '25%', '50%', '75%']
    for i in range(len(columns)):
        final[columns[i]] = []
    for key in df:
        column = df[key].dropna().sort_values()
        column = column.sort_values()
        column = column.reset_index(drop=True)
        final[key].append(str(len(column.values)))
        final[key].append(get_mean(column))
        final[key].append(get_std(column, final[key][-1]))
        final[key].append(column[0])
        final[key].append(column.iloc[-1])
        final[key].append(get_first(column))
        final[key].append(get_second(column))
        final[key].append(get_third(column))
    df = pd.DataFrame(data=final)
    print(df.round(4).to_string(index=False))
        
if __name__ == "__main__":
    if (len(sys.argv) <= 1 or len(sys.argv) > 2):
        print("error: You need to provide one dataset")
    else:
        describes(sys.argv[1])

