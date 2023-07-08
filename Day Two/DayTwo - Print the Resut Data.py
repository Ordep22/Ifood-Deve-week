"""
[PT-BR]

No segundo dia, a tarefa foi extrair dados do NPS e aplicar as técnicas de
ETL ( Extração, Transformação e Carregamento) nesses dados.
Com a ajuda da biblioteca matplotlib, criamos uma gráficos para visualizar e
compreender o nível de satisfação dos nossos clientes.

[EN]

On the second day, the task was to extract data from the NPS and applay
the technics of ETL (Extraction, Transform, and Load) on this data.
Whit the help of the matplot library, we create a plot to visualize and understande
the level of satisfaction of our clients

"""
from turtle import color

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patch


#Define the constant value to  view  the nps

## Nones of the NPS View
npsZones  = ["Critical", "Improvement" ,"Quality" ,"Excellence"]

##Limits of the NPS view
npsValues = [-100,0,50,75,100]

##Code of color that will show on graphic
npsColors = ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4']

#Read de CSV file
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

        nPsValue  =  (promoters - detractors) /(len(self.feedbacks) *100)

        return nPsValue, print(f"NPS: {(promoters - detractors) /len(self.feedbacks) *100}")




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



#Another way to find the feedbacks on file
fb = data.apply(lambda line: Feedback(line['note'],line['comment']),axis= 1) #Axis = one the function will read the lines

analizeNps  = FeedbackAnalizer(fb)

npsValue,_ = analizeNps.NpsCalculate()

CriateNpsGraphic(npsValue)






































