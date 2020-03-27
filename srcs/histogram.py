import matplotlib.pyplot as plt
import csv
import sys

def histogram(file_input):
    data_dict = {}
    houses = []

    with open(file_input) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        is_header = True
        for row in file:
            if (is_header):
                is_header = False
            else:
                if (row[1] not in houses):
                    houses.append(row[1])

    with open(file_input) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        headers = next(file)
        data = next(file)
        for i in range(len(data)):
            if (i == 0):
                continue
            try:
                float(data[i])
                data_dict[headers[i]] = {"min_grade": None, "max_grade": None}
            except:
                pass

    with open(file_input) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        is_header = True
        for row in file:
            if (is_header):
                is_header = False
            else:
                for i in range(len(row)):
                    if (headers[i] in data_dict and len(row[i])):
                        if row[1] not in data_dict[headers[i]]:
                            data_dict[headers[i]][row[1]] = []
                        data_dict[headers[i]][row[1]].append(row[i])
                        if ((data_dict[headers[i]]["max_grade"] == None) or (float(row[i]) > float(data_dict[headers[i]]["max_grade"]))):
                            data_dict[headers[i]]["max_grade"] = row[i]
                        elif ((data_dict[headers[i]]["min_grade"] == None) or (float(row[i]) < float(data_dict[headers[i]]["min_grade"]))):
                            data_dict[headers[i]]["min_grade"] = row[i]

    row = int(len(data_dict) / 4) + len(data_dict) % 4
    fig, ax = plt.subplots(4, row, figsize=(15,15))
    fig.canvas.set_window_title('Which Hogwarts course has a homogeneous score distribution between all four houses ?') 
    row = 0
    column = 0
    for key in data_dict:
        ratio = float(data_dict[key]["max_grade"]) - float(data_dict[key]["min_grade"])
        ax[row, column].set_title(key)
        ax[row, column].set_xlabel("grade distribution")
        ax[row, column].set_ylabel("students")
        for elem in data_dict[key]:
            if (elem != "min_grade" and elem != "max_grade"):
                for i in range(len(data_dict[key][elem])):
                    data_dict[key][elem][i] = (float(data_dict[key][elem][i]) - float(data_dict[key]["min_grade"])) / (float(data_dict[key]["max_grade"]) - float(data_dict[key]["min_grade"]))
                ax[row, column].hist(data_dict[key][elem], bins= [x / 20 for x in range(0, 20)], alpha=0.5, label=elem)
        ax[row, column].legend()
        column += 1
        if (column == 4):
            column = 0
            row += 1
    while (column < 4):
        ax[row, column].axis('off')
        column += 1
    plt.show()

if __name__ == "__main__":
    if (len(sys.argv) <= 1 or len(sys.argv) > 2):
        print("error: You need to provide one dataset")
    else:
        histogram(sys.argv[1])
