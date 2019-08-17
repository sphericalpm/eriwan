#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from random import shuffle
from app.models import Joke


def random_joke():
    ''' this is function return one random id'''
    all_jokes_id = []
    jokes = Joke.query.all()
    if len(jokes) == 0:
        print('database is empty!')
    else:
        for i in jokes:
            all_jokes_id.append(i.id)

    shuffle(all_jokes_id)
    random_id = all_jokes_id[0]
    a = Joke.query.filter_by(id=random_id).first()
    #print(a.joke_text)
    return a.joke_text


if __name__ == '__main__':
    random_joke()
