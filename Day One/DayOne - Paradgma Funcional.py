import pandas as pd
# TODO: Evoluir a implementação para separar melhor as responsabilidades (funcional)
#Read datas from CSV

def calcular_nps(notas):

    detratores  = 0

    promotores  = 0
    #Check the number of promother and detractors
    for elemento in notas:

        if elemento >= 9:
            promotores += 1

        elif elemento <= 6:
            detratores += 1

    #Calculate the NPS
    ##Notas 7 e 8 são notas neutras e elas não são avaliadas pelo NPS
    nPs = (promotores - detratores) /len(notas) *100

    print(nPs)


dados  = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Dev Week Ifood/feedbacks.csv",delimiter= ';')
notas  = dados['nota']
calcular_nps(notas)