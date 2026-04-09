import random 

 
recommencer=True
while recommencer :
   nombre_inconnu=random.randint(1,20)
   proposition=int()
   while proposition != nombre_inconnu :
    proposition=input("faites une proposition...")
    proposition=int(proposition)

    #proposition = int(input("Donne un nombre : "))while proposition != 42:  print("Ce n'est pas 42")    proposition = int(input("Réessaie : "))print("Bravo, tu as trouvé 42 !")
    if proposition==nombre_inconnu:
        print("bravo vous avez gagné !")
        print("Vive les crêpes à la queue de taupe .")
        recommencer=input("Voulez-vous recommencer (o/n)?")
        while recommencer not in ["o","n"]:
            print("veuillez répondre par oui(o) ou non(n)")
            recommencer=input("voulez-vous recommencer (o/n)?")
        if recommencer =="o" : recommencer=True
        else : recommencer=False

    elif proposition<nombre_inconnu:
        print("Le nombre recherché est plus grand banane.")
    elif proposition>nombre_inconnu:
        print("Le nombre recherché est plus petit crétin.")
    
