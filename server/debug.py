#!/usr/bin/env python3

from app import app
from app import db
from models import Owner, Pet

if __name__ == '__main__':
    with app.app_context():
        import ipdb; ipdb.set_trace()
