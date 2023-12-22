#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        v = models.storage.all()
        my_list = []
        result = []
        for key in v:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                my_list.append(v[key])
        for el in my_list:
            if (el.state_id == self.id):
                result.append(el)
        return (result)
