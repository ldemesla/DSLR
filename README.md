# DSLR

This is a project is an implemention of a multiclassifier, using the one-vs-all (or one-vs-rest) technique, which aim to predict the Harry Potter's Hogwarts Houses of a student according to a set of features.

## Usage

`describes.py dataset` display mean, standard deviation, minimun, maximum, count, median, first and third quartile for all features.

`histogram.py dataset` show the distribution of grades for all features between all the houses.

`scatter_plot.py dataset` display the a scatter plot of the two houses with the strongest relation according to the Bravais-Pearson relation.

`pair_plot.py dataset` show a pair plot of all numeric values of the dataset.

`logreg_train.py dataset` train the model with the dataset and generate a `weight.py` file with all the thetas needed for prediction.
 
 `logreg_predict.py dataset weights` generate prediction for the given dataset and weights. It generate a `houses.csv` file with all the result of the prediction.
 
 ## Images


