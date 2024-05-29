import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get("https://g1.globo.com/")

content = response.content

site = BeautifulSoup(content,'html.parser' )

#html da noticia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})
for noticia in noticias:

    #título
    titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
    print(titulo.text)

    # print(noticia.prettify())

    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

    if(subtitulo):
        print(subtitulo.text)
    
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', ""])

news = pd.DataFrame(lista_noticias, columns=['titulo', 'subtitulo', 'link'])

news.to_excel('noticias.xlsx', index = False)
    
