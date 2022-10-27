import os
import time
import keyboard
import numpy

def __afficherFin(winner : str, turn : int):

    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print("---------------------")
    print("")
    if(turn == 1): print(B + winner + W + " a gagné la manche")
    else: print(R + winner + W + " a gagné la manche")
    print("")
    print("---------------------")

def __afficherMenu2(nb_allumettes : int, table : list[str], x : int, turn : int, selected : list[int] , j1_name : str, j2_name : str):

    mot : str
    _i : int
    mot = ""

    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)
    G  = '\033[92m' # green
    O  = '\033[93m' # orange

    os.system("cls")

    print("---------------------")
    print("")

    for _i in range(0, nb_allumettes):
        if(_i==x):
            if(x in selected):
                if (table[x] == "|"): mot += O + " |" + W
                else: mot += B + " |" + W
            elif(table[_i] == "|"): mot += B + " |" + W
            else: mot += B + " ." + W
        else:
            if(_i in selected and table[_i] == "|"): mot += R + " |" + W
            elif(table[_i] == "|"): mot += " |"
            else: mot += "  "

    print(mot)
    print("")
    print("---------------------")
    print("")
    if(turn==1):
        if(len(selected) == 0): print("Tour de " + B +  j1_name + W + ", Choix restants : " + G + str(3 - len(selected)) + W)
        elif(len(selected) == 1): print("Tour de " + B +  j1_name + W + ", Choix restants : " + O + str(3 - len(selected)) + W)
        else: print("Tour de " + B +  j1_name + W + ", Choix restants : " + R + str(3 - len(selected)) + W)
    else:
        if(len(selected) == 0): print("Tour de " + R +  j2_name + W + ", Choix restants : " + G + str(3 - len(selected)) + W)
        elif(len(selected) == 1): print("Tour de " + R +  j2_name + W + ", Choix restants : " + O + str(3 - len(selected)) + W)
        else: print("Tour de " + R +  j2_name + W + ", Choix restants : " + R + str(3 - len(selected)) + W)
    print("")
    print("Utilisez les flèches pour vous déplacer, espace pour choisir une allumette et entrer pour finir votre tour")

def LaunchGame_allumettes(j1_name : str, j2_name : str):

    x : int
    turn : int
    nb_allumettes : int

    gameFinished : bool
    validate : bool

    table : list[str]
    selected : list[int]

    nb_allumettes = 20
    allumettes_tires = 0
    turn = 1
    x = 0

    table = list[str](numpy.full(nb_allumettes, "|"))
    selected = []

    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)

    __afficherMenu2(nb_allumettes, table, x, turn, selected , j1_name, j2_name)

    gameFinished = False

    while not gameFinished:

        validate = False

        while not validate:

            while True:

                if(keyboard.is_pressed("left")):
                    if(x > 0):
                        x-=1
                        break

                if(keyboard.is_pressed("right")):
                    if(x < nb_allumettes - 1):
                        x+=1
                        break

                if(keyboard.is_pressed("space")):
                    if(table[x]=="|"):
                        if(x in selected):
                            if(x-1 in selected and x+1 in selected):
                                __afficherMenu2(nb_allumettes, table, x, turn, selected , j1_name, j2_name)
                                print(R + "Vous ne pouvez pas sélectionner de cases qui ne sont pas côte à côte" + W)
                                time.sleep(0.2)
                            else:
                                selected.remove(x)
                                break
                        else:
                            if(len(selected) < 3):
                                if(len(selected) == 0):
                                    selected.append(x)
                                    break
                                elif(x-1 in selected or x+1 in selected):
                                    selected.append(x)
                                    break
                                else:
                                    __afficherMenu2(nb_allumettes, table, x, turn, selected , j1_name, j2_name)
                                    print(R + "Vous ne pouvez pas sélectionner de cases qui ne sont pas côte à côte" + W)
                                    time.sleep(0.2)
                            else:
                                __afficherMenu2(nb_allumettes, table, x, turn, selected , j1_name, j2_name)
                                print(R + "Vous avez déjà séléctionné 3 cases" + W)
                                time.sleep(0.2)

                    else:
                        print(R + "Vous ne pouvez pas sélectionner de cases vides" + W)
                        time.sleep(0.2)

                if(keyboard.is_pressed("enter")):

                    if(len(selected) != 0):
                        validate = True

                        if(turn == 1): turn = 2
                        else: turn = 1

                        for i in range(0, len(selected)):
                            table[selected[i]] = ""

                        allumettes_tires = allumettes_tires + len(selected)
                        selected = []

                        if(nb_allumettes == allumettes_tires): gameFinished = True
                        break

                    else:
                        __afficherMenu2(nb_allumettes, table, x, turn, selected , j1_name, j2_name)
                        print(R + "Vous n'avez pas choisi d'allumettes" + W)

            if(not validate and not gameFinished):
                __afficherMenu2(nb_allumettes, table, x, turn, selected , j1_name, j2_name)
                time.sleep(0.2)

    if(turn == 2):#pyright: reportUnnecessaryComparison=false
        __afficherFin(j2_name, turn)
        winner = j2_name
    else:
        __afficherFin(j1_name, turn)
        winner = j1_name

    os.system("pause")

    return winner

if __name__ == "__main__":

    j1 = "Jimmy"
    j2 = "Nathan"

    LaunchGame_allumettes(j1,j2)

