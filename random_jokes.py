#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import random
#from flask_sqlalchemy import SQLAlchemy

#from app import models
from app.models import Joke


def get_all_id():
    jokes = Joke.query.all()
    for i in jokes:
        print(i.joke_text)


def random_jokes():
    pass


if __name__ == '__main__':
    get_all_id()
