import pandas as pd
# TODO: Evoluir a implementação para separar melhor as responsabilidades (funcional)

data  = pd.read_csv("feedbacks.csv",delimiter= ';')

class Feedback:


    def __init__(self,note, comment):

        self.note  = note

        self.comment  = comment


class FeedbackAnalizer:


    def __init__(self,feedbacks):

        self.feedbacks = feedbacks

    def NpsCalculate(self):

        detractors  = sum(1 for feedback in self.feedbacks if feedback.note <= 6)

        promoters  = sum( 1 for feedback in self.feedbacks if feedback.note >= 9)

        return print(f"NPS: {(promoters - detractors) /len(self.feedbacks) *100}")



#Itering on file in colunm nota and save on a list parameter
#feedbacks  = [ Feedback(linha['nota'],linha['comentario']) for i, linha in dados.iterrows()] #List comprehetion

#Another way to find the feedbacks on file
fb = data.apply(lambda line: Feedback(line['note'],line['comment']),axis= 1) #Axis = one the function will read the lines

analizer  = FeedbackAnalizer(fb)

analizer.NpsCalculate()










