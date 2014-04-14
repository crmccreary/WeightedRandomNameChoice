import csv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///census_data.db')
Base = declarative_base()


class Surname(Base):
    __tablename__ = 'surnames'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    freq = Column(Float)
    cum_freq = Column(Float)
    rank = Column(Integer)


class FemaleFirstName(Base):
    __tablename__ = 'female_first_names'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    freq = Column(Float)
    cum_freq = Column(Float)
    rank = Column(Integer)


class MaleFirstName(Base):
    __tablename__ = 'male_first_names'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    freq = Column(Float)
    cum_freq = Column(Float)
    rank = Column(Integer)

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
            names.append(_class(row[0],
                                float(row[1]),
                                float(row[2]),
                                int(row[3])))
        session.add_all(names)
        session.commit

