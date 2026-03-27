def compteur_lettres(mot):
    nombre_lettre=0
    for lettre in mot:
        #nombre_lettre=nombre_lettre+1
        nombre_lettre+=1 #sert à augmenter la valeur d'une unité de la variable nombre_lettres

    return nombre_lettre
print(compteur_lettres("chateau"))
