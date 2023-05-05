import requests
from bs4 import BeautifulSoup


class ProductElement:
    id = 0
    name = ""
    points = 0
    price = 0.00
    points_per_eur = 0.00

    def get_price(self):
        AMD_SEARCH_URL = "https://geizhals.de/?cat=cpuamdam4&asuch="
        INTEL_SEARCH_URL = "https://geizhals.de/?cat=cpu1151&asuch="
        SORTING_PHRASE = "&sort=p&bl1_id=30"

        if self.name.find("AMD") != -1:
            price_request = requests.get(AMD_SEARCH_URL + self.name + SORTING_PHRASE)
        else:
            price_request = requests.get(INTEL_SEARCH_URL + self.name + SORTING_PHRASE)

        price_table = BeautifulSoup(price_request.content, 'html.parser').find('div', class_="cell productlist__price")
        best_price_tag = price_table.find('span', class_="notrans").text.replace(",", ".").replace("€", "")
        self.price = float(best_price_tag)
        return self.price

    def get_points_per_eur(self):
        if self.price <= 0.00:
            return self.points
        else:
            self.points_per_eur = self.points/self.price
            return self.points_per_eur

product_list = []


URL = "https://benchmarks.ul.com/de/compare/best-cpus?amount=0&sortBy=SCOREALL&reverseOrder=true&types=DESKTOP&minRating=0"
r = requests.get(URL)
res = BeautifulSoup(r.content, 'html.parser')
tabel = res.find('tbody')

for element in tabel.find_all('tr'):
    product = ProductElement()
    product.id = int(element.find('td', class_='order-cell').text) #ID
    #product.points = int(element.find('span', class_='bar-score').text) #ID
    product.name = element.find('a', class_='OneLinkNoTx').text #Name
    product.get_price()
    product.get_points_per_eur()
    product_list.append(product)


sortPr = '↓'
sortPt = '↑'
sortPp = '↓'

print(f'{"Products":60} | {"Points":7}{sortPt:1} | {"Price":8}{sortPr:1} | Pt/€ {sortPp:1}')
print("--------------------------------------------------------------------------------------------")
for obj in product_list:
    print(f'{obj.name:60} | {obj.points:8d} | {obj.price:8.2f}€ | {obj.points_per_eur:6.2f}')
    

