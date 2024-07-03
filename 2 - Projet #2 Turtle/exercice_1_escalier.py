import turtle
t = turtle.Turtle()

NB_PIXELS_PER_SCALE = 30
nb_scales = 0

#---------------------------------FUNCTIONS---------------------------------
def ask_nb_scales() -> int:
    answer_nb_scales = 0
    while answer_nb_scales == 0:
        answer_nb_scales = input("Combien de marches pour votre escalier: ")
        try:
            answer_nb_scales = int(answer_nb_scales)
        except:
            answer_nb_scales = 0
            print("Merci d'indiquer uniquement un nombre entier !") 
    return answer_nb_scales

def create_scale(
                nb_of_scales : int
                ):
    for i in range(0, nb_of_scales):
        #Create/finish the scale base
        #First round
        if i == 0: t.forward(NB_PIXELS_PER_SCALE)
        #Face up
        t.left(90)
        #Line up
        t.forward(NB_PIXELS_PER_SCALE)
        #Face right
        t.right(90)
        #Continue next scale
        t.forward(NB_PIXELS_PER_SCALE)

#---------------------------------MAIN---------------------------------
def main():
    #Demande à l'utilisateur le nombre de scales qu'il souhaite créer
    nb_scales = ask_nb_scales()
    
    #On creer l'escalier avec le nombre de marches correspondantes
    create_scale(nb_scales)
    
    #Figer le programme
    turtle.done()

#---------------------------------EXE---------------------------------
main()
