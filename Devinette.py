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

    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # r
    N  = '\033[90m' # noir
    O  = '\033[93m' # yellow
    P  = '\033[95m' # purple
    G  = '\033[92m' # green

    os.system("cls")
    print("-----------------------------------")
    print(couleur + j_name + W + " à vous de jouer !" + N + " (Appuyez pour lancer le chronomètre)" + W)
    print("-----------------------------------")
    print("Nombre entre " + O + str(mini) + W + " et " + P + str(maxi) + W + " : ")
    os.system("pause")
    os.system("cls")

    temps = time.time()

    print("-----------------------------------")
    print(couleur + j_name + W + " à vous de jouer !")
    print("-----------------------------------")

    while True:

        print("Nombre entre " + O + str(mini) + W + " et " + P + str(maxi) + W + " : ")
        choix = input("Faites une première hypothèse : ")
        if(not str(choix).isdigit() or int(choix) < int(mini) or int(choix) > int(maxi)):
            os.system("cls")
            print("-----------------------------------")
            print(couleur + j_name + W + " à vous de jouer ! " + R + "Valeur impossible" + W)
            print("-----------------------------------")
        else:
            nombre = int(choix)
            break

    while True :

        if nombre == nombre_a_trouver:

            temps = time.time()-temps
            break

        else:
            os.system("cls")


            print("-----------------------------------")
            print(couleur + j_name + W + " à vous de jouer !")
            print("-----------------------------------")
            while True:

                print("Nombre entre " + O + str(mini) + W + " et " + P + str(maxi) + W + " : ")
                if(nombre > nombre_a_trouver): choix = input(couleur1 + p_name + W + " dit que c'est un nombre plus " + O + "petit " + W + "que " + G + str(nombre) + W + " : ")
                if(nombre < nombre_a_trouver): choix = input(couleur1 + p_name + W + " dit que c'est un nombre plus " + P + "grand " + W + "que " + G + str(nombre) + W + " : ")
                if(not str(choix).isdigit() or int(choix) < int(mini) or int(choix) > int(maxi)):
                    os.system("cls")
                    print("-----------------------------------")
                    print(couleur + j_name + W + " à vous de jouer ! " + R + "Valeur impossible" + W)
                    print("-----------------------------------")
                else:
                    nombre = int(choix)
                    if(nombre_a_trouver != nombre_a_trouver): os.system("cls")
                    break
    
    print("-----------------------------------")
    print(G + "Trouvé ! " + W + "Le nombre était bien : " + G + str(nombre_a_trouver) + W)
    print("-----------------------------------")
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

    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # red
    O  = '\033[93m' # yellow
    P  = '\033[95m' # purple

    os.system("cls")
    print("Tour de " + couleur + j_name + W + " :")

    while True:
        choix = str(input("Choisissez un nombre entre " + O + str(mini) + W + " et " + P + str(maxi) + W + " : "))
        if(not choix.isdigit() or int(choix) < int(mini) or int(choix) > int(maxi)):
            os.system("cls")
            print("Tour de " + couleur + j_name + W + " :")
            print(R + "Valeur impossible" + W)
        else: break

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
        winner =j1_name

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
        print("---------------------------")
        os.system("pause")
        winner = j2_name

    else:
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
        winner = ""

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
def __askForMaxi(mini : int):

    maxi : str
    maxi_ok : bool

    W  = '\033[0m'  # white (normal)
    P  = '\033[95m' # purple
    R  = '\033[91m' # red
    O  = '\033[93m' # yellow

    os.system("cls")
    maxi = input('Définissez le nombre ' + P + 'maximum' + W + ' que pourront entrez les joueurs : ')

    maxi_ok = False

    while(not maxi_ok):

        if(not maxi.isdigit()):
            print(R + "Valeur impossible !" + W)
            os.system("pause")
            os.system("cls")
            maxi = input('Définissez le nombre ' + P + 'maximum' + W + ' que pourront entrez les joueurs : ')
        elif(int(maxi) <= mini):
            print(R + "Le" + P + " Maximum" + R +" doit être plus élevé que le " + O +"minimum" + R + " !" + W)
            os.system("pause")
            os.system("cls")
            maxi = input('Définissez le nombre ' + P + 'maximum' + W + ' que pourront entrez les joueurs : ')
        else:
            maxi_ok = True

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

    W  = '\033[0m'  # white (normal)
    O  = '\033[93m' # yellow
    R  = '\033[91m' # red

    os.system("cls")

    mini = str(input('Définissez le nombre ' + O + 'minimum' + W + ' que pourront entrez les joueurs : '))

    while(not mini.isdigit()):
        print(R + "Valeur impossible" + W)
        os.system("pause")
        os.system("cls")
        print("")
        mini = str(input('Définissez le nombre ' + O + 'minimum' + W + ' que pourront entrez les joueurs : '))


    return int(mini)

def LaunchGame_devinettes(j1_name : str, j2_name : str)->str:

    nombre_a_trouver : int
    temps1 : float
    temps2 : float
    mini : int
    maxi : int

    B  = '\033[94m' # blue
    R  = '\033[91m' # r

    mini = __askForMini()

    maxi = __askForMaxi(mini)

    nombre_a_trouver = __askNombreATrouver(B, j1_name, mini, maxi)

    temps1 = __LaunchTurn(nombre_a_trouver, R, B,j2_name, j1_name, mini, maxi)

    nombre_a_trouver = __askNombreATrouver(R, j2_name, mini, maxi)

    temps2 = __LaunchTurn(nombre_a_trouver, B, R, j1_name, j2_name, mini, maxi)

    #check et retour du vainqueur
    return __checkWin(temps1, temps2, j1_name, j2_name)


if __name__ == "__main__":
    LaunchGame_devinettes("Nathan","Justin")
