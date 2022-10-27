from ctypes import wintypes
import os
import time

def LaunchGame_devinettes(j1_name : str, j2_name : str)->str:

    os.system("cls")
    maxi = str(input('Nombre max que lon peut rentrer : '))


    while(not maxi.isdigit()):
        print("Valeur impossible")
        maxi = str(input('Nombre max que lon peut rentrer : '))
        os.system("pause")


    mini = str(input('Nombre min que lon peut rentrer : '))
    while(not mini.isdigit()):
        print("Valeur impossible")
        mini = str(input('Nombre min que lon peut rentrer : '))
        os.system("pause")
    dansvar = True

    j1_name : str
    j2_name : str

    B  = '\033[94m' # blue
    W  = '\033[0m'  # white (normal)
    R  = '\033[91m' # r
    nombre : str
    trouve : bool
    partiefini : bool
    nombre_a_trouver : str
    winType : int
    temps1 : float
    temps2 : float
    winner = ""
    
    os.system("cls")
    
    nombre = 0
    print("A " + B + j1_name + W + " de choisir un nombre")
    os.system("pause")
    while True:
        nombre_a_trouver = str(input(B + j1_name + W + "  choisissez un nombre entre " + str(mini) + " et " + str(maxi) + " : "))
        if(not nombre_a_trouver.isdigit()):print("Valeur impossible")
        elif(int(nombre_a_trouver) < int(mini) or int(nombre_a_trouver) > int(maxi)):print("Valeur impossible")
        else:break
        
    partiefini = False
    trouve = False
    print("A " + R + j2_name + W + " de trouver")
    os.system("pause")
    os.system("cls")    

    while partiefini == False :

        temps1 = time.time()
        while trouve != True :
            

            if int(nombre) == int(nombre_a_trouver):
                trouve = True
                temps1 = time.time()-temps1
                break
            if int(nombre) < int(nombre_a_trouver):
                
                while True:
                    os.system("cls")

                    print(R +j2_name + W + " : ")
                    print("Nombre entre " + str(mini) + " et " + str(maxi) + " : ")
                    nombre = int(input("nombre plus grand que " + str(nombre) + " : "))

                    if(not str(nombre).isdigit()):print("Valeur impossible")
                    elif(int(nombre) < int(mini) or int(nombre) > int(maxi)):print("Valeur impossible")
                    else:break
                os.system("cls")
            if int(nombre) > int(nombre_a_trouver):
                
                while True:
                    os.system("cls")
                    print(R +j2_name + W + " : ")
                    print("nombre entre " + str(mini) + " et " + str(maxi) + " : ")
                    nombre = int(input("nombre plus petit que " + str(nombre) + " : "))

                    if(not str(nombre).isdigit()):print("Valeur impossible")
                    elif(int(nombre) < int(mini) or int(nombre) > int(maxi)):print("Valeur impossible")
                    else:break
                    
                os.system("cls")
        print("Trouvé !")
        os.system("pause")
        trouve = False
        while True:
            nombre_a_trouver = str(input(R + j2_name + W + "  choisissez un nombre entre " + str(mini) + " et " + str(maxi) + " : "))
            if(not nombre_a_trouver.isdigit()):print("Valeur impossible")
            elif(int(nombre_a_trouver) < int(mini) or int(nombre_a_trouver) > int(maxi)):print("Valeur impossible")
            else:break
                
        os.system("cls")

        nombre = 0       
        temps2 = 0    
        print("A " + B + j1_name + W + " de trouver")
        os.system("pause")
        os.system("cls")
        temps2 = time.time()
        while trouve != True :
            if int(nombre) == int(nombre_a_trouver):
                trouve = True
                temps2 = time.time()-temps2
                partiefini = True
                break

            if int(nombre) < int(nombre_a_trouver):
                    
                while True:
                    print(B +j1_name + W + " : ")
                    print("nombre entre " + mini + " et " + maxi + " : ")
                    nombre = str(input("nombre plus grand que " + str(nombre) + " : "))

                    if(not str(nombre).isdigit()):print("Valeur impossible")
                    elif(int(nombre) < int(mini) or int(nombre) > int(maxi)):print("Valeur impossible")
                    else:break
                os.system("cls")    
            if int(nombre) > int(nombre_a_trouver):
                    
                while True:
                    print(B +j1_name + W + " : ")
                    print("nombre entre " + str(mini) + " et " + str(maxi) + " : ")
                    nombre = str(input("nombre plus petit que " + str(maxi) + " : "))

                    if(not str(nombre).isdigit()):print("Valeur impossible")
                    elif(int(nombre) < int(mini) or int(nombre) > int(maxi)):print("Valeur impossible")
                    else:break
                os.system("cls")  
    while True:

        if temps1 < temps2 :
            print("le gangnant est : " + B + j1_name + W)
            print(B + str(j1_name) + W + " a terminé en : " + str(temps1))
            print(R + str(j2_name) + W + " a terminé en : " + str(temps2))
            winType = 2
            os.system("pause")
            break
        elif temps1 > temps2 :
            print("le gangnant est : "+ R + j2_name + W)
            print(B + str(j1_name) + W + " a terminé en : " + str(temps1))
            print(R + str(j2_name) + W + " a terminé en : " + str(temps2))
            winType = 1
            os.system("pause")
            break
        elif temps1 == temps2:
            print("égalité")
            print(B + str(j1_name) + W + " a terminé en : " + str(temps1))
            print(R + str(j2_name) + W + " a terminé en : " + str(temps2))
            winType = 1
            os.system("pause")
            break
    #Définition du vainqueur
    if(winType == -1):
        winner = ""
    elif(winType == 2):
        winner = j1_name
    elif(winType == 1):
        winner = j2_name

    #Retour
    return winner