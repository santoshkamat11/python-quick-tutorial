# dictionaries. kind of key value pair
data={
    'name' : 'durgesh',
    'address' : 'Lucknow'
}

print(data['name'])

print("printing dictionary")
for key in data.keys():
    print(key,"=>",data.get(key))

print("print all values")
print(data.values())

print("iterating through values one by one")
for v in data.values():
    print(v)