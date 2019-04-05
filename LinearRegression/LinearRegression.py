import matplotlib.pyplot as plt
import numpy as np

def Hypothese(t0,t1,x) :
    """
        Calcul de l'hypothèse
    """
    return t0 + t1 * x

def AllSumHyp(array, t0, t1, isT1 = False) :
    """
        Somme de l'ensemble des hypothèses
    """
    j = 0
    allHyp = 0
    #Ajout de l'ensemble des thèses suivant theta / Theta 0 et theta 1 ne disposent pas de la même formule
    while(j < len(array)) :
        if isT1 :
            allHyp += (Hypothese(t0, t1, array[j][0]) - array[j][1]) * array[j][0]
        else :
            allHyp += Hypothese(t0, t1, array[j][0]) - array[j][1]
        j += 1
       
    return allHyp

def DisplayGraph(array, x , y, t0, t1) :
    """
        Affichage du graphique de la régression linéaire
    """
    plt.figure(1)
    plt.subplot(211)
    plt.scatter(x, y, color = 'red')
    plt.plot(x, Hypothese(t0,t1,x), color = 'blue')

    plt.subplot(212)
    plt.scatter(x, y - Hypothese(t0,t1,x), color = 'red')
    plt.axhline(0, color='blue')

    plt.show()

def main():
    """
        Calcul de la régression linéaire via le calcul d'hypothèse
    """

    #Définition des variables
    t0 = 1
    t1 = 1
    array = [[1, 7], [2, 3], [3, 1]]
    i = 1
    lastCost = 1

    while i < 200000 :
        print("Boucle %f" %i)
        #t0inter et t1inter sont des variables provisoires pour stockées les nouvelles valeurs de theta
        t0inter = t0 - (1/i) / len(array) * AllSumHyp(array,t0,t1)
        t1inter = t1 - (1/i) / len(array) * AllSumHyp(array,t0,t1, True)
        i += 1

        #Calcul du coût
        cost = 1 / (2*len(array)) * (AllSumHyp(array, t0, t1)**2)
        print("TETA0 %f" %t0inter)
        print("TETA1 %f" %t1inter)
        print("Cost %f" %round(cost,6))

        #Si le cout est à peu prêt inférieur à 0,08 alors on stoppe le processus de recherche de l'hypothèse
        if (cost < 0.08) & (round(cost,6) == round(lastCost,6)) :
            i = 200000
        
        lastCost = cost
        t0 = t0inter
        t1 = t1inter

    #Afffichage du graphique
    x=np.array([[1], [2], [3]])
    y=np.array([[7], [3], [1]])
    DisplayGraph(array,x ,y, t0, t1)

if __name__ == "__main__":
    main()