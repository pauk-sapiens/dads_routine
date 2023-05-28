#!/venv/bin/python3
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_stock(html):
    soup = BeautifulSoup(html, features='html.parser')
    t = soup.find('table', {'class': 'datatable_table__D_jso datatable_table--border__B_zW0 datatable_table--mobile-basic__W2ilt datatable_table--freeze-column__7YoIE'})
    children = t.findChildren()
    i = 0
    d = []
    for child in children:
        if i == 20:
            d.append(child.text)
        if i == 25:
            d.append(child.text)
        if i == 182:
            d.append(child.text)
        i += 1
    return d


def get_html(url):
    r = requests.get(url)
    return r.text


def main():
    stocks = {
            'tmos': 'https://ru.investing.com/etfs/tmos-historical-data',
            'sbgb': 'https://ru.investing.com/etfs/sberbank-indeks-mosbirzhi-gosudar-historical-data',
            'itot': 'https://ru.investing.com/etfs/ishares-core-s-p-tot-us-stock-mrkt-historical-data',
            'ewz': 'https://ru.investing.com/etfs/ishares-brazil-index-historical-data',
            'ewu': 'https://ru.investing.com/etfs/ishares-msci-uk-historical-data',
            'ewg': 'https://ru.investing.com/etfs/ishare-msci-germany-historical-data',
            '2846': 'https://ru.investing.com/etfs/ishares-csi-300-a-share-historical-data',
            'vglt': 'https://ru.investing.com/etfs/vanguard-long-term-gov.-bond-historical-data',
            'bil': 'https://ru.investing.com/etfs/spdr-lehman-1-3-month-t-bill-historical-data'
           }
    dicto = {}
    for stock in stocks:
        dicto.setdefault(stock, get_stock(get_html(stocks[stock])))
    with open('stocks.txt', 'w') as f:
        for res in dicto:
            s = (res + ' current: ' + dicto[res][0] + dicto[res][1]).ljust(26, ' ') + '| month ago: ' + dicto[res][2] + '\n'
            f.write(s)
        f.write(str(datetime.now())[0:16])


if __name__ == '__main__':
    main()



