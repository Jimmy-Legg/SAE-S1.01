import os
import time


#----------------------------------------
# Demande au deuxième joueur les hypothèses sur le nombre entré par le premier 
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : int, str, str, int, int
#
#Sortie : temps qu'il a pris à trouver : float
#----------------------------------------
def __LaunchTurn(nombre_a_trouver : int, couleur : str, couleur1 : str, j_name : str, p_name : str, mini:int, maxi:int)->float:

    choix : str
    nombre : int
    R  = '\033[91m' # r
    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print(couleur + j_name + W + " à vous de jouer !")
    os.system("pause")

    temps = time.time()

    while True:

        print("Nombre entre " + str(mini) + " et " + str(maxi) + " : ")
        choix = input("Faites une première hypothèse : ")
        if(not str(choix).isdigit()):print(R + "Valeur impossible" + W),os.system("pause"),os.system("cls")
        elif(int(choix) < int(mini) or int(choix) > int(maxi)):print(R + "Valeur impossible" + W),os.system("pause"),os.system("cls")
        else:
            nombre = int(choix)
            break

    while True :

        if nombre == nombre_a_trouver:

            temps = time.time()-temps
            break

        elif nombre < nombre_a_trouver:

            os.system("cls")
            print(couleur + j_name + W + " : ")
            print("Nombre entre " + str(mini) + " et " + str(maxi) + " : ")

            while True:

                choix = input(couleur1 + p_name + W + " dit que c'est un nombre plus grand que " + str(nombre) + " : ")
                if(not str(choix).isdigit()): print(R + "Valeur impossible" + W),os.system("pause"),os.system("cls")
                elif(int(choix) < int(mini) or int(choix) > int(maxi)): print(R + "Valeur impossible" + W),os.system("pause"),os.system("cls")
                else:
                    nombre = int(choix)
                    break

        elif nombre > nombre_a_trouver:

            os.system("cls")
            print(couleur + j_name + W + " : ")
            print("nombre entre " + str(mini) + " et " + str(maxi) + " : ")

            while True:

                choix = input(couleur1 + p_name + W + " dit que c'est un nombre plus petit que " + str(nombre) + " : ")
                if(not str(choix).isdigit()): print(R + "Valeur impossible" + W),os.system("pause"),os.system("cls")
                elif(int(choix) < int(mini) or int(choix) > int(maxi)): print(R + "Valeur impossible" + W),os.system("pause"),os.system("cls")
                else:
                    nombre = int(choix)
                    break

    print('\033[93m' + "Trouvé !" + W)
    os.system("pause")
    return temps


#----------------------------------------
#Demande le nombre que l'autre joueur doit trouver 
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : str, str, int, int
#
#Sortie : nombre choisi : int
#----------------------------------------
def __askNombreATrouver(couleur : str, j_name : str, mini : int, maxi : int)->int:

    choix : str
    R  = '\033[91m' # r
    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print("A " + couleur + j_name + W + " de choisir un nombre")

    while True:
        choix = str(input(couleur + j_name + W + "  choisissez un nombre entre " + str(mini) + " et " + str(maxi) + " : "))
        if(not choix.isdigit()): print(R + "Valeur impossible" + W),os.system("pause"),os.system("cls")
        elif(int(choix) < int(mini) or int(choix) > int(maxi)):print(R + "Valeur impossible" + W),os.system("pause"),os.system("cls")
        else:break

    return int(choix)


#----------------------------------------
#Affiche le temps des deux joueurs et le joueur qui a gagné en comparant le temps des deux joueurs
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : float, float, str, str
#
#Sortie : Gagnant : str
#----------------------------------------
def __checkWin(temps1:float,temps2:float, j1_name : str, j2_name : str)->str:
    os.system("cls")
    winType : int

    B  = '\033[94m' # blue
    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # r

    if temps1 < temps2 :
        print("---------------------------")
        print("")
        print("le gangnant est : " + B + j1_name + W)
        print("")
        print("---------------------------")
        print("")
        print(B + str(j1_name) + W + " a terminé en : " + str(temps1)[0:4])
        print(R + str(j2_name) + W + " a terminé en : " + str(temps2)[0:4])
        print("")
        print("---------------------------")
        os.system("pause")
        winType = 1

    elif temps1 > temps2 :
        print("---------------------------")
        print("")
        print("le gangnant est : " + R + j2_name + W)
        print("")
        print("---------------------------")
        print("")
        print(B + str(j1_name) + W + " a terminé en : " + str(temps1)[0:4])
        print(R + str(j2_name) + W + " a terminé en : " + str(temps2)[0:4])
        print("")
        print(print("---------------------------"))
        os.system("pause")
        winType = 2
        
    else:
        print("égalité")
        print("---------------------------")
        print("")
        print("égalité")
        print("")
        print("---------------------------")
        print("")
        print(B + str(j1_name) + W + " a terminé en : " + str(temps1)[0:4])
        print(R + str(j2_name) + W + " a terminé en : " + str(temps2)[0:4])
        print("")
        print("---------------------------")
        os.system("pause")
        winType = 0

    if(winType == 0):
        winner = ""
    elif(winType == 1):
        winner = j1_name
    elif(winType == 2):
        winner = j2_name

    return winner


#----------------------------------------
# Demande le nombre Max que les joueurs vont pouvoir entrer 
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : None
#
#Sortie : Max : int
#----------------------------------------
def __askForMaxi():

    maxi : str

    os.system("cls")
    maxi = str(input('Nombre max que lon peut rentrer : '))


    while(not maxi.isdigit()):
        print("Valeur impossible")
        maxi = str(input('Nombre max que lon peut rentrer : '))
        os.system("pause")

    return int(maxi)


#----------------------------------------
# Demande le nombre Min que les joueurs vont pouvoir entrer 
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : None
#
#Sortie : Max : int
#----------------------------------------
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

    temps1 = __LaunchTurn(nombre_a_trouver, R, B,j2_name,j1_name, mini, maxi)

    nombre_a_trouver = __askNombreATrouver(R, j2_name, mini, maxi)

    temps2 = __LaunchTurn(nombre_a_trouver, B, R, j1_name, j2_name, mini, maxi)

    #Définition du vainqueur
    winner = __checkWin(temps1, temps2, j1_name, j2_name)

    #Retour
    return winner

if __name__ == "__main__":

    LaunchGame_devinettes("Nathan", "Jimmy")
