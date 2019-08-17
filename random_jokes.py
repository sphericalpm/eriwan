#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from random import randint
from app.models import Joke
from app import db


def get_max_id():
    ''' return max id from table'''
    return db.session.query(db.func.max(Joke.id)).scalar()


def generate_random_int(max_id):
    '''generate random in from range '''
    for x in range(1):
        return randint(1, max_id)


def get_text(rand_id):
    ''' return text from random id '''
    return Joke.query.filter_by(id=rand_id).first().joke_text


if __name__ == '__main__':
    max_id = get_max_id()
    rand_int = generate_random_int(max_id)
    a = get_text(rand_int)
