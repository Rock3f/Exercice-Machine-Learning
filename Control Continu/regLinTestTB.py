import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=[[1], [3], [5], [9], [10], [11], [12], [13], [15], [18]]
y=[[81682.0], [81720.0], [81760.0], [81826.0], [81844.0], [81864.0], [81881.0], [81900.0], [81933.0], [82003.0]]

linearRegressor = LinearRegression()
#Apprentissage du modèle
reg= linearRegressor.fit(x, y)

#Prédiction de la valeur à J+1
print("Valeur a J+1 :")
print(linearRegressor.predict([[19]]))

#Affichage de la régression linéaire et des résidus
plt.subplot(211)
plt.scatter(x, y, color = 'red')
plt.plot(x, linearRegressor.predict(x), color = 'blue')
plt.title("Regression lineaire")

plt.subplot(212)
plt.scatter(x, y - linearRegressor.predict(x), color = 'red')
plt.axhline(0, color='blue')
plt.title("Residus")

plt.show()