################################################################################ Controller

from random import *

from Model import liste_questions, liste_propositions, nbre_questions_max
from View import Intro2, Intro1, Intro3, progression, Affichage_Question, fin_test


class Question:
    def __init__(self,indice_question,ordre_propositions):
        self.question = liste_questions[indice_question]
        self.proposition_0 = liste_propositions[indice_question][ordre_propositions[0]]
        self.proposition_1 = liste_propositions[indice_question][ordre_propositions[1]]
        self.proposition_2 = liste_propositions[indice_question][ordre_propositions[2]]
        self.proposition_3 = liste_propositions[indice_question][ordre_propositions[3]]
    def __str__(self):
        return "{} \n 1 - {} \n 2 - {} \n 3 - {} \n 4 - {}".format(self.question,self.proposition_0,self.proposition_1,self.proposition_2,self.proposition_3)

class User:
    def __init__(self,nom_user,resultat):
        self.nom = nom_user
        self.points_G = resultat[0]
        self.points_P = resultat[1]
        self.points_Sd = resultat[2]
        self.points_Sp = resultat[3]

def OrdreQuestions(nbre_questions) :
    ordre_questions = [i for i in range(0,nbre_questions)]
    shuffle(ordre_questions)
    return ordre_questions

def OrdrePropositions():
    ordre_propositions = ["G","P","Sd","Sp"]
    shuffle(ordre_propositions)
    return ordre_propositions

def Correspondance_Reponse(reponse,ordre_propositions):
    reponse = int(reponse)
    if  1<= reponse and reponse <=4 :
        if ordre_propositions[reponse-1] == "G" :
            return [1,0,0,0]
        elif ordre_propositions[reponse-1] == "P" :
            return [0, 1, 0, 0]
        elif ordre_propositions[reponse-1] == "Sd" :
            return [0, 0, 1, 0]
        elif ordre_propositions[reponse-1] == "Sp" :
            return [0, 0, 0, 1]
    else :
        return [0,0,0,0]

def Choix_Maison(user):
        resultat = [user.points_G, user.points_P, user.points_Sd, user.points_Sp]
        somme_points = sum(resultat)
        Statistiques = ["Gryffondor ",user.points_G/somme_points,"Poufsouffle",user.points_P/somme_points,
                        "Serdaigle  ",user.points_Sd/somme_points,"Serpentard ",user.points_Sp/somme_points]

        points_max = max(resultat)
        position_max = [i for i, j in enumerate(resultat) if j == points_max]
        nbre_occurence = len(position_max)

        Maisons = []
        for i in range(0,nbre_occurence):
            if position_max[i]==0:
                Maisons.append("Gryffondor")
            elif position_max[i]==1:
                Maisons.append("Poufsouffle")
            elif position_max[i]==2:
                Maisons.append("Serdaigle")
            elif position_max[i]==3:
                Maisons.append("Serpentard")
        return Maisons,Statistiques

def Start():
    Intro1()
    nom_user = input("Inscris ton prénom")
    resultat = [0, 0, 0, 0]  # Initialisation des points [Gryffondor, Poufsouffle,Serdaigle,Serpentard]
    user = User(nom_user,resultat)
    Intro2(user.nom,nbre_questions_max)
    nbre_questions = input("Saisir le nombre de questions à poser : ")
    nbre_questions = int(nbre_questions)
    ordre_questions = OrdreQuestions(nbre_questions_max)  # Préparation de l'ordre aléatoire des questions à poser
    ordre_questions = ordre_questions[0:nbre_questions]
    Intro3(nbre_questions)
    for i in range(0, nbre_questions):
        progression(i, nbre_questions)
        indice_questionnaire = ordre_questions[i]
        ordre_propositions = OrdrePropositions()
        question = Question(indice_questionnaire, ordre_propositions)
        Affichage_Question(question)
        reponse = input("Votre réponse :")
        resultat = Correspondance_Reponse(reponse,ordre_propositions)
        user.points_G += resultat[0]
        user.points_P += resultat[1]
        user.points_Sd += resultat[2]
        user.points_Sp += resultat[3]
    maisons,statistiques = Choix_Maison(user)
    fin_test(user,maisons,statistiques)