import os
import random
#----------------------------------------
#retourne la couleur d'un symbole sous forme str
#
#private : cette fonction n'est utile que pour ce script
#
#Entrée : str
#
#Sortie : str
#----------------------------------------
def __couleur(symbole : str, index : int, winCases: list[int])->str:

    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # red
    B  = '\033[94m' # blue
    G  = '\033[92m' # green

    if(index in winCases): return G
    elif(symbole == "0"): return B
    elif(symbole == "O"): return R
    else: return W

def __changeTurn(turn : int)->int:
    if(turn == 1): turn = 2
    else: turn = 1
    return turn

def __checkWin(cases : list[list[str]])->list[int]:

    winCases : list[int]

    winCases = []

    for i in range(0,4):
        for j in range(6,2,-1):
            if (cases[i][j] == cases[i+1][j-1] and cases[i+1][j-1] == cases[i+2][j-2] and cases[i+2][j-2] == cases[i+3][j-3] and not cases[i+1][j-1] == "."):

                winCases.append(i * 7 + j)
                winCases.append((i+1) * 7 + j-1)
                winCases.append((i+2) * 7 + j-2)
                winCases.append((i+3) * 7 + j-3)

    for i in range(0,4):
        for j in range(0,7):
            if (cases[j][i] == cases[j][i+1] and cases[j][i+1] == cases[j][i+2] and cases[j][i+2] == cases[j][i+3] and not cases[j][i] == "."):

                winCases.append(j * 7 + i)
                winCases.append(j * 7 + i+1)
                winCases.append(j * 7 + i+2)
                winCases.append(j * 7 + i+3)

    for i in range(0,4):
        for j in range(0,7):
            if (cases[i][j] == cases[i+1][j] and cases[i+1][j] == cases [i+2][j] and cases[i+2][j] == cases[i+3][j] ) and (not cases[i][j] == "." and not cases[i+1][j] == "." and not cases[i+2][j] == "." and not cases[i+3][j] == "."):

                winCases.append(i * 7 + j)
                winCases.append((i+1) * 7 + j)
                winCases.append((i+2) * 7 + j)
                winCases.append((i+3) * 7 + j)

    for i in range(0,4):
        for j in range(0,4):
            if ((cases[i][j] == cases[i+1][j+1] and cases[i+1][j+1] == cases [i+2][j+2] and cases[i+2][j+2] == cases[i+3][j+3]) and (not cases[i][j] == "." and not cases[i+1][j+1] == "." and not cases[i+2][j+2] == "." and not cases[i+3][j+3] == ".")):

                winCases.append(i * 7 + j)
                winCases.append((i+1) * 7 + j+1)
                winCases.append((i+2) * 7 + j+2)
                winCases.append((i+3) * 7 + j+3)

    return winCases

#----------------------------------------
#Affiche l'interface de jeu
#
#private : cette fonction n'est utile que pour ce script
#
#Entrée : j1_name : str, j2_name : str, score_j1 : int, score_j2 : int, cases : list[str]
#
#Sortie : affichage
#----------------------------------------
def __afficherMenu(cases : list[list[str]], winCases : list[int]):

    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print("---------------------------------------------")
    print("Schéma :")
    print("          " + __couleur(cases[0][0], 0, winCases) + cases[0][0] + W + " | " + __couleur(cases[0][1], 1, winCases) + cases[0][1] + W + " | " + __couleur(cases[0][2], 2, winCases) + cases[0][2] + W + " | " + __couleur(cases[0][3], 3, winCases) + cases[0][3] + W + " | " + __couleur(cases[0][4], 4, winCases) + cases[0][4] + W + " | " + __couleur(cases[0][5], 5, winCases) + cases[0][5] + W +  " | " + __couleur(cases[0][6], 6, winCases) + cases[0][6] + W)
    __afficherPartie(cases, winCases)

#----------------------------------------
#Affiche la partie en cours
#
#private : cette fonction n'est utile que pour ce script
#
#Entrée : cases : list[list[str]], winCases : list[int]
#
#Sortie : affichage
#----------------------------------------
def __afficherPartie(cases : list[list[str]], winCases : list[int]):

    W  = '\033[0m'  # white (normal)

    print("---------------------------------------------")
    print("Partie :")

    for i in range(1,7):
        print("          " + __couleur(cases[i][0], i*7, winCases) + cases[i][0] + W + " | " + __couleur(cases[i][1], i*7+1, winCases) + cases[i][1] + W + " | " + __couleur(cases[i][2], i*7+2, winCases) + cases[i][2] + W + " | " + __couleur(cases[i][3], i*7+3, winCases) + cases[i][3] + W + " | " + __couleur(cases[i][4], i*7+4, winCases) + cases[i][4] + W + " | " + __couleur(cases[i][5], i*7+5, winCases) + cases[i][5] + W +  " | " + __couleur(cases[i][6], i*7+6, winCases) + cases[i][6] + W)

    print("---------------------------------------------")

#----------------------------------------
#Demande a l'utilisateur d'entrer dans quelle colonne il veut placer son pion, si l'entrée n'est pas bonne le lui redemande
#
#private : cette fonction n'est utile que pour ce script
#
#Entrée : cases : list[list[str]], j_name : str, couleur : str
#
#Sortie : list[int]
#----------------------------------------
def __askForPlayerAction(cases : list[list[str]], j_name : str, couleur : str)->list[int]:

    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)

    choiceIsOk : bool
    placeFound : bool
    choiceIsOk = False
    lignes : int
    choice : str

    while not choiceIsOk:

        #demande le choix de l'utilisateur
        choice = str(input(couleur + j_name + W + " choisissez votre case en suivant le schéma ci dessus : "))

        #vérifie la valeur de l'utilisateur

        if(not choice.isdigit()):
            print(R + "Valeur impossible !" + W)
            os.system("pause")
            return []

        elif(int(choice) < 1 or int(choice) > 7):
            print(R + "La colonne n'existe pas !" + W)
            os.system("pause")
            return []

        else:

            lignes = 6
            placeFound = False
            while not placeFound:

                if(lignes <= 0):
                    print(R + "La colonne est pleine !" + W)
                    os.system("pause")
                    return []

                elif(cases[lignes][int(choice) - 1] == "0" or cases[lignes][int(choice) - 1] == "O"):
                    lignes -= 1

                else:
                    choiceIsOk = True
                    placeFound = True

    return[int(choice), lignes] #pyright: reportUnboundVariable=false


#----------------------------------------
#Affiche l'ecran de fin de partie et retourne le gagnant de la partie
#
#private : cette fonction n'est utile que pour ce script
#
#Entrée : equality : bool, turn : int, j1_name : str, j2_name : str, cases : list[list[str]], winCases : list[int]
#
#Sortie : str
#----------------------------------------
def __affichageFin(equality : bool, turn : int, j1_name : str, j2_name : str, cases : list[list[str]], winCases : list[int])->str:

    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # red
    B  = '\033[94m' # blue
    O  = '\033[93m' # yellow

    winner : str

    os.system("cls")

    print("---------------------------------------------")
    print("               " + O + "Partie terminée" + W)
    print("")

    __afficherPartie(cases, winCases)

    if(equality):
        print("égalité !")
        winner = ""
    elif(turn == 2 and not equality):
        print(B + j1_name + W + " a gagné ")
        print("---------------------------------------------")
        winner = j1_name
    elif(turn == 1 and not equality):
        print(R + j2_name + W + " a gagné ")
        winner = j2_name
        print("---------------------------------------------")

    return winner

#----------------------------------------
#Lance la partie de puissance 4 et retourne le vainqueur de la partie
#
#Entrée : j1_name : str, j2_name : str
#
#Sortie : str
#----------------------------------------
def LaunchGame_puissance4(j1_name : str, j2_name : str)->str:

    cases : list[list[str]]

    turn : int
    winner : str

    gameFinished : bool
    equality : bool
    lignes : int
    jeton : int
    turn : int

    winCases : list[int]
    listChoices : list[int]

    R  = '\033[91m' # red
    B  = '\033[94m' # blue

    #initialise le tableau

    cases = [["1","2","3","4","5","6","7"],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."]]
    winCases = []

    #intialise les données
    turn = random.randint(1,2)
    gameFinished = False
    equality = False

    lignes = 6
    winner = ""

    #boucle principale

    jeton = 42
    while not gameFinished:

        listChoices = []
        while len(listChoices) == 0 :

            #affiche le menu
            __afficherMenu(cases, winCases)

            if(turn == 1): listChoices = __askForPlayerAction(cases, j1_name, B)
            else: listChoices = __askForPlayerAction(cases, j2_name, R)

        choice = listChoices[0]
        lignes = listChoices[1]

        #ajoute le symbole dans la case souhaité
        if(turn == 1):
            cases[lignes][choice - 1] = '0'
            jeton -= 1
        elif(turn == 2):
            cases[lignes][choice - 1] = 'O'
            jeton -= 1

        #Vérification de victoire :
        winCases = __checkWin(cases)
        if(len(winCases) > 0): gameFinished = True

        #Changement de tour :
        turn = __changeTurn(turn)

        #Vérification d'égalité si pas de victoire :
        if(not gameFinished):
            equality = True
            if jeton < 1 :
                equality = True
            else:
                equality = False

            if(equality): gameFinished = True

        #Fin de Partie:

        if(gameFinished):
            winner = __affichageFin(equality, turn, j1_name, j2_name, cases, winCases)

    os.system("pause")
    return winner
