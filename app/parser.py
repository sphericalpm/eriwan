# parsing jokes from anekdotitut.ru
# 
import urllib.request
from urllib.parse import quote
from urllib.parse import unquote
from bs4 import BeautifulSoup
import re
from app.models import Joke
from app import db


def parse_anekdot():
    jokes_out = []
    for i in range(1, 10):
        url = url = 'https://anekdotitut.ru/pro_armyanskoe_radio' + str(
            i) + '.php'
        html_doc = urllib.request.urlopen(url)
        soup_doc = BeautifulSoup(html_doc, 'html.parser')
        jokes = soup_doc.body(class_='noselect', id=re.compile('anekdot\d+'))
        for joke in jokes:
            jokes_out.append(joke.text)
            if not bool(Joke.query.filter_by(joke_text='some_text').first()):
                j = Joke(joke_text=joke.text)
                db.session.add(j)
                db.session.commit()

    # return jokes_out

