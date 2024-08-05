import turtle
t = turtle.Turtle()

answer_nb_carres = 0
px_size_carre = 0

#------------------------FUNCTIONS------------------------
def ask_user_nb_carres() -> int:
    answer_nb_carres = 0
    while answer_nb_carres == 0:   
        try:
            answer_nb_carres = int(input("Merci de préciser le nombre de carré sohaité : "))
        except:
            print("Merci de rentrer un nombre entier !")
    return answer_nb_carres

def ask_user_px_size_carre() -> int:
    answer_px_size_carre = 0
    while answer_px_size_carre == 0:   
        try:
            answer_px_size_carre = int(input("Merci de préciser la taille (en px) du carré : "))
        except:
            print("Merci de rentrer un nombre entier !")
    return answer_px_size_carre

def dessiner_carre(
                  nb_pixels : int
                  ):
    for i in range (0,4):
        t.forward(nb_pixels)
        t.left(90)
        
def dessiner_carres(
                   nb_carres : int,
                   taille_depart : int
                   ):
    taille_carre = taille_depart
    for i in range(1, nb_carres + 1):
        dessiner_carre(taille_carre)
        taille_carre = (i + 1) * taille_depart
    
#------------------------MAIN------------------------
def main():
    #Ask le user le nb de carres
    answer_nb_carres = ask_user_nb_carres()
    
    #Ask le user la taille du carre
    px_size_carre = ask_user_px_size_carre()
    
    #Dessine le carre
    dessiner_carres(answer_nb_carres, px_size_carre) 
    
    #Fige l env visuel
    turtle.done()   

#------------------------EXE------------------------
main()