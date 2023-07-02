import pandas as pd


# TODO: Evoluir a implementação para separar melhor as responsabilidades (funcional)
#Read datas from CSV

dados  = pd.read_csv("feedbacks.csv",delimiter= ';')

notas  = dados['nota'] #Do arquivos csv estamos buscando somente a coluna com o cabeçalho notas

def CalcNps(notas):

    detratores  = notas.apply(lambda nota: nota <= 6).sum()

    #As avaliações contidas entre o intervalo de 6 até 9 não são analisados pois são considerados neutros

    promotores  = notas[notas >=9].count()

    return print(f"NPS: {(promotores - detratores)/ len(notas)*100}")


CalcNps(notas)
