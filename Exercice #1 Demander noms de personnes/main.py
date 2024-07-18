#-------------------------FUNCTIONS-------------------------
def ask_name_to_add() -> str:
    name_to_add = input("Merci d'indiquer le nom à rajouter à la liste: ")
    if name_to_add == "": 
        return None
    return name_to_add

#-------------------------MAIN-------------------------     
def main():
    noms = []
    while True:
        name_to_add = ask_name_to_add()
        if name_to_add == None :
            print("Vous n'avez rien indiqué !")
            break
        noms.append(name_to_add)
    noms.sort()
    for i in noms:
        print(i)

#-------------------------EXE-------------------------
main()