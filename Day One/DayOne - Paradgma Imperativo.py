import pandas as pd
# TODO: Implemet the imperative paramenter to calc the Net Promoter Score (NPs)

# Read data from CSV
dados  = pd.read_csv("/Users/PedroVitorPereira/Documents/GitHub/Dev Week Ifood/feedbacks.csv",delimiter= ';')

detratores  = 0

promotores  = 0

notas  = dados['nota']


# Check the number of promother and detractors
for elemento in notas:

    if elemento >= 9:
        promotores += 1

    elif elemento <= 6:
        detratores += 1

# Calculate the NPS
## Noter between  seven and eigth are consider netral

nPs = (promotores - detratores) /len(notas) *100

print(nPs)
