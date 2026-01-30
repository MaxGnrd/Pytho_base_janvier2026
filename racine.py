from math import sqrt

print("Bonjour et bienvenue dans ce programme de calcul des racines d'une fonction du deuxième degré.")
print("Dans l'équation y=ax²+bx+c,")

a=input("Quelle est la valeur de a? ")
b=input("Quelle est la valeur de b? ")
c=input("Quelle est la valeur de c? ")

a=float(a)
b=float(b)
c=float(c)

delta=b**2-4*a*c





if delta < 0:
    print("Delta n'as malheureusement pas de racines!")
     
elif delta== 0 :
    racine_1=-b/(2 * a)
    print(f"Delta n'as qu'une racine qui vaut {racine_1}")
      
elif delta > 0:
    racine_2 = (-b + sqrt(delta)) / (2 * a)
    racine_3= (-b - sqrt(delta)) / (2 * a)

    print(f"Delta a 2 racines qui valent {round(racine_2,5)} et {racine_3}")
     
else :
    print("error")

