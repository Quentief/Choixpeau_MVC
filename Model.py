################################################################################ Model

import pandas as pd

excel_file = 'DB.xlsx'
questionnaire = pd.read_excel(excel_file, sheet_name="Feuil1")

nbre_questions_max = len(questionnaire)
liste_questions = questionnaire['Questions'].tolist()
liste_propositions = [{"G":questionnaire['Gryffondor'].tolist()[i], "P":questionnaire['Poufsouffle'].tolist()[i],
                      "Sd":questionnaire['Serdaigle'].tolist()[i], "Sp":questionnaire['Serpentard'].tolist()[i]}
                     for i in range(0,nbre_questions_max)]

class Joueur:
    def __init__(self,nom_user):
        self.nom = nom_user
        resultat = [0,0,0,0]
        self.points_G = resultat[0]
        self.points_P = resultat[1]
        self.points_Sd = resultat[2]
        self.points_Sp = resultat[3]

class Question:
    def __init__(self,indice_question):
        self.question = liste_questions[indice_question]
        self.proposition_0 = liste_propositions[indice_question][self.ordre_propositions[0]]
        self.proposition_1 = liste_propositions[indice_question][self.ordre_propositions[1]]
        self.proposition_2 = liste_propositions[indice_question][self.ordre_propositions[2]]
        self.proposition_3 = liste_propositions[indice_question][self.ordre_propositions[3]]
    def __str__(self):
        return "{} \n 1 - {} \n 2 - {} \n 3 - {} \n 4 - {}".format(self.question,self.proposition_0,self.proposition_1,self.proposition_2,self.proposition_3)
    def OrdrePropositions(self):
        ordre_propositions = ["G", "P", "Sd", "Sp"]
        shuffle(ordre_propositions)
        self.ordre_propositions = ordre_propositions

class Chapeau:
    def __init__(self,nbre_questions,ordre_propositions,reponse,joueur):
        self.nbre_questions = nbre_questions
        self.ordre_propositions = ordre_propositions
    def OrdreQuestions(self):
        resultat = [i for i in range(0, nbre_questions_max)]
        shuffle(resultat)
        resultat = resultat[0:nbre_questions]
        self.ordre_questions = resultat
    def Correspondance_Reponse(self):
        self.reponse = int(reponse)
        if 1 <= self.reponse and self.reponse <= 4:
            if self.ordre_propositions[self.reponse - 1] == "G":
                return [1, 0, 0, 0]
            elif self.ordre_propositions[self.reponse - 1] == "P":
                return [0, 1, 0, 0]
            elif self.ordre_propositions[self.reponse - 1] == "Sd":
                return [0, 0, 1, 0]
            elif self.ordre_propositions[self.reponse - 1] == "Sp":
                return [0, 0, 0, 1]
        else:
            return [0, 0, 0, 0]
    def Choix_Maison(self):
        self.joueur = joueur
        resultat = [self.joueur.points_G, self.joueur.points_P, self.joueur.points_Sd, self.joueur.points_Sp]
        somme_points = sum(resultat)
        Statistiques = ["Gryffondor ", joueur.points_G / somme_points, "Poufsouffle", joueur.points_P / somme_points,
                        "Serdaigle  ", joueur.points_Sd / somme_points, "Serpentard ", joueur.points_Sp / somme_points]

        points_max = max(resultat)
        position_max = [i for i, j in enumerate(resultat) if j == points_max]
        nbre_occurence = len(position_max)

        Maisons = []
        for i in range(0, nbre_occurence):
            if position_max[i] == 0:
                Maisons.append("Gryffondor")
            elif position_max[i] == 1:
                Maisons.append("Poufsouffle")
            elif position_max[i] == 2:
                Maisons.append("Serdaigle")
            elif position_max[i] == 3:
                Maisons.append("Serpentard")
        self.Maisons = Maisons
        self.Statistiques = Statistiques