table=input("De quel nombre voulez-vous avoir la table de multiplication affichée  ? ")
table=int(table)
for i in range(table):
    
    print(f" {i} . {table} = {table*i}")
