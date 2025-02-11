from ucimlrepo import fetch_ucirepo 
  
# busca conjunto de dados
bank_marketing = fetch_ucirepo(id=222) 
  
# data (as pandas dataframes) 
X = bank_marketing.data.features 
y = bank_marketing.data.targets 
  
# metadados
print(bank_marketing.metadata) 
  
# informações das variaveis 
print(bank_marketing.variables) 