#!/usr/bin/python3
''' BaseModel module '''

import uuid
from datetime import datetime

class BaseModel:
    ''' Defines common attributes/methods for other classes.'''

    def __init__(self):
        def __init__(self, *args, **kwargs):
        ''' Initialize BaseModel attributes.'''
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        ''' Return a string representation of the BaseModel.'''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        ''' Update updated_at attribute with the current datetime.'''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Return a dictionary representation of the BaseModel.'''
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
