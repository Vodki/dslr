
import numpy as np
import pandas as pd
import sys
import os

def normalize(data):
    return data.apply(lambda x: (x - x.min()) / (x.max() - x.min()))

class LogisticRegressionOneVsAllModel:
    
    def __init__(self, thetas=None, y=None, np_data=None, house=None): # Initialisation of alpha (learning rate) and epochs (number of iteration) 
        self.alpha = 0.0005
        self.epochs = 10000
        self.y = y
        self.np_data = np_data
        self.thetas = np.array(thetas)
        self.house = house

    def _sigmoid(self, x):
        return np.array(1 / (1 + np.exp(-x)))

    def predict(self, x: np.array):
        X = np.insert(x, 0, 1, axis=1)
        return self._sigmoid(X.dot(self.thetas))

    def training(self):
        x = np.insert(self.np_data, 0, 1, axis=1) # Adding the bias
        m = len(self.y)
        for _ in range(self.epochs):
            gradient = 1 / m * (np.dot(x.T, (np.dot(x, self.thetas) - self.y)))
            self.thetas = self.thetas - (self.alpha * gradient)
        return self.thetas
    

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 logreg_train.py <dataset>")
    if not os.path.isfile(sys.argv[1]):
        sys.exit("Error: Wrong input file")

    data = pd.read_csv(sys.argv[1])
    data.ffill(inplace=True, axis=0)
    data = data.drop(['First Name', 'Last Name', 'Birthday'], axis=1)
    data['Best Hand'] = data['Best Hand'].map({"Left": 0, "Right": 1})
    np_data = np.array(normalize(data.iloc[:, 2:]))
    houses = ['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff']
    y_map = {house: data["Hogwarts House"].map(lambda x: 1 if x == house else 0).to_numpy() for house in houses}
    houses_thetas = []
    for house in houses:
        y = np.array(y_map[house])
        model = LogisticRegressionOneVsAllModel([1] * 15, y, np_data, house)
        thetas = model.training()
        houses_thetas.append(thetas)

    weights_file = pd.DataFrame(np.array(houses_thetas).T, columns=['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff'])
    weights_file.to_csv('weights.csv', index=False)
if __name__ == "__main__":
    main()

