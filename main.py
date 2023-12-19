from bs4 import BeautifulSoup
import requests

# link = 'https://tms.tpf.go.tz/'
link2 = 'https://www.selenium.dev/'


response = requests.get('https://tms.tpf.go.tz/')


if response.status_code == 200:
    link = response.text
    soup = BeautifulSoup(link, 'lxml')
    search = soup.find('h1', class_ = 'header_font_t').text
    print(search)
else:
    print(f'Error with retrieving the webpage. Status code: {response.status_code}')
    


# with open('Plate.txt', 'r') as plate_numbers:
#     plate_num = plate_numbers.read()
#     print(plate_num)
#     soup = BeautifulSoup(link2, 'lxml')
#     print(soup.prettify())

def automatic(nums):
    # print(nums)
    pass

automatic('T580DEB')