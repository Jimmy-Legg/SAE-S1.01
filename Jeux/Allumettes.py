import os

#----------------------------------------
#Affiche l'ecran de fin de partie
#
#private : cette fonction n'est utile que pour ce script
#
#Entrée : winner : str, couleur : str
#
#Sortie : affichage
#----------------------------------------
def __afficherFin(winner : str, couleur : str):

    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print("---------------------")
    print("")
    print(couleur + winner + W + " a gagné la manche")
    print("")
    print("---------------------")

#----------------------------------------
#Affiche a l'utilisateur la partie en cours et lui demande combien il veut enlever d'allumettes. Si le choix est erroné, le redemande
#
#private : cette fonction n'est utile que pour ce script
#
#Entrée : table : list[str], j_name : str, couleur :str
#
#Sortie : int (le nombre d'allumettes a enlever)
#----------------------------------------
def __getAmount(table : list[str], j_name : str, couleur :str)->int:

    mot : str
    _i : int

    W  = '\033[0m'  # white (normal)
    R = '\033[91m' # red

    choix = "0"
    while not choix.isdigit() or int(choix) < 1 or int(choix) > 3:

        mot = ""
        os.system("cls")

        print("---------------------")
        print("")

        for _i in range(0, len(table)):

            if(table[_i] == "|"): mot += " |"
            else: mot += "  "

        print(mot)
        print("")
        print("---------------------")
        print("")

        print("Tour de " + couleur +  j_name + W + ", Choix restants : ")

        print("")

        choix = input("Entrez le nombre d'allumettes à enlever : (1-3) : ")

        if(not choix.isdigit()):

            print(R + "Valeur impossible" + W)
            os.system("pause")

        elif(int(choix) < 1 or int(choix) > 3):

            print(R + "Choisissez un nombre entre 1 et 3 !" + W)
            os.system("pause")

    return int(choix)

#----------------------------------------
#Change le tour
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : int
#
#Sortie : int
#----------------------------------------
def __changeTurn(turn : int)->int:
    if(turn == 1): turn = 2
    else: turn = 1
    return turn

#----------------------------------------
#Lance la partie d'allumettes et retourne le vainqueur de la partie
#
#Entrée : j1_name : str, j2_name : str
#
#Sortie : str
#----------------------------------------
def LaunchGame_allumettes(j1_name : str, j2_name : str):

    turn : int
    nb_allumettes : int
    amount : int

    table : list[str]

    nb_allumettes = 20
    turn = 1

    table = []

    for _i in range(0, nb_allumettes):
        table.append("|")

    B = '\033[94m' # blue
    R = '\033[91m' # red

    while True:
        print("ok")
        if(turn == 1): amount = __getAmount(table, j1_name, B)
        else: amount = __getAmount(table, j2_name, R)

        for _i in range(0, amount):
            if(len(table) >= 1):
                table.remove("|")

        if(len(table)<=1): break
        else: turn = __changeTurn(turn)

    if(len(table) == 1):
        if(turn == 2): #pyright: reportUnnecessaryComparison=false
            __afficherFin(j2_name, R)
            winner = j2_name
        else:
            __afficherFin(j1_name, B)
            winner = j1_name
    else:
        if(turn == 2): #pyright: reportUnnecessaryComparison=false
            __afficherFin(j1_name, B)
            winner = j1_name
        else:
            __afficherFin(j2_name, R)
            winner = j2_name

    os.system("pause")

    return winner
