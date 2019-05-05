import math

def main():
    """
        Calcul de A pour que ln(a) = 1
    """

    print("Calcul de A pour que ln(a) = 1")
    print("Les différentes valeurs affichées correspondant à chaque itération et quelle valeur approximative est égale ln(a)")
    input("Appuyer sur touche pour continuer...")

    i = 2
    j=1

    while math.log(i) <= 1 and j < 200000 :
        print("iteration %f" %j)
        print(" a = %f" %i)
        print("ln(a)= %f" %math.log(i))
        i+=0.000001
        j+=1

if __name__ == "__main__":
    main()