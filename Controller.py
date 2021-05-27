################################################################################ Controller
from Model import Joueur, nbre_questions_max, Chapeau
from View import Intro1


def Start():
    Intro1()
    nom_user = input("Inscris ton prénom")
    joueur = Joueur(nom_user)
    Intro2(joueur.nom,nbre_questions_max)
    nbre_questions = input("Saisir le nombre de questions à poser : ")
    nbre_questions = int(nbre_questions)
    Intro3(nbre_questions)
    for i in range(0, nbre_questions):
        progression(i, nbre_questions)
        question = Question()
        chapeau = Chapeau(nbre_questions, ordre_propositions, reponse, joueur)
        indice_questionnaire = ordre_questions[i]
        ordre_propositions = OrdrePropositions()
        question = Question(indice_questionnaire, ordre_propositions)
        Affichage_Question(question)
        reponse = input("Votre réponse :")
        resultat = Correspondance_Reponse(reponse,ordre_propositions)
        joueur.points_G += resultat[0]
        joueur.points_P += resultat[1]
        joueur.points_Sd += resultat[2]
        joueur.points_Sp += resultat[3]
    maisons,statistiques = Choix_Maison(joueur)
    fin_test(joueur,maisons,statistiques)