import math

def main():
    """
        Calcul de A pour que ln(a) = 1
    """

    i = 2
    j=1

    while math.log(i) <= 1 :
        print("iteration %f" %j)
        print(" a = %f" %i)
        print(math.log(i))
        i+=0.000001
        j+=1

if __name__ == "__main__":
    main()