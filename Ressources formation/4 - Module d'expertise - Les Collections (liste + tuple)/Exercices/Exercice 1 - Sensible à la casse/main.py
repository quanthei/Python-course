def element_in_liste(el, checked_list: list):
    if el.lower() in [element.lower() for element in checked_list]:
        return True
    return False

noms = ["Louise", "Maellia", "Valentine", "Anthony", "Jules", "Maxime"]

name_to_checked = "MaelLia"
name_to_checked = name_to_checked.lower().capitalize()

if element_in_liste(name_to_checked, noms):
    print(f"{name_to_checked} est présent(e)")
else:
    print(f"{name_to_checked} n'est pas là")
