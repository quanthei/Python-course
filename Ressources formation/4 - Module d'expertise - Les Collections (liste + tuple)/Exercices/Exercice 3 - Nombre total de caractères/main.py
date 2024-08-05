# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Nombre total de caractères"
#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

# 1 - for / len
sum_caracters = 0
for nom in noms:
    sum_caracters += len(nom)
print(f"Nombres total de caractères: {sum_caracters}")
    
#2 - Completion de liste + sum
sum_caracters_2 = sum([len(nom) for nom in noms])
print(f"Nombres total de caractères: {sum_caracters_2}")

# 3 - Join / len
noms_join = "".join(noms)
print(f"Nombres total de caractères: {len(noms_join)}")