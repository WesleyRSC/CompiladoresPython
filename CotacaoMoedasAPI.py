import requests
import pandas as pd

response = requests.get("https://api.hgbrasil.com/finance/quotations?key=e5539d7a")
util = response.json()['results']['currencies']
util.pop("source")

keys_list= []
name_list=[]
buy_list=[]
sell_list=[]
variation_list=[]
    
for x in util:
    keys_list.append(x)
    name_list.append(util[x]['name'])
    buy_list.append(util[x]['buy'])
    sell_list.append(util[x]['sell'])
    variation_list.append(util[x]['variation'])


df = pd.DataFrame(
    {
        'Moeda':keys_list,
        'Nome':name_list,
        'Preco_Compra':buy_list,
        'Preco_Venda':sell_list,
        'Variacao':variation_list
    }
)

df.to_csv('New_file.csv',index=False)


print(keys_list)
print(name_list)
print(buy_list)
print(sell_list)
print(variation_list)

print(type(util))


