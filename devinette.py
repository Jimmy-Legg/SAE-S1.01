import os
import time

def __LaunchTurn(nombre_a_trouver : int, couleur : str, j_name : str, mini:int, maxi:int)->float:

    choix : str
    nombre : int

    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print(couleur + j_name + W + " à vous de jouer !")
    os.system("pause")

    temps = time.time()

    while True:

        print("Nombre entre " + str(mini) + " et " + str(maxi) + " : ")
        choix = input("Faites une première hypothèse : ")
        if(not str(choix).isdigit()):print("Valeur impossible")
        elif(int(choix) < int(mini) or int(choix) > int(maxi)):print("Valeur impossible")
        else:
            nombre = int(choix)
            break

    while True :

        if nombre == nombre_a_trouver:

            temps = time.time()-temps
            break

        elif nombre < nombre_a_trouver:

            os.system("cls")
            print(nombre, nombre_a_trouver)

            print(couleur + j_name + W + " : ")
            print("Nombre entre " + str(mini) + " et " + str(maxi) + " : ")

            while True:

                choix = input("Nombre plus grand que " + str(nombre) + " : ")
                if(not str(choix).isdigit()): print("Valeur impossible")
                elif(int(choix) < int(mini) or int(choix) > int(maxi)): print("Valeur impossible")
                else:
                    nombre = int(choix)
                    break

        elif nombre > nombre_a_trouver:

            os.system("cls")
            print(nombre, nombre_a_trouver)
            print(couleur + j_name + W + " : ")
            print("nombre entre " + str(mini) + " et " + str(maxi) + " : ")

            while True:

                choix = input("nombre plus petit que " + str(nombre) + " : ")
                if(not str(choix).isdigit()): print("Valeur impossible")
                elif(int(choix) < int(mini) or int(choix) > int(maxi)): print("Valeur impossible")
                else:
                    nombre = int(choix)
                    break

    print("Trouvé !")
    os.system("pause")
    return temps

def __askNombreATrouver(couleur : str, j_name : str, mini : int, maxi : int)->int:

    choix : str

    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print("A " + couleur + j_name + W + " de choisir un nombre")

    while True:
        choix = str(input(couleur + j_name + W + "  choisissez un nombre entre " + str(mini) + " et " + str(maxi) + " : "))
        if(not choix.isdigit()): print("Valeur impossible")
        elif(int(choix) < int(mini) or int(choix) > int(maxi)):print("Valeur impossible")
        else:break

    return int(choix)

def __checkWin(temps1:float,temps2:float, j1_name : str, j2_name : str)->str:

    winType : int

    B  = '\033[94m' # blue
    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # r

    if temps1 < temps2 :
        print("le gangnant est : " + B + j1_name + W)
        print(B + str(j1_name) + W + " a terminé en : " + str(temps1))
        print(R + str(j2_name) + W + " a terminé en : " + str(temps2))
        winType = 1
        os.system("pause")

    elif temps1 > temps2 :
        print("le gangnant est : "+ R + j2_name + W)
        print(B + str(j1_name) + W + " a terminé en : " + str(temps1))
        print(R + str(j2_name) + W + " a terminé en : " + str(temps2))
        winType = 2
        os.system("pause")
    else:
        print("égalité")
        print(B + str(j1_name) + W + " a terminé en : " + str(temps1))
        print(R + str(j2_name) + W + " a terminé en : " + str(temps2))
        winType = 0
        os.system("pause")

    if(winType == 0):
        winner = ""
    elif(winType == 1):
        winner = j1_name
    elif(winType == 2):
        winner = j2_name

    return winner

def __askForMaxi():

    maxi : str

    os.system("cls")
    maxi = str(input('Nombre max que lon peut rentrer : '))


    while(not maxi.isdigit()):
        print("Valeur impossible")
        maxi = str(input('Nombre max que lon peut rentrer : '))
        os.system("pause")

    return int(maxi)

def __askForMini():

    mini : str

    os.system("cls")
    mini = str(input('Nombre min que lon peut rentrer : '))

    while(not mini.isdigit()):
        print("Valeur impossible")
        mini = str(input('Nombre min que lon peut rentrer : '))
        os.system("pause")

    return int(mini)

def LaunchGame_devinettes(j1_name : str, j2_name : str)->str:

    nombre_a_trouver : int
    temps1 : float
    temps2 : float
    mini : int
    maxi : int

    winner = ""

    B  = '\033[94m' # blue
    R  = '\033[91m' # r

    maxi = __askForMaxi()

    mini = __askForMini()

    nombre_a_trouver = __askNombreATrouver(B, j1_name, mini, maxi)

    temps1 = __LaunchTurn(nombre_a_trouver, R, j2_name, mini, maxi)

    nombre_a_trouver = __askNombreATrouver(R, j2_name, mini, maxi)

    temps2 = __LaunchTurn(nombre_a_trouver, B, j1_name, mini, maxi)

    #Définition du vainqueur
    winner = __checkWin(temps1, temps2, j1_name, j2_name)

    #Retour
    return winner

if __name__ == "__main__":

    LaunchGame_devinettes("Nathan", "Jimmy")
