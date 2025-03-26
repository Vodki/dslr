import pandas as pd
import numpy as np
from logreg_train import LogisticRegressionOneVsAllModel, normalize
import os
import sys



def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: logreg_predict.py <dataset> <weights>")
    if not os.path.isfile(sys.argv[1]) or not os.path.isfile(sys.argv[2]):
        sys.exit("Error: Wrong input file")

    houses = ['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff']
    indexed_houses = {index: house for index, house in enumerate(houses)}
    weights_data = pd.read_csv(sys.argv[2])
    weights_arrays = {col: weights_data[col].values for col in weights_data.columns}
    data = pd.read_csv(sys.argv[1])
    data.ffill(inplace=True, axis=0)
    data = data.drop(['Birthday','First Name','Last Name', 'Best Hand', 'Arithmancy', 'Potions', 'Care of Magical Creatures', 'Muggle Studies', 'History of Magic'], axis=1)
    
    result = []
    x = np.array(normalize(data.iloc[:,2:]))
    for house in houses:
        model = LogisticRegressionOneVsAllModel()
        model.thetas = weights_arrays[house]
        y_hat = model.predict(x)
        result.append(y_hat)
    result = np.c_[result].T
    highest = np.argmax(result, axis=1)
    predicted_houses = [indexed_houses[n] for n in highest]
    predictions_file = pd.DataFrame({
        'Index': range(len(highest)),
        'Hogwarts House': predicted_houses
    })
    predictions_file.to_csv('houses.csv', index=False)


if __name__ == "__main__":
    main()