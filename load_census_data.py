import csv

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

for fname, _class in [('ref_census_surnames.csv', Surname),
                      ('ref_census_firstnames_female.csv', FemaleFirstName),
                      ('ref_census_firstnames_male.csv', MaleFirstName)]:
    names = []
    with open(fname, 'rb') as csvfile:
        rdr = csv.reader(csvfile, delimiter=',')
        for row in rdr:
            names.append(_class(name=row[0],
                                freq=float(row[1]),
                                cum_freq=float(row[2]),
                                rank=int(row[3])))
        session.add_all(names)
        session.commit

print('Number of surnames: {}'.format(session.query(Surname).count()))
print('Number of female first names: {}'.format(session.query(FemaleFirstName).count()))
print('Number of male first names: {}'.format(session.query(MaleFirstName).count()))
