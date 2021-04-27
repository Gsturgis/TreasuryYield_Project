import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

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
            
def make_chart():
    df = pd.read_csv("Treasury_data.csv")
    df.columns = ['Date','1 Mo','2 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']
    fig = plt.figure(figsize=(16, 8))
    plt.plot(df['Date'],df['1 Yr'], label='Year 1')
    plt.plot(df['Date'],df['3 Yr'], label='Year 3')
    plt.plot(df['Date'],df['5 Yr'], label='Year 5')
    plt.plot(df['Date'],df['7 Yr'], label='Year 7')
    plt.plot(df['Date'],df['10 Yr'], label='Year 10')
    plt.plot(df['Date'],df['20 Yr'], label='Year 20')
    plt.plot(df['Date'],df['30 Yr'], label='Year 30')
    plt.suptitle('Treasury Yield curve rates(Yearly)')
    plt.xlabel('Dates')
    plt.ylabel('Interest')
    plt.grid()
    plt.legend()
    plt.savefig('charts/Treasury_curve.png')
    
    
    

        
if __name__ == '__main__':
    webscraper()
    make_chart()
