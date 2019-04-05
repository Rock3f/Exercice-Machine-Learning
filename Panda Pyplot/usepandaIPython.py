import pandas as pd
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

#Affichage des consommations moyennes de bieres
def AffichageDesConsommationsMoyennes(df) : 
    """
        Affichages des différentes consommations de bières
    """

    #Consommation de biere sur le weekend
    weekendconsumption_liters = reduce(lambda x,y: x+y, GetConsommationDeBiereWeekend(df))
    weekendconsumption_liters_mid = weekendconsumption_liters / len(GetConsommationDeBiereWeekend(df))
    print("Median Beer drink Weekend %f" %weekendconsumption_liters_mid)

    #Consommation de biere sur la semaine
    weekconsumption_liters = reduce(lambda x,y: x+y, GetConsommationDeBiereSemaine(df))
    weekconsumption_liters_mid = weekconsumption_liters / len(GetConsommationDeBiereSemaine(df))
    print("Median Beer drink Week %f" %weekconsumption_liters_mid)

    #Consommation de biere lors des jours de pluies
    rainyDayconsumption_liters = reduce(lambda x,y: x+y, GetConsommationDeBierePluie(df) )
    rainyDayconsumption_liters_mid = rainyDayconsumption_liters / len(GetConsommationDeBierePluie(df) )
    print("Median Beer drink rainy day %f" %rainyDayconsumption_liters_mid)

    #Consommation de viere lors des jours ensoleille
    sunnyDayconsumption_liters = reduce(lambda x,y: x+y, GetConsommationDeBiereSoleil(df) )
    sunnyDayconsumption_liters_mid = sunnyDayconsumption_liters / len(GetConsommationDeBiereSoleil(df) )
    print("Median Beer drink sunny day %f" %sunnyDayconsumption_liters_mid)

#Affichage des graphiques
def AffichageDesGraphs(df):
    """
        Affichage des différents graphiques
    """
    #TEMPERATURE
    #Mise en place des axes d'analyses + de l'ensemble des points
    plt.figure(1)
    plt1 = plt.subplot(211)
    plt1.set_title("Graphique de la consommation de biere suivant la temperature.")

    x = df["TempMed"]
    y = df["Beer"]

    plt.scatter(x,y)

    #Calcul de la courbe de tendance
    z = np.polyfit(x,y,1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"ro")

    #RAIN

    plt2 = plt.subplot(212)
    plt2.set_title("Graphique de la consommation de biere suivant les precipitations.")
    #Mise en place des axes d'analyses + de l'ensemble des points
    x = df["Rain"]
    y = df["Beer"]

    plt.scatter(x,y)

    #Calcul de la courbe de tendance
    z = np.polyfit(x,y,1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"ro")

    #Affichage des informations
    plt.show()

#Boite à moustache
def BoiteAMoustache(numberFigure, data, title, data1 = None, title1 = None, isVertical = False) : 
    """
        Affichage d'une boite à moustache suivant différentes données
    """
    plt.figure(numberFigure)

    if data1 is None :
        plt1 = plt.subplot(211)
        plt1.set_title(title)
        plt.boxplot(data, vert = isVertical)
    else :
        plt1 = plt.subplot(211)
        plt1.set_title(title)
        plt.boxplot(data, vert = isVertical)

        plt2 = plt.subplot(212)
        plt2.set_title(title1)
        plt.boxplot(data1, vert = isVertical)
    
    plt.show()

#Getter
def GetConsommationDeBiereWeekend(df) : 
    """
        Obtention de la consommation de bière le weekend
    """
    return df.loc[df['WeekEnd']==1]['Beer']

def GetConsommationDeBiereSemaine(df) : 
    """
        Obtention de la consommation de bière en semaine
    """
    return df.loc[df['WeekEnd']==0]['Beer']

def GetConsommationDeBierePluie(df) : 
    """
        Obtention de la consommation de bière par temps de pluie
    """
    return df.loc[df['Rain'].astype(float) > 0]['Beer']

def GetConsommationDeBiereSoleil(df) :
    """
        Obtention de la consommation de bière par temps ensolleilé
    """
    return df.loc[df['Rain'].astype(float) == 0]['Beer']

def main():
    """
        Affichage de la consommation moyenne de bière, et des différentes boites à moustaches
    """
    #Recuperation du fichier csv
    data_frame = pd.read_csv("../Consumo_cerveja.csv")

    #Suppression des valeurs NaN
    data_frame = data_frame.dropna()

    #Affichage des différentes consommations
    AffichageDesConsommationsMoyennes(data_frame)
    #Affichage des graphiques et des Boites à Moustache
    AffichageDesGraphs(data_frame)
    BoiteAMoustache(2, data_frame['Beer'], "Boite à Moustache de la consommation de bière")
    BoiteAMoustache(3, GetConsommationDeBiereSoleil(data_frame), "Boite à Moustache de la consommation de bière par temps ensoleillé", GetConsommationDeBierePluie(data_frame), "Boite à Moustache de la consommation de bière par temps de pluie")
    BoiteAMoustache(4, GetConsommationDeBiereWeekend(data_frame), "Boite à Moustache de la consommation de bière sur le weekend", GetConsommationDeBiereSemaine(data_frame), "Boite à Moustache de la consommation de bière sur la semaine")

if __name__ == "__main__":
    main()