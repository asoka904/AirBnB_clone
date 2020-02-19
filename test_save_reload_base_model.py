#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_dic = {"name": "Holberton", "my_number": 89, "id": "98133155-3396-4881-8c15-a9d480152017", "updated_at": "2020-02-19T20:39:44.760546", "created_at": "2020-02-19T20:39:44.760499", "__class__": "BaseModel"}
my_model = BaseModel(**my_dic)
#my_model.name = "Holberton"
#my_model.my_number = 89
my_model.save()
print(my_model)
