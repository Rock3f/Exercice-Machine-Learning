from collections import defaultdict
from surprise import SVD
from surprise import Dataset

from surprise import KNNWithMeans
from surprise import accuracy
from surprise.model_selection import train_test_split
import matplotlib.pyplot as plt

#Renvoie le top n des recommendation pour chaque utilisateur du dataset
def get_top_n(predictions, n=10):
    # Réaliser un mapage des prédictions sur chaque utilisateurs 
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Filtre les prédictions pour chaque utilisateur et retourne les n plus élevés
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

def displayTop10(data) :
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)

    #Prédiction pour l'ensemble des natotation qui ne sont pas dans le training set
    testset = trainset.build_anti_testset()
    predictions = algo.test(testset)

    top_n = get_top_n(predictions, n=10)

    # Afficher les résultats
    for uid, user_ratings in top_n.items():
        print(uid, [iid for (iid, _) in user_ratings])


def DisplayGraphDelta(data) : 
    # Créer un jeu de test et de train ( 25%, 75%)
    trainset, testset = train_test_split(data, test_size=.15)

    algo = KNNWithMeans()

    # Train sur le jeu de donnée trainset
    algo.fit(trainset)
    # Prediction sur le jeu de donnée testset
    predictions = algo.test(testset)

    # Affiche le RMSE
    accuracy.rmse(predictions)

    #print(predictions)

    result =[]
    for prediction in predictions:
        print(prediction)
        # Calcul le delta entre la prediction et la réalité
        result.append(prediction.r_ui - prediction.est)

    # Affiche l'histogramme du delta entre les prediction et la réalité
    print(len(result))
    plt.hist(result, 100)
    plt.show()

# Premier entrainement de l'aglo SVD sur le datasers
data = Dataset.load_builtin('ml-100k')
DisplayGraphDelta(data)
displayTop10(data)