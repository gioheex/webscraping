import requests
from bs4 import BeautifulSoup

url_base ='https://lista.mercadolivre.com.br/'

product_name =  str(input('insira o produto que deseja pesquisar: '))

response =  requests.get(url_base + product_name)

site = BeautifulSoup(response.text, 'html.parser')

products = site.findAll('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})
for product in products: 

    title = product.find('h2', attrs={'class': 'ui-search-item__title'})

    link = product.find('a', attrs={'class' : 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})

    currency = product.find('span', attrs={'class' : 'andes-money-amount__currency-symbol'})

    value_trunc = product.find('span', attrs={'class': 'andes-money-amount__fraction'})
    
    value_cents = product.find('span', attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-16'})

# print(product.prettify())
    print('titulo do produto: ', title.text)
    print('link do produto: ', link['href'])
    if value_cents == True:
        print('valor do produto: ', currency.text+  ' '+ value_trunc.text + ',' + value_cents.text)
    else:
        print('valor do produto: ', currency.text+  ' '+ value_trunc.text)
    print()
