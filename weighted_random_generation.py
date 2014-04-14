import csv
import random
import bisect
import pprint
from operator import attrgetter
from collections import Counter

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import (Surname,
                   FemaleFirstName,
                   MaleFirstName)

engine = create_engine('sqlite:///census_data.db')
Session = sessionmaker(bind=engine)
session = Session()

surnames = sorted(session.query(Surname).all(), key=attrgetter('cum_freq'))
_surnames = [i.name for i in surnames]
cum_freq = [i.cum_freq for i in surnames]
surnames_picked = []
N=10000000
for i in range(N):
    x = random.random() * cum_freq[-1]
    surnames_picked.append(_surnames[bisect.bisect(cum_freq, x)])
most_common = Counter(surnames_picked).most_common(20)
pprint.pprint([(n,c/float(N)*100.0) for n,c in most_common])
