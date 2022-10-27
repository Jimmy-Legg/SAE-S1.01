import os
import Jeux.Morpion as Morpion
import Jeux.Allumettes as Allumettes
import Jeux.P4 as P4
import Jeux.devinette as Devinette
from Classes.Joueur import joueur

def getJoueurs(fichier : str)->list[joueur]:

    listJoueurs : list[joueur]

    f = open (fichier,"rb")
    lines = f.readlines()

    listJoueurs = []

    for _i in range(0,len(lines)):
        datas = lines[_i].split()
        j = joueur(str(datas[0])[2:-1], int(str(datas[1])[2:-1]), int(str(datas[2])[2:-1]), int(str(datas[3])[2:-1]), int(str(datas[4])[2:-1]))
        listJoueurs.append(j)

    return listJoueurs

def afficher_menu_1():

    os.system("cls")
    print("---------------------")
    print("     Bienvenue !     ")
    print("                     ")
    print("  1 - Jouer          ")
    print("  2 - Scores         ")
    print("  3 - Quitter        ")
    print("                     ")
    print("---------------------")

def afficher_menu_2():

    os.system("cls")
    print("---------------------")
    print("       Jouer :       ")
    print("                     ")
    print("  1 - Devinette      ")
    print("  2 - Allumettes     ")
    print("  3 - Morpion        ")
    print("  4 - Puissance 4    ")
    print("                     ")
    print("  5 - Retour         ")
    print("                     ")
    print("---------------------")

def afficher_menu_3():

    os.system("cls")
    print("---------------------")
    print("       Scores :      ")
    print("                     ")
    print("  1 - Devinette      ")
    print("  2 - Allumettes     ")
    print("  3 - Morpion        ")
    print("  4 - Puissance 4    ")
    print("                     ")
    print("  5 - Retour         ")
    print("                     ")
    print("---------------------")

def afficher_scores(listJoueur : list[joueur], nom : str):

    os.system("cls")
    print("---------------------")
    print("Scores : " + nom)
    print("                     ")

    scores = {}

    for j in listJoueurs:
        if(nom == "devinette"): scores[j.getName()] = j.getScoreDevinette()
        if(nom == "allumettes"): scores[j.getName()] = j.getScoreAllumettes()
        if(nom == "morpion"): scores[j.getName()] = j.getScoreMorpion()
        if(nom == "puissance4"): scores[j.getName()] = j.getScorePuissance4()

    #pyright: reportUnknownLambdaType=false
    #pyright: reportUnknownVariableType=false
    scores = sorted(scores.items(), key=lambda t:t[1])

    #pyright: reportUnknownArgumentType=false
    for k in range(len(scores)-1, -1, -1):
        print(scores[k][0] + " : " + str(scores[k][1]))

    print("                     ")
    print("---------------------")
    os.system("pause")

def ajouterScore(winner : str, score : int, jeu : str, listJoueur : list[joueur]):

    playerFound : bool

    playerFound = False

    for j in listJoueurs:
        if(j.getName() == winner):
            if(jeu == "devinette"):j.setScoreDevinette(j.getScoreDevinette() + 1)
            elif(jeu == "allumettes"):j.setScoreAllumettes(j.getScoreAllumettes() + 1)
            elif(jeu == "morpion"):j.setScoreMorpion(j.getScoreMorpion() + 1)
            elif(jeu == "puissance4"):j.setScorePuissance4(j.getScorePuissance4() + 1)
            else: print("Jeu inconnu")
            playerFound = True

    if(not playerFound):
        if(jeu == "devinette"): listJoueurs.append(joueur(winner, 1, 0, 0, 0))
        elif(jeu == "allumettes"): listJoueurs.append(joueur(winner, 1, 0, 0, 0))
        elif(jeu == "morpion"): listJoueurs.append(joueur(winner, 1, 0, 0, 0))
        elif(jeu == "puissance4"): listJoueurs.append(joueur(winner, 1, 0, 0, 0))
        else: print("Jeu erreur")

    writePlayersData(listJoueurs)

def writePlayersData(listJoueur : list[joueur]):

    _i : int

    lines : list[bytes]
    lines = []

    f = open("./Scores/playersData.txt","wb")
    for _i in range(0, len(listJoueur)):
        if(_i == 0):lines.append(str(listJoueur[_i].getName() + " " + str(listJoueur[_i].getScoreDevinette()) + " " + str(listJoueur[_i].getScoreAllumettes()) + " " + str(listJoueur[_i].getScoreMorpion()) + " " + str(listJoueur[_i].getScorePuissance4())).encode())
        else: lines.append(str("\n" + listJoueur[_i].getName() + " " + str(listJoueur[_i].getScoreDevinette()) + " " + str(listJoueur[_i].getScoreAllumettes()) + " " + str(listJoueur[_i].getScoreMorpion()) + " " + str(listJoueur[_i].getScorePuissance4())).encode())

    f.writelines(lines)
    f.close()

if __name__ == "__main__":

    listJoueurs : list[joueur]

    j1_name : str
    j2_name : str

    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)

    #demande les noms des joueurs
    os.system("cls")
    j1_name = str(input(B + "Joueur 1" + W + ", quel est votre nom ? "))
    j2_name = str(input(R + "Joueur 2" + W + ", quel est votre nom ? "))

    listJoueurs = getJoueurs("./Scores/playersData.txt")

    while True :

        afficher_menu_1()

        choice = str(input("Choisissez le jeu : "))

        match choice:

            case "1":

                 while True :

                    afficher_menu_2()

                    choice = str(input("Choisissez le jeu : "))

                    match choice:

                        case "1":
                            winner = Devinette.LaunchGame_devinettes(j1_name,j2_name)
                            if(not winner == ""): ajouterScore(winner, 1, "devinette", listJoueurs)

                        case "2":
                            winner = Allumettes.LaunchGame_allumettes(j1_name, j2_name)
                            if(not winner == ""): ajouterScore(winner, 1, "allumettes", listJoueurs)

                        case "3":
                            winner = Morpion.LaunchGame_morpion(j1_name, j2_name)
                            if(not winner == ""): ajouterScore(winner, 1, "morpion", listJoueurs)

                        case "4":
                            winner = P4.LaunchGame_puissance4(j1_name, j2_name)
                            if(not winner == ""): ajouterScore(winner, 1, "puissance4", listJoueurs)


                        case "5":
                            break

                        case other:
                            print("Réponse inconnue")
                            os.system("pause")

            case "2":
                while True :

                    afficher_menu_3()

                    choice = str(input("Choisissez le jeu : "))

                    match choice:

                        case "1":
                            afficher_scores(listJoueurs, "devinette")

                        case "2":
                            afficher_scores(listJoueurs, "allumettes")

                        case "3":
                            afficher_scores(listJoueurs, "morpion")

                        case "4":
                            afficher_scores(listJoueurs, "puissance4")

                        case "5":
                            break

                        case other:
                            print("Réponse inconnue")
                            os.system("pause")

            case "3":
                break

            case other:
                print("Réponse inconnue")
                os.system("pause")