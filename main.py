import requests
from bs4 import BeautifulSoup
import os

from Island import Island
import send_webhook as webhook


if __name__ == "__main__":
    url = os.getenv('DATA_SOURCE')
    response = requests.get(url)

    if response.status_code != 200:
        print(response.text)
        exit()

    soup = BeautifulSoup(response.text, 'html.parser')
    islands = soup.find_all(class_='col col-sm-4 pl-1 pr-1')

    data = list()
    for i in islands:
        data.append(Island(i.find('strong').text, i.find(class_='tfs14').text))

    webhook.send_webhook(data)

