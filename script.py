import requests
from bs4 import BeautifulSoup
import csv

def webscraper():

    url = "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield"

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    table = soup.find("table",{"class":"t-chart"})

    rows = table.findAll("tr")

    data_matrix = []

    for i in range(1, len(rows)):
        x = (list(rows[i].stripped_strings))
        data_matrix.append(x)

    with open('Treasury_data.csv','w') as CSVfile:
        CSVWriter = csv.writer(CSVfile)
        for ml in data_matrix:
            CSVWriter.writerow(ml)  

        
if __name__ == '__main__':
    webscraper()
