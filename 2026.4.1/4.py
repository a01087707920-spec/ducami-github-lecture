dict1 = dict({'자바': 80, 'PHP': 90, 'HTML': 70})

dict1['파이썬'] = 100
print(dict1)
del dict1['PHP']
print(dict1)
dict1['자바'] = 100
print(dict1)
dict1.clear()
print(dict1)