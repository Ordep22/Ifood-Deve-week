import pandas as pd
# TODO: Evoluir a implementação para separar melhor as responsabilidades (funcional)
#Read datas from CSV

class Feedback:

   #Creating the  construtuctor of the class
    def __init__(self,nota, comentario):
        self.nota  = nota
        self.comentario  = comentario


class FeedbackAnalizer:

    # Creating the  construtuctor of the class
    def __init__(self,feedbacks):

        self.feedbacks = feedbacks
    def calcular_nps(self):

        detratores  = sum( 1 for feedback in self.feedbacks if feedback.nota <= 6)

        promotores  = sum( 1 for feedback in self.feedbacks if feedback.nota >= 9)

        return (promotores - detratores) /len(self.feedbacks) *100


dados  = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Dev Week Ifood/feedbacks.csv",delimiter= ';')

feedbacks  = [ Feedback(linha['nota'],linha['comentario']) for i, linha in dados.iterrows()]

analisador  = FeedbackAnalizer(feedbacks)

nps  = analisador.calcular_nps()


