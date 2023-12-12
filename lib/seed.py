#!/usr/bin/env python3
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)

    dev_id = Column(Integer, ForeignKey('devs.id'))
    dev = relationship('Dev', back_populates='freebies')

    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship('Company', back_populates='freebies')

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

# Script goes here!
