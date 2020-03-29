import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def standardize_data(data):
    for key in data:
        if (key == "Hogwarts House"):
            continue
        else:
            maxm = data[key].max()
            minm = data[key].min()
            for elem in data[key].iteritems():
                data.at[elem[0], key] = (data.at[elem[0], key] - minm) / (maxm - minm)

def extract_data(input):
    df = pd.read_csv(input)
    df = df.drop(["First Name", "Last Name", "Birthday", "Best Hand", "Index"], axis=1)
    df = df.dropna()
    return df

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost(theta, x, y):
    h = sigmoid(x @ theta)
    m = len(y)
    cost = 1 / m * np.sum(
        -y * np.log(h) - (1 - y) * np.log(1 - h)
    )
    grad = 1 / m * ((y - h) @ x)
    return cost, grad

def fit(x, y, max_iter=5000, alpha=0.1):
    x = np.insert(x, 0, 1, axis=1)
    thetas = []
    classes = np.unique(y)
    costs = np.zeros(max_iter)
    for c in classes:
        binary_y = np.where(y == c, 1, 0)
        
        theta = np.zeros(x.shape[1])
        for epoch in range(max_iter):
            costs[epoch], grad = cost(theta, x, binary_y)
            theta += alpha * grad
            
        thetas.append(theta)
    return thetas, classes, costs

def train(input):
    data = extract_data(input)
    standardize_data(data)
    np_data = data.to_numpy()
    houses = ["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"]
    x = np.arange(np_data.shape[0] * (np_data.shape[1] - 1), dtype='f').reshape(np_data.shape[0], np_data.shape[1] - 1)
    y = np.arange(np_data.shape[0])
    for i in range(len(np_data)):
        for j in range(len(np_data[i])):
            if (j == 0):
                for k in range(len(houses)):
                    if (houses[k] == np_data[i][j]):
                        y[i] = k
            else:
                x[i][(j - 1)] = np_data[i][j]
    thetas, classes, costs = fit(x, y)
    thetas = np.array(thetas)
    np.save("weight", np.array(thetas))

if __name__ == "__main__":
    if (len(sys.argv) <= 1 or len(sys.argv) > 2):
        print("error: You need to provide one dataset")
    else:
        train(sys.argv[1])
