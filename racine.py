from math import sqrt

print("Bonjour et bienvenue dans ce programme de calcul des racines d'une fonction du deuxième degré.")
print("Dans la fonction y=ax²+bx+c,")

a=input("Quelle est la valeur de a ? ")
b=input("Quelle est la valeur de b ? ")
c=input("Quelle est la valeur de c ? ")

a=float(a)
b=float(b)
c=float(c)

delta=b**2-4*a*c


if delta < 0 :
    
    print("Il n'y a pas de racine à cette fonction")
     
elif delta == 0 :
    x=(-b)/(2*a)
    print("Il y a une racine à cette fonction")
    print(f"Sa valeur est de : x={round(x,4)}")  

elif delta > 0 :
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)

    print("Il y a deux racines à cette fonction.")
    print(f"la valeur de la première est de : x1={round(x1,4)}")
    print(f"la valeur de la première est de : x2={round(x2,4)}")
    
    print("Au revoir !")
 
