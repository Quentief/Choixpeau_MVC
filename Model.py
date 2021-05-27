################################################################################ Model

### codes à exécuter dans Terminal pour installer les Packages requis
# pip install pandas
# pip install openpyxl
import time

import pandas as pd
excel_file = 'DB.xlsx'
questionnaire = pd.read_excel(excel_file, sheet_name="Feuil1")

nbre_questions_max = len(questionnaire)
liste_questions = questionnaire['Questions'].tolist()
liste_propositions = [{"G":questionnaire['Gryffondor'].tolist()[i], "P":questionnaire['Poufsouffle'].tolist()[i],
                      "Sd":questionnaire['Serdaigle'].tolist()[i], "Sp":questionnaire['Serpentard'].tolist()[i]}
                     for i in range(0,nbre_questions_max)]

