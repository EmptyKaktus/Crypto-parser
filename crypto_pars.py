import requests
from bs4 import BeautifulSoup as bs

# Сайт: https://ru.investing.com


class Price:
    def __init__(self, cur):
        self.cur = cur  # Берем название крипты

    def price(self):  # Функция возвращает цену крипты
        URL_TEMPLATE = f"https://ru.investing.com/crypto/{self.cur}"
        r = requests.get(URL_TEMPLATE)

        soup = bs(r.text, "html.parser")
        price = soup.find_all('span', class_='inlineblock')
        return price[2].text

    def status_code(self):  # Функция возвращает статус страницы
        URL_TEMPLATE = f"https://ru.investing.com/crypto/{self.cur}"
        r = requests.get(URL_TEMPLATE)
        return r.status_code

    def ticker(self):  # Возвращает тикер крипты
        URL_TEMPLATE = f"https://ru.investing.com/crypto/{self.cur}"
        r = requests.get(URL_TEMPLATE)

        soup = bs(r.text, "html.parser")
        ticker = soup.find_all("p")
        return ticker[17].text.split()[1].lower()

    def max_price(self):
        URL_TEMPLATE = f"https://ru.investing.com/crypto/{self.cur}"
        r = requests.get(URL_TEMPLATE)

        soup = bs(r.text, "html.parser")
        price = soup.find_all("p")
        return f"{'$'} {price[23].text.split(' - ')[1]}"

    def min_price(self):
        URL_TEMPLATE = f"https://ru.investing.com/crypto/{self.cur}"
        r = requests.get(URL_TEMPLATE)

        soup = bs(r.text, "html.parser")
        price = soup.find_all("p")
        return f"{'$'} {price[23].text.split(' - ')[0]}"

