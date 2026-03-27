import string
def compteur_lettres(mot):
    nombre_lettre=0
    for lettre in mot:
        if lettre.lower() in list(string.ascii_lowercase):
           #lower pour tout mettre en minuscule avant de compter
           #nombre_lettre=nombre_lettre+1
           nombre_lettre+=1 #sert à augmenter la valeur d'une unité de la variable nombre_lettres

    return nombre_lettre
phrase="Je voudrais un couscous tagine"

nombre_lettres=compteur_lettres(phrase)
print("Dans la phrase : ")
print(phrase)
print(f"il y a {nombre_lettres} lettres")
