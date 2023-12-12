#!/usr/bin/python3
''' Test module for BaseModel.
 This module contains test cases for the BaseModel class.'''

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    ''' Test cases for the BaseModel class.'''

    def test_save_method(self):
        '''Test the save() method.'''
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        '''Test the to_dict() method.'''
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        obj_dict = my_model.to_dict()

        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertIn("id", obj_dict)

    def test_id_attribute(self):
        '''Test the id attribute.'''
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_created_at_attribute(self):
        '''Test the created_at attribute.'''
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_str_method(self):
        '''Test the __str__() method.'''
        my_model = BaseModel()
        self.assertIn("[BaseModel]", str(my_model))
        self.assertIn("({})".format(my_model.id), str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

if __name__ == "__main__":
    unittest.main()
