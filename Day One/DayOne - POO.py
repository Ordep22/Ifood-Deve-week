import pandas as pd
# TODO: Evoluting to the functional paradigm to the POO one
data  = pd.read_csv("feedbacks.csv",delimiter= ';')


#This class when it is instantiated takes the feedbacks and saves in note and comment variables
class Feedback:

    def __init__(self,note, comment):

        self.note  = note

        self.comment  = comment

#This class have methods that can analyze the values saved on the Feedback class
class FeedbackAnalizer:

    def __init__(self,feedbacks):

        self.feedbacks = feedbacks

    #Metods calculade NPS (Net Promoter Score)

    def NpsCalculate(self):

        detractors  = sum(1 for feedback in self.feedbacks if feedback.note <= 6)

        promoters  = sum( 1 for feedback in self.feedbacks if feedback.note >= 9)

        return print(f"NPS: {(promoters - detractors) /len(self.feedbacks) *100}")



#Itering on file in colunm note and save on a list parameter
#feedbacks  = [ Feedback(linha['nota'],linha['comentario']) for i, linha in dados.iterrows()] #List comprehetion

#Another way to find the feedbacks on file
fb = data.apply(lambda line: Feedback(line['note'],line['comment']),axis= 1) #Axis = one the function will read the lines

analizer  = FeedbackAnalizer(fb)

analizer.NpsCalculate()










