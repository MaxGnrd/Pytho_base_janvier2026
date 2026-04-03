import math
def menu():
    print("Pour calculer l'aire d'un carré, tapez 1")
    print("Pour calculer l'aire d'un triangle, tapez 2")
    print("Pour calculer l'aire d'un cercle, tapez 3")
    print("Pour quitter le programme, tapez 0")
    choix=input("Votre choix")
    #choix=int(choix)#on met "int" pour que ce qu'on écrive soit considéré pas comme un caractère mais le convertit en nombre entier.
    
    
    valid=False
    while not valid :
        try:
            choix=int(choix)#pour convertir la string en un nombre entier on écrit int()
            if choix in [0,1,2,3]:
                valid=True
            else:
                raise
        except:
            print("Veuillez répondre par 0,1,2 ou 3")
            choix=input("Votre choix : ")
            

    if choix==1:
        aire_carre()
    elif choix==2:
        aire_triangle()
    elif choix==3:
        aire_cercle()
    elif choix==0:
        quit()

def quit():
    print("Au revoir !!!")
     # "quit" toujours bien de créer une fonction qui arrète le programme pour pouvoir rajouter plus façilement plus tard des trucs 

def aire_carre():
    cote=input("Quelle est la longueur du côté de votre carré ? ")
    cote=float(cote)
    aire_carre=cote**2
    print(f"L'aire de votre carré vaut : {aire_carre}")
    menu()
    #menu() pour qu'il affiche la réponse et direct après réaffiche le menu pour recommencer ; à l'infini
    #"f"=string de formatage dans lequel on place la valeur de la variable : le chiffre du côté du carré qu'on a donné

def aire_cercle():
    rayon=input("Quelle est la longueur du rayon de votre cercle ? ")
    rayon=float(rayon)
    aire_cercle=math.pi*rayon**2
    print(f"L'aire de votre cercle vaut : {round(aire_cercle,4)}")
    menu()


def aire_triangle():
    base=input("Quelle est la longueur de la base de votre triangle ? ")
    base=float(base)
    hauteur=input("Quelle est la hauteur de votre triangle ?")
    hauteur=float(hauteur)
    aire_triangle=(base*hauteur)/2
    print(f"L'aire de votre triangle vaut : {round(aire_triangle,4)}")
    menu()


if __name__=="__main__":
# dit quelles sont les fonction qui doit être exécutée au démarrage du fichier : au démarrage du code , on exécute la fonction menu
    menu()
#exécute la fonction menu
