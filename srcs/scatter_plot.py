import matplotlib.pyplot as plt
import csv
import sys
import math

def get_data(input_file):
    data_dict = {}
    with open(input_file) as csvfile:
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

    with open(input_file) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        is_header = True
        for row in file:
            missing_data = False
            if (is_header):
                is_header = False
                continue
            for i in range(len(row)):
                if (row[i] == ""):
                    missing_data = True
            else:
                if (missing_data == True):
                    continue
                for i in range(len(row)):
                    if (headers[i] in data_dict):
                        if (row[i] == ""):
                            continue
                        else:
                            data_dict[headers[i]].append(float(row[i]))
    return data_dict

def pearson_score(X, Y):
    xmean = sum(X) / len(X)
    ymean = sum(Y) / len(Y)
    xsub = [i - xmean for i in X]
    ysub = [i - ymean for i in Y]
    xsub_times_ysub = [a * b for a, b in list(zip(xsub, ysub))]
    etx = (sum(list(map((lambda x: (x - xmean) ** 2), X))) / (len(X) - 1)) ** 0.5
    ety = (sum(list(map((lambda x: (x - ymean) ** 2), Y))) / (len(Y) - 1)) ** 0.5
    return (sum(xsub_times_ysub) / len(xsub_times_ysub) / (etx * ety))


    

def scatter_plot(input_file):
    data_dict = get_data(input_file)
    best_score = {"score": -1.1, "first": None, "second": None}
    for i, j in enumerate(data_dict):
        for k, l in enumerate(data_dict):
            if (k > i):
                score = abs(pearson_score(data_dict[j], data_dict[l]))
                if (score > best_score["score"]):
                    best_score["score"] = score
                    best_score["first"] = j
                    best_score["second"] = l
    print("According to the Bravais-Pearson relation, the two most related feature are {} and {} with a coefficient of {}".format(best_score["first"], best_score["second"], round(best_score["score"], 3)))
    fig = plt.figure("What are the two features that are similar ?")
    plt.scatter(data_dict[best_score["first"]], data_dict[best_score["second"]], c = "red")
    plt.xlabel(best_score["first"])
    plt.ylabel(best_score["second"])
    plt.show()


if __name__ == "__main__":
    if (len(sys.argv) <= 1 or len(sys.argv) > 2):
        print("error: You need to provide one dataset")
    else:
        scatter_plot(sys.argv[1])
