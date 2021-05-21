################################################################################ View

import time

def Intro1():
    chapeau(24)
    print("Bonjour et bienvenue :) \n Comment t'appelles-tu ?")

def Intro2(nom_user,nbre_questions_max):
    print("Enchanté {} ! Je suis le Choixpeau. \n Je vais t'assigner à la Maison qui te correspond le plus, en fonction de tes réponses".format(nom_user))
    print("Combien de questions puis-je te poser ? (Maximum : {} questions)".format(nbre_questions_max))

def Intro3(nbre_questions):
    print("Entendu ! Je vais donc te poser : {} questions".format(nbre_questions))
    print("Commençons !")

def fin_test(user,maison,statistiques):
    print("Voilà {}, c'est terminé !".format(user.nom))
    print("Voyons voir......")
    time.sleep(3)
    print("Ah oui c'est évident !")
    time.sleep(2)
    chapeau(24)
    for i in range(0,len(maison)):
        print("{} !!!!".format(maison[i]))
        print()
    for i in range(0,8,2):
        print("{:>3} | {:>6.2f} % ".format(statistiques[i],statistiques[i+1]*100))


def Affichage_Question(question):
    print (question)
    print ("Choisis une proposition en saisissant son numero. \n Si tu ne souhaites pas répondre, inscris un autre chiffre")


def chapeau(nbre_ligne):
    vide = " "
    char_triangle = "^"
    nbre_vide = nbre_ligne - 1     # Nombre de vide à insérer avant le ^
    print()
    for num_ligne in range(1, nbre_ligne-5):
        if (num_ligne == 1):
            nbre_char_triangle = 1
        else:
            nbre_char_triangle = 2 * num_ligne - 1
        print(vide * nbre_vide, char_triangle * nbre_char_triangle, vide * nbre_vide)
        nbre_vide -= 1
    for num_ligne in(nbre_ligne-5,nbre_ligne+1):
        nbre_char_triangle = 2*nbre_ligne + 1
        print(char_triangle * nbre_char_triangle)

def progression(i,nbre_questions):
    progress = i/nbre_questions *100
    print ("{:.1f} % complété".format(progress))