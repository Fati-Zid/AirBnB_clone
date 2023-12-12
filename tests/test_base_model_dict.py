#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

''' Scenario 1: Create 2 BaseModel instances without arguments => 2 different ids'''
print("Scenario 1:")
model1 = BaseModel()
model2 = BaseModel()
print(f"Model 1 ID: {model1.id}")
print(f"Model 2 ID: {model2.id}")
print(f"Model 1 is Model 2: {model1 is model2}")
print()

''' Scenario 2: Create 1 BaseModel instance without arguments + Create 1 BaseModel instance with the .to_dict() of the first instance'''
print("Scenario 2:")
original_model = BaseModel()
print(f"Original Model ID: {original_model.id}")
print("Original Model:")
print(original_model)
print()

''' Create a new model using the to_dict() of the original model '''
new_model_dict = original_model.to_dict()
new_model = BaseModel(**new_model_dict)
print(f"New Model ID: {new_model.id}")
print("New Model:")
print(new_model)
print(f"Original Model is New Model: {original_model is new_model}")

