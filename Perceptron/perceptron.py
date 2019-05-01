import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

class Perceptron(object):

    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
           
    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
          activation = 1
        else:
          activation = 0            
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)


print("Chargements des éléments...")
digits = datasets.load_digits()
data = digits['data']
target = digits['target']

print ("Séparation de la donnée")
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2)
training_inputs = []

for item in x_train:
    training_inputs.append(item)

labels = y_train

print("Création du modèle d'entrainment")
perceptron = Perceptron(len(x_train))
perceptron.train(training_inputs, labels)

print("prediction")
inputs = x_test
perceptron.predict(inputs) 

