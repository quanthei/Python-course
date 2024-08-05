import turtle
t = turtle.Turtle()

px_size_carre = 0
#------------------------FUNCTIONS------------------------
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
    
#------------------------MAIN------------------------
def main():
    #Ask le user la taille du carre
    px_size_carre = ask_user_px_size_carre()
    
    #Dessine le carre
    dessiner_carre(px_size_carre) * 3
    
    #Fige l env visuel
    turtle.done()   

#------------------------EXE------------------------
main()