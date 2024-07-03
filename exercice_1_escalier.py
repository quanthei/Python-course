# 30 pixels
# faire une fonction
import turtle
#Creat the visual env
t = turtle.Turtle()
NB_OF_PIXELS_PER_SCALE = 30
nb_scales = 0
#------------------------------FUNCTIONS------------------------------
def ask_user_nb_scales() -> int:
    answer_nb_scales = 0
    while answer_nb_scales == 0:
        answer_nb_scales = input("Merci de rentrer le nombres d'escaliers que vous souhaitez dessiner: ")
        try: 
            answer_nb_scales = int(answer_nb_scales)
        except:
            print("Merci de rentrer uniquement un nombre entiers !")
    return answer_nb_scales

def create_a_scale(
                  isStartUp : bool = False 
                  ):
    #Finish/create the base of the scale
    if not isStartUp: 
        t.forward(NB_OF_PIXELS_PER_SCALE/4)
    else:
        t.forward(NB_OF_PIXELS_PER_SCALE/2)
    #Position face up
    t.left(90)
    #Scale up
    t.forward(NB_OF_PIXELS_PER_SCALE/2)
    #Position face right
    t.right(90)
    #Base of the next scale
    t.forward(NB_OF_PIXELS_PER_SCALE/4)
#------------------------------MAIN------------------------------
def main():
    #Ask the user about the numbers of scales he went to introduce
    nb_scales = ask_user_nb_scales()

    #Process the numbers of scales
    for i in range(0,nb_scales+1):
        if i == 0:
            create_a_scale(True)
        else:
            create_a_scale()
    #Stop the turtle movement
    t.done()
#------------------------------EXE------------------------------
main()