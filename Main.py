import os
import Jeux.Morpion as Morpion
import Jeux.Allumettes as Allumettes
import Jeux.P4 as P4
import Jeux.Devinette as Devinette
from Classes.Joueur import joueur

#----------------------------------------
#Récupère dans le fichier donné en entrée les joueurs et en fait un liste
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : (fichier) str
#
#Sortie : list[joueur]
#----------------------------------------
def __getJoueurs(fichier : str)->list[joueur]:

    listJoueurs : list[joueur]

    f = open (fichier,"r")
    lines = f.readlines()

    listJoueurs = []

    for _i in range(0,len(lines)):
        datas = lines[_i].split()
        j = joueur(str(datas[0]), int(str(datas[1])), int(str(datas[2])), int(str(datas[3])), int(str(datas[4])))
        listJoueurs.append(j)

    f.close()

    return listJoueurs

#----------------------------------------
#Affiche le menu numéro 1
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : aucune
#
#Sortie : affichage
#----------------------------------------
def __afficher_menu_1():

    os.system("cls")
    print("---------------------")
    print("     Bienvenue !     ")
    print("                     ")
    print("  1 - Jouer          ")
    print("  2 - Scores         ")
    print("  3 - Règles         ")
    print("  4 - Quitter        ")
    print("                     ")
    print("---------------------")

#----------------------------------------
#Affiche le menu numéro 2
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : aucune
#
#Sortie : affichage
#----------------------------------------
def __afficher_menu_2():

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

#----------------------------------------
#Affiche le menu numéro 3
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : aucune
#
#Sortie : affichage
#----------------------------------------
def __afficher_menu_3():

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

#----------------------------------------
#Affiche le menu numéro 4
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : aucune
#
#Sortie : affichage
#----------------------------------------
def __afficher_menu_4():

    os.system("cls")
    print("---------------------")
    print("       Règles :      ")
    print("                     ")
    print("  1 - Devinette      ")
    print("  2 - Allumettes     ")
    print("  3 - Morpion        ")
    print("  4 - Puissance 4    ")
    print("                     ")
    print("  5 - Retour         ")
    print("                     ")
    print("---------------------")

#----------------------------------------
#Affiche les scores d'un jeu pour tout les joueurs, classé dans l'ordre croissant
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : list[joueur], str (le nom du jeu souhaité)
#
#Sortie : affichage
#----------------------------------------
def __afficher_scores(listJoueur : list[joueur], nom : str):

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
        if(scores[k][1] != 0):print(scores[k][0] + " : " + str(scores[k][1]))
    print("                     ")
    print("---------------------")
    os.system("pause")

#----------------------------------------
#Affiche les règles d'un jeu
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : str (le nom du jeu souhaité)
#
#Sortie : affichage
#----------------------------------------
def __afficher_regles(nom : str):

    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)
    O  = '\033[93m' # yellow
    P  = '\033[95m' # purple
    N  = '\033[90m' # noir

    os.system("cls")
    print("---------------------")
    print(O + "Règles : " + nom + W)
    print("---------------------")
    if(nom == "devinette"):
        print("Les joueurs commencent par choisir l'intervalle dans lequel la partie se jouera")
        print("")
        print(N + "(Le joueur qui démarre est défini aléatoirement)" + W)
        print("")
        print("Le " + B + "joueur 1" + W + " choisit " + P + "le nombre a faire deviner" + W + ";")
        print("Le " + R + "joueur 2" + W + " essaye ensuite de le" + P + " deviner" + W + " le plus" + P + " rapidement" + W + " possible")
        print("")
        print("Le " + R + "joueur 2" + W + " choisit le nombre a faire deviner;")
        print("Le " + B + "joueur 1" + W + " essaye ensuite de le" + P + " deviner" + W + " le plus" + P + " rapidement" + W + " possible")
        print("")
        print(P + "Le joueur qui a deviné le plus rapidement gagne la partie !" + W)
    if(nom == "allumettes"):
        print("La partie démarre avec 20 allumettes")
        print("")
        print(N + "(Le joueur qui démarre est défini aléatoirement)" + W)
        print("")
        print("Le " + B + "joueur 1" + W + " choisit de retirer " + P + "entre 1 et 3 allumettes" + W)
        print("")
        print("Le " + R + "joueur 2" + W + " choisit à son tour de retirer " + P + "entre 1 et 3 allumettes" + W)
        print()
        print("Et ainsi de suite " + P + "jusqu'a ne plus y avoir d'allumettes" + W)
        print()
        print(P + "Le joueur qui tire la dernière allumette perd la partie" + W)
    if(nom == "morpion"):
        print("La partie se déroule dans un tableau de 3 x 3")
        print("")
        print(N + "(Le joueur qui démarre est défini aléatoirement)" + W)
        print("")
        print("Le " + B + "joueur 1" + W + " choisit de mettre son " + P + "symbole de couleur" + W + " dans la case qu'il désire")
        print("")
        print("Le " + R + "joueur 2" + W + " choisit de à son tour de mettre son " + P + "symbole de couleur" + W + " dans la case qu'il désire")
        print()
        print("Et ainsi de suite " + P + "jusqu’à obtenir une rangée de 3 symbole de même couleur dans toutes les directions possible" + W)
        print()
        print(P + "Le joueur qui possède les 3 jetons alignés gagne la partie" + W)
    if(nom == "puissance4"):
        print("La partie se déroule dans un tableau de 6 x 7")
        print("")
        print(N + "(Le joueur qui démarre est défini aléatoirement)" + W)
        print("")
        print("Le " + B + "joueur 1" + W + " met un de ses " + P + "jetons de couleur" + W + " dans l’une des colonnes de son choix. Le " + P + "jeton" + W + " tombe alors en bas de la colonne.")
        print("")
        print("Le " + R + "joueur 2" + W + " insère à son tour son " + P + "jeton de couleur" + W + ", dans la colonne de son choix.")
        print()
        print("Et ainsi de suite " + P + "jusqu’à obtenir une rangée de 4 jetons de même couleur dans toutes les directions possible" + W)
        print()
        print(P + "Le joueur qui possède les 4 jetons alignés gagne la partie" + W)
    print("---------------------")
    os.system("pause")

#----------------------------------------
#Ajoute un point a un joueur souhaité, designé par son nom, dans le jeu souhaité
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : str (le nom du joueur), str (le nom du jeu souhaité), list[joueur]
#
#Sortie : Modification du fichier texte en ajoutant un point au joueur souhaité
#----------------------------------------
def __ajouterScore(winner : str, jeu : str, listJoueur : list[joueur]):

    playerFound : bool

    playerFound = False

    for j in listJoueur:
        if(j.getName() == winner):
            if(jeu == "devinette"):j.setScoreDevinette(j.getScoreDevinette() + 1)
            elif(jeu == "allumettes"):j.setScoreAllumettes(j.getScoreAllumettes() + 1)
            elif(jeu == "morpion"):j.setScoreMorpion(j.getScoreMorpion() + 1)
            elif(jeu == "puissance4"):j.setScorePuissance4(j.getScorePuissance4() + 1)
            else: print("Jeu inconnu")
            playerFound = True

    if(not playerFound):
        if(jeu == "devinette"): listJoueurs.append(joueur(winner, 1, 0, 0, 0))
        elif(jeu == "allumettes"): listJoueurs.append(joueur(winner, 0, 1, 0, 0))
        elif(jeu == "morpion"): listJoueurs.append(joueur(winner, 0, 0, 1, 0))
        elif(jeu == "puissance4"): listJoueurs.append(joueur(winner, 0, 0, 0, 1))
        else: print("Jeu erreur")

    __writePlayersData(listJoueurs)


#----------------------------------------
#Ecris les données des joueurs dans le fichier ./Scores/playersData.txt
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : list[joueur]
#
#Sortie : Modification du fichier texte en fonction de la list de joueur
#----------------------------------------
def __writePlayersData(listJoueur : list[joueur]):

    _i : int

    lines : list[str]
    lines = []

    f = open("./Scores/playersData.txt","w")
    for _i in range(0, len(listJoueur)):
        if(_i == 0):lines.append(listJoueur[_i].getName() + " " + str(listJoueur[_i].getScoreDevinette()) + " " + str(listJoueur[_i].getScoreAllumettes()) + " " + str(listJoueur[_i].getScoreMorpion()) + " " + str(listJoueur[_i].getScorePuissance4()))
        else: lines.append("\n" + listJoueur[_i].getName() + " " + str(listJoueur[_i].getScoreDevinette()) + " " + str(listJoueur[_i].getScoreAllumettes()) + " " + str(listJoueur[_i].getScoreMorpion()) + " " + str(listJoueur[_i].getScorePuissance4()))

    f.writelines(lines)
    f.close()

if __name__ == "__main__":

    listJoueurs : list[joueur]

    j1_name : str
    j2_name : str
    WantToQuit : bool

    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)

    #demande les noms des joueurs
    os.system("cls")
    j1_name = str(input(B + "Joueur 1" + W + ", quel est votre nom ? "))
    j2_name = str(input(R + "Joueur 2" + W + ", quel est votre nom ? "))

    listJoueurs = __getJoueurs("./Scores/playersData.txt")

    WantToQuit = False

    while not WantToQuit :

        __afficher_menu_1()

        choice = str(input("Choisissez le jeu : "))

        match choice:

            case "1":

                WantToGoBack = False
                while not WantToGoBack :

                    __afficher_menu_2()

                    choice = str(input("Choisissez le jeu : "))

                    match choice:

                        case "1":
                            winner = Devinette.LaunchGame_devinettes(j1_name,j2_name)
                            if(not winner == ""): __ajouterScore(winner, "devinette", listJoueurs)

                        case "2":
                            winner = Allumettes.LaunchGame_allumettes(j1_name, j2_name)
                            if(not winner == ""): __ajouterScore(winner, "allumettes", listJoueurs)

                        case "3":
                            winner = Morpion.LaunchGame_morpion(j1_name, j2_name)
                            if(not winner == ""): __ajouterScore(winner, "morpion", listJoueurs)

                        case "4":
                            winner = P4.LaunchGame_puissance4(j1_name, j2_name)
                            if(not winner == ""): __ajouterScore(winner, "puissance4", listJoueurs)

                        case "5":
                            WantToGoBack = True

                        case other:
                            print("Réponse inconnue")
                            os.system("pause")

            case "2":
                WantToGoBack = False
                while not WantToGoBack :

                    __afficher_menu_3()

                    choice = str(input("Choisissez le jeu : "))

                    match choice:

                        case "1":
                            __afficher_scores(listJoueurs, "devinette")

                        case "2":
                            __afficher_scores(listJoueurs, "allumettes")

                        case "3":
                            __afficher_scores(listJoueurs, "morpion")

                        case "4":
                            __afficher_scores(listJoueurs, "puissance4")

                        case "5":
                            WantToGoBack = True

                        case other:
                            print("Réponse inconnue")
                            os.system("pause")

            case "3":
                WantToGoBack = False
                while not WantToGoBack :

                    __afficher_menu_4()

                    choice = str(input("Choisissez le jeu : "))

                    match choice:

                        case "1":
                            __afficher_regles("devinette")

                        case "2":
                            __afficher_regles("allumettes")

                        case "3":
                            __afficher_regles("morpion")

                        case "4":
                            __afficher_regles("puissance4")

                        case "5":
                            WantToGoBack = True

                        case other:
                            print("Réponse inconnue")
                            os.system("pause")

            case "4":
                WantToQuit = True

            case other:
                print("Réponse inconnue")
                os.system("pause")
