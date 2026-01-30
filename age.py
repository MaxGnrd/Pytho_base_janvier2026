from datetime import datetime
now=datetime.today().year

nom_1=input("quel est ton nom?")
annee_1=input("En quelle année est-tu né(e)?")
nom_2=input("comment s'apelle ton voisin?")
annee_2=input("En quelle année est-il né?")

annee_1=int(annee_1)
annee_2=int(annee_2)
age_1=now-annee_1
age_2=now-annee_2

print(f"{nom_1} a {age_1} ans.")
print(f"{nom_2} a {age_2} ans.")

if age_1 > age_2 :
    print(f"{nom_1} a {age_1-age_2} ans de plus que {nom_2}.")

elif age_2 > age_1 :
    print(f"{nom_2} a {age_2-age_1} ans de plus que {nom_1}.")



elif age_1==age_2 :
    print(f"{nom_1} et {nom_2} ont le meme age.")
