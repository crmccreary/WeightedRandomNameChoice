import csv
import random
import bisect
from operator import attrgetter
from collections import Counter

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import (Base,
                   Surname,
                   FemaleFirstName,
                   MaleFirstName)

engine = create_engine('sqlite:///census_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

surnames = sorted(session.query(Surname).all(), key=attrgetter('cum_freq'))
_surnames = [i.name for i in surnames]
cum_freq = [i.cum_freq for i in surnames]
surnames_picked = []
for i in range(1000000):
    x = random.random() * cum_freq[-1]
    surnames_picked.append(bisect.bisect(cum_freq, x))
Counter(surnames_picked).most_common(20)
