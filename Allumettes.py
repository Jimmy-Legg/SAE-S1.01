import os
import numpy

def __afficherFin(winner : str, couleur : str):

    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print("---------------------")
    print("")
    print(couleur + winner + W + " a gagné la manche")
    print("")
    print("---------------------")

def __afficherMenu2(nb_allumettes : int, table : list[str], j_name : str, couleur :str)->int:

    mot : str
    _i : int

    W  = '\033[0m'  # white (normal)

    while True:
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

        choix = str(input("Entrez le nombre d'allumettes à enlever : (1-3) : "))
        if(not choix.isdigit()):
            print("Valeur impossible")
            os.system("pause")
        else: break

    return int(choix)

def __changeTurn(turn : int)->int:
    if(turn == 1): turn = 2
    else: turn = 1
    return turn

def LaunchGame_allumettes(j1_name : str, j2_name : str):

    turn : int
    nb_allumettes : int
    amount : int

    table : list[str]

    nb_allumettes = 20
    turn = 1

    table = list[str](numpy.full(nb_allumettes, "|"))

    B = '\033[94m' # blue
    R = '\033[91m' # red

    while True:

        if(turn == 1): amount = __afficherMenu2(nb_allumettes, table, j1_name, B)
        else: amount = __afficherMenu2(nb_allumettes, table, j2_name, R)

        for _i in range(0, amount):
            if(len(table) > 1):
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
