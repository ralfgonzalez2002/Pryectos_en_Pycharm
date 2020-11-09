import json

#Para usar los json
#with open('file.json') as file: #modo lectura
#    file_dict = json.loads(file.read())
with open('file.json') as file: #modo objeto
    file_dict = json.load(file)

print(file_dict)
print(file_dict['name'])
print(file_dict['interests'])
print(file_dict['interests'][2])
print(file_dict['last articles'])
print(file_dict['last articles']['clothes'])

#Para devolver un json (crerlo) hacemos:

person_dict = {"name": "Clark",
               "lastname": "Kent",
               "nickname": "Superman",
               "lenguages": ["Kriptonian", "English"]}
with open('customer.json', 'w') as customer: #modo objeto
    json.dump(person_dict, customer)

with open('customer.json') as customer: #modo objeto
    customer_dict = json.load(customer)

print(customer_dict)