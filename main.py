
import requests
from bs4 import BeautifulSoup

URL = "https://benchmarks.ul.com/de/compare/best-cpus?amount=0&sortBy=SCOREALL&reverseOrder=true&types=DESKTOP&minRating=0"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")


job_elements = soup.find_all("a", class_="OneLinkNoTx")

for job_element in job_elements:
    title_element = job_element.text
    print(title_element)

'''

class productClass:
    id = 0
    name = " "
    points = 0
    price = 0.00


liste = []

for i in range(1,6):
    product = productClass()
    product.name = "I5-" + str(i) + "2800"
    product.points = i*100
    product.price = 25.99*i
    liste.append(product)



sortPr = '↓'
sortPt = '↑'
sortPp = '↓'

print(f'{"Product":40} | {"Points":7}{sortPt:1} | {"Price":8}{sortPr:1} | Pt/€ {sortPp:1}')
print("------------------------------------------------------------------------")
for obj in liste:
    print(f'{obj.name:40} | {obj.points:8d} | {obj.price:8.2f}€ | {obj.points / obj.price:6.2f}')
    
'''