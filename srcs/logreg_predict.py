import sys
import pandas as pd
import numpy as np
import csv

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(classes, thetas, x):
    x = np.insert(x, 0, 1, axis=1)
    preds = [np.argmax(
        [sigmoid(xi @ theta) for theta in thetas]
    ) for xi in x]
    return [classes[p] for p in preds]

def standardize_data(data):
    for key in data:
        if (key == "Hogwarts House"):
            continue
        else:
            maxm = data[key].max()
            minm = data[key].min()
            for elem in data[key].iteritems():
                data.at[elem[0], key] = (data.at[elem[0], key] - minm) / (maxm - minm)

def get_mean(data):
    total = 0
    for x in data:
        try:
            int(x)
            total = total + x
        except:
            pass
    return (total / len(data))
    
def extract_data(train, weight):
    df = pd.read_csv(train)
    df = df.drop(["First Name", "Last Name", "Birthday", "Best Hand", "Index", "Hogwarts House"], axis=1)
    for key in df:
        df[key] = df[key].fillna(get_mean(df[key]))
    standardize_data(df)
    data = df.to_numpy()
    thetas = np.load(weight)
    return data, thetas

def test(train, weight):
    houses = ["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"]
    classes = np.array([i for i in range(len(houses))])
    x, thetas = extract_data(train, weight)
    pred = predict(classes, thetas, x)
    with open("houses.csv", "w+") as f:
        f.write("Index,Hogwarts House\n")   
        for i, j in enumerate(pred):
            f.write("{},{}\n".format(str(i), str(houses[j])))

if __name__ == "__main__":
    if (len(sys.argv) <= 1):
        print("error: You need to provide one dataset and one weight file")
    elif (len(sys.argv) == 2):
        print("error: You need to provide one weight file")
    elif (len(sys.argv) > 3):
        print("error: Too many arguments")
    else:
        test(sys.argv[1], sys.argv[2])
