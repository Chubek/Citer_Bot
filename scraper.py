#scrape the quote

from bs4 import BeautifulSoup
import requests
import random


def random_page():
    page_num = random.randint(2, 2880)

    return "http://citation-celebre.leparisien.fr/liste-citation?nationalite=france&page=" + str(page_num)


def get_quote():
    url = random_page()
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    quotes = soup.findAll('q')

    final_quote = random.choice(quotes)

    return final_quote.string

print(get_quote())
