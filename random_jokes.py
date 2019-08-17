#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from random import choice, randint
from app.models import Joke
from app import db


def get_max_id():
    ''' return max id from table'''
    return db.session.query(db.func.max(Joke.id)).scalar()

max_id = get_max_id()

def generate_random_int(max_id=max_id):
    for x in range(1): 
        #print(randint(1,max_id))
        return randint(1,max_id)

rand_int = generate_random_int()

def get_text(rand_id=rand_int):
    return Joke.query.filter_by(id=rand_id).first().joke_text

def random_joke():
    ''' this is function return one random id'''
    all_jokes_id = []
    jokes = Joke.query.all()
    if len(jokes) == 0:
        print('database is empty!')
    else:
        #b = Joke.query.filter_by(id='1').first()
        for i in jokes:
            all_jokes_id.append(i.joke_text)

    #return b.id
    return choice(all_jokes_id)


if __name__ == '__main__':
    #a = random_joke()
    a = get_text()
    print(a)
