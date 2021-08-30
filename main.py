from bs4 import BeautifulSoup
import requests
from selenium import webdriver

def get_page():
    url = f"https://tms.tpf.go.tz"
    plate_names(url)



def plate_names(url):
    response = requests.get(url)

    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    container = soup.find('section', class_ = 'container')
    title = container.find('div', class_ = 'list_header').text
    lists = container.find('div', class_ = 'list_wrap')
    com = lists.find('ul', class_ = 'directory-list active')
    lis_coms = com.find_all('li', class_ = 'provider provider-row')

    for lis_com in lis_coms:   #could not figure out how to for index, lis_com in enumerate(lis_coms): and make it count continuosly for the multiple pages
        compa = lis_com.find('h3', class_ = 'company_info')
        company = compa.find('a').text

        print(f'{company} \n')
    print('')


if __name__ == '__main__':
    for index, x in enumerate(range(0, 3)):
        get_page(x)
        plate_names()
