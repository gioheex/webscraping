from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('window-size=800,800')

browser = webdriver.Chrome(options=chrome_options)

browser.get('https://www.airbnb.com.br/')
sleep(1)

place = browser.find_element(By.XPATH, '//*[@id="bigsearch-query-location-input"]')
place.send_keys('São Paulo')
place.submit()
sleep(2)
page_content = browser.page_source
site = BeautifulSoup(page_content, 'html.parser' )

accomodations = site.find_all('div', attrs={'itemprop': 'itemListElement'})
for accomodation in accomodations:
    acco_description = accomodation.find('meta', attrs={'itemprop': 'name'})
    acco_url = accomodation.find('meta', attrs={'itemprop': 'url'})

    print('Description: ', acco_description['content'])
    print('URL: ', acco_url['content'])

    acco_price = accomodation.find('div', attrs={'style': '--pricing-guest-display-price-alignment: flex-start; --pricing-guest-display-price-flex-wrap: wrap; --pricing-guest-primary-line-font-size: 0.9375rem; --pricing-guest-primary-line-line-height: 1.1875rem; --pricing-guest-primary-line-unit-price-font-weight: var(--linaria-theme_typography-weight-medium600); --pricing-guest-primary-line-trailing-content-font-size: 0.875rem; --pricing-guest-secondary-line-font-size: 0.9375rem; --pricing-guest-secondary-line-line-height: 1.1875rem; --pricing-guest-secondary-line-color: #6A6A6A; --pricing-guest-explanation-disclaimer-font-size: 0.875rem; --pricing-guest-explanation-disclaimer-line-height: 1.125rem; --pricing-guest-primary-line-strikethrough-price-font-weight: 600; --pricing-guest-primary-line-qualifier-font-size: 0.9375rem; --pricing-guest-primary-line-qualifier-line-height: 19px;'})
    acco_price = acco_price.find_all('span')[1].text
    print(acco_price)

    acco_info = accomodation.find_all('span', attrs={'class' : 'dir dir-ltr'})
    # print(acco_info[0].text +' '+ acco_info[1].text)
    # for item in acco_info:
    #     print(item.text)
    acco_info =" ".join([info.text for info in acco_info])
    print(acco_info)
    print('detalhes da hospedagem: ', acco_info)
    # print(accomodation.prettify())
    print()