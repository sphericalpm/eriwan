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
    return all_jokes_id[0]


if __name__ == '__main__':
    random_joke()
