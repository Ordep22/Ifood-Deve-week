#Day Three
"""
[PT-BR]

No segundo dia, vamos conectar nosso Google Colab ao Google Drive,
extrair dados do NPS e aplicar as técnicas de ETL (Extração, T
ransformação e Carregamento) nesses dados. Com a ajuda da biblioteca
matplotlib, criaremos gráficos para visualizar e compreender o nível de
satisfação dos nossos usuários.

[EN]


"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import openai




apiKey = 'INSERT YOUR API KEY'
openai.api_key = apiKey


#Define the constant value to  view  the nps
npsZones  = ["Critical", "Improvement" ,"Quality" ,"Excellence"]
npsValues = [-100,0,50,75,100]
npsColors = ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4']


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
        return (promoters - detractors) /len(self.feedbacks) *100


#This function will criate and show the NPS graphic
def CriateNpsGraphic(nps):

    #Criate a gaphic 10x2
    figure, axes  = plt.subplots(figsize =(10,2))

    #insert in the graphic the columuns and colors

    for i, zone in enumerate(npsZones):
        #left means where the bar will init
        axes.barh([0], width = npsValues[i+1] - npsValues[i],left= npsValues[i],color = npsColors[i])

    #Represent the nps result on graphic
    axes.barh([0],width= 0.5, left= nps, color = 'black')

    #Disable  y values
    axes.set_yticks([])

    #Set  x axes limit
    axes.set_xlim(-100,100)

    #Set the values on the x axes
    axes.set_xticks(npsValues)

    #Show the NPS values on the graphic
    plt.text(nps,0,f"{nps:.2f}",ha = "center",va = "center", color = "white")

    #Criate the legensd on the graphic
    patches  = [patch.Patch(color = npsColors[i], label = npsZones[i]) for i in range(len(npsZones))]
    plt.legend(handles = patches,bbox_to_anchor = (1,1))

    #insert the title on graphic
    plt.title("Nps Graphic Ifood Deve Week")

    plt.show()


def SentimentAnalyzer(feedbacks):

    formatedComments = "\n".join([f"- Nota {fb.note}: {fb.comment}" for fb in feedbacks])

    print(formatedComments)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {
            "role": "system",
             "content": "Você é uma model de análise de sentimento com foco em feedbakcs sobre experiencias do cunsumidor!"},

            {
                "role": "user",
                "content": f"Analise os seguintes comtários, classificando-o como Positivo, Nrutro ou Negativo {formatedComments}"
            }
        ]
    )

    return completion.choices[0].message.content




#Another way to find the feedbacks on file
feedback = Feedback(data['note'],data['comment'])

fb = data.apply(lambda line: Feedback(line['note'],line['comment']),axis= 1) #Axis = one the function will read the lines

analizeNps  = FeedbackAnalizer(fb)

npsValue = analizeNps.NpsCalculate()

CriateNpsGraphic(npsValue)

insigths  = SentimentAnalyzer(fb)



































