from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Name(Base):
    __tablename__ = 'names'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    freq = Column(Float)
    cum_freq = Column(Float)
    rank = Column(Integer)
    discriminator = Column('type', String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}


class Surname(Name):
    __mapper_args__ = {'polymorphic_identity': 'surname'}


class FemaleFirstName(Name):
    __mapper_args__ = {'polymorphic_identity': 'female_first_name'}


class MaleFirstName(Name):
    __mapper_args__ = {'polymorphic_identity': 'male_first_name'}

