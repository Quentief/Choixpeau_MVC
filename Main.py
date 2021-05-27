# ################################################################################ Model
#
# ### codes à exécuter dans Terminal pour installer les Packages requis
# # pip install pandas
# # pip install openpyxl
#
#
# import pandas as pd
# excel_file = 'DB.xlsx'
# questionnaire = pd.read_excel(excel_file, sheet_name="Feuil1")
#
# nbre_questions_max = len(questionnaire)
# liste_questions = questionnaire['Questions'].tolist()
# liste_propositions = [{"G":questionnaire['Gryffondor'].tolist()[i], "P":questionnaire['Poufsouffle'].tolist()[i],
#                       "Sd":questionnaire['Serdaigle'].tolist()[i], "Sp":questionnaire['Serpentard'].tolist()[i]}
#                      for i in range(0,nbre_questions_max)]
#
#
# ################################################################################ Controller
#
# from random import *
#
# class Question:
#     def __init__(self,indice_question,ordre_propositions):
#         self.question = liste_questions[indice_question]
#         self.proposition_0 = liste_propositions[indice_question][ordre_propositions[0]]
#         self.proposition_1 = liste_propositions[indice_question][ordre_propositions[1]]
#         self.proposition_2 = liste_propositions[indice_question][ordre_propositions[2]]
#         self.proposition_3 = liste_propositions[indice_question][ordre_propositions[3]]
#     def __str__(self):
#         return "{} \n 1 - {} \n 2 - {} \n 3 - {} \n 4 - {}".format(self.question,self.proposition_0,self.proposition_1,self.proposition_2,self.proposition_3)
#
# class User:
#     def __init__(self,nom_user,resultat):
#         self.nom = nom_user
#         self.points_G = resultat[0]
#         self.points_P = resultat[1]
#         self.points_Sd = resultat[2]
#         self.points_Sp = resultat[3]
#
# def OrdreQuestions(nbre_questions) :
#     ordre_questions = [i for i in range(0,nbre_questions)]
#     shuffle(ordre_questions)
#     return ordre_questions
#
# def OrdrePropositions():
#     ordre_propositions = ["G","P","Sd","Sp"]
#     shuffle(ordre_propositions)
#     return ordre_propositions
#
# def Correspondance_Reponse(reponse,ordre_propositions):
#     reponse = int(reponse)
#     if  1<= reponse and reponse <=4 :
#         if ordre_propositions[reponse-1] == "G" :
#             return [1,0,0,0]
#         elif ordre_propositions[reponse-1] == "P" :
#             return [0, 1, 0, 0]
#         elif ordre_propositions[reponse-1] == "Sd" :
#             return [0, 0, 1, 0]
#         elif ordre_propositions[reponse-1] == "Sp" :
#             return [0, 0, 0, 1]
#     else :
#         return [0,0,0,0]
#
# def Choix_Maison(user):
#         resultat = [user.points_G, user.points_P, user.points_Sd, user.points_Sp]
#         somme_points = sum(resultat)
#         Statistiques = ["Gryffondor ",user.points_G/somme_points,"Poufsouffle",user.points_P/somme_points,
#                         "Serdaigle  ",user.points_Sd/somme_points,"Serpentard ",user.points_Sp/somme_points]
#
#         points_max = max(resultat)
#         position_max = [i for i, j in enumerate(resultat) if j == points_max]
#         nbre_occurence = len(position_max)
#
#         Maisons = []
#         for i in range(0,nbre_occurence):
#             if position_max[i]==0:
#                 Maisons.append("Gryffondor")
#             elif position_max[i]==1:
#                 Maisons.append("Poufsouffle")
#             elif position_max[i]==2:
#                 Maisons.append("Serdaigle")
#             elif position_max[i]==3:
#                 Maisons.append("Serpentard")
#         return Maisons,Statistiques
#
# def Start():
#     Intro1()
#     nom_user = input("Inscris ton prénom")
#     resultat = [0, 0, 0, 0]  # Initialisation des points [Gryffondor, Poufsouffle,Serdaigle,Serpentard]
#     user = User(nom_user,resultat)
#     Intro2(user.nom,nbre_questions_max)
#     nbre_questions = input("Saisir le nombre de questions à poser : ")
#     nbre_questions = int(nbre_questions)
#     ordre_questions = OrdreQuestions(nbre_questions_max)  # Préparation de l'ordre aléatoire des questions à poser
#     ordre_questions = ordre_questions[0:nbre_questions]
#     Intro3(nbre_questions)
#     for i in range(0, nbre_questions):
#         progression(i, nbre_questions)
#         indice_questionnaire = ordre_questions[i]
#         ordre_propositions = OrdrePropositions()
#         question = Question(indice_questionnaire, ordre_propositions)
#         Affichage_Question(question)
#         reponse = input("Votre réponse :")
#         resultat = Correspondance_Reponse(reponse,ordre_propositions)
#         user.points_G += resultat[0]
#         user.points_P += resultat[1]
#         user.points_Sd += resultat[2]
#         user.points_Sp += resultat[3]
#     maisons,statistiques = Choix_Maison(user)
#     fin_test(user,maisons,statistiques)
#
#
# ################################################################################ View
#
# import time
#
# def Intro1():
#     chapeau(24)
#     print("Bonjour et bienvenue :) \n Comment t'appelles-tu ?")
#
# def Intro2(nom_user,nbre_questions_max):
#     print("Enchanté {} ! Je suis le Choixpeau. \n Je vais t'assigner à la Maison qui te correspond le plus, en fonction de tes réponses".format(nom_user))
#     print("Combien de questions puis-je te poser ? (Maximum : {} questions)".format(nbre_questions_max))
#
# def Intro3(nbre_questions):
#     print("Entendu ! Je vais donc te poser : {} questions".format(nbre_questions))
#     print("Commençons !")
#
# def fin_test(user,maison,statistiques):
#     print("Voilà {}, c'est terminé !".format(user.nom))
#     print("Voyons voir......")
#     time.sleep(3)
#     print("Ah oui c'est évident !")
#     time.sleep(2)
#     chapeau(24)
#     for i in range(0,len(maison)):
#         print("{} !!!!".format(maison[i]))
#         print()
#     for i in range(0,8,2):
#         print("{:>3} | {:>6.2f} % ".format(statistiques[i],statistiques[i+1]*100))
#
#
# def Affichage_Question(question):
#     print (question)
#     print ("Choisis une proposition en saisissant son numero. \n Si tu ne souhaites pas répondre, inscris un autre chiffre")
#
#
# def chapeau(nbre_ligne):
#     vide = " "
#     char_triangle = "^"
#     nbre_vide = nbre_ligne - 1     # Nombre de vide à insérer avant le ^
#     print()
#     for num_ligne in range(1, nbre_ligne-5):
#         if (num_ligne == 1):
#             nbre_char_triangle = 1
#         else:
#             nbre_char_triangle = 2 * num_ligne - 1
#         print(vide * nbre_vide, char_triangle * nbre_char_triangle, vide * nbre_vide)
#         nbre_vide -= 1
#     for num_ligne in(nbre_ligne-5,nbre_ligne+1):
#         nbre_char_triangle = 2*nbre_ligne + 1
#         print(char_triangle * nbre_char_triangle)
#
# def progression(i,nbre_questions):
#     progress = i/nbre_questions *100
#     print ("{:.1f} % complété".format(progress))

from Controller import Start

if __name__ == '__main__':
    Start()
