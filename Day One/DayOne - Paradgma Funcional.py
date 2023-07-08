import pandas as pd

#TODO: Evolution of the imperative paradigm for the funcinal one, better organizing the code structure

#Read datas from CSV
dados  = pd.read_csv("feedbacks.csv",delimiter= ';')

#From the CSV file we want find the values that are in the note column
notas  = dados['note']

def CalcNps(notas):

    detratores  = notas.apply(lambda note: note <= 6).sum()

    ### Noter between  seven and eigth are consider netral
    promotores  = notas[notas >=9].count()

    return print(f"NPS: {(promotores - detratores)/ len(notas)*100}")


CalcNps(notas)
