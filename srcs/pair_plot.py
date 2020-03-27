import matplotlib.pyplot as plt
import csv
import sys
import math
import seaborn as sns
import pandas as pd

def pair_plot(input):
    plt.figure("what features are you going to use for your logistic regression?")
    data = pd.read_csv(input)
    data = data.drop(['Index','First Name','Last Name', 'Birthday'], axis=1)
    sns.set(style="ticks", color_codes=True)
    sns.pairplot(data, hue='Hogwarts House')
    plt.show()

if __name__ == "__main__":
    if (len(sys.argv) <= 1 or len(sys.argv) > 2):
        print("error: You need to provide one dataset")
    else:
        pair_plot(sys.argv[1])
