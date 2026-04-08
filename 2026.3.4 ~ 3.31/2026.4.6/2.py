data = ["A", "B", "A", "C", "B", "D", "A"]

result = []

for i in data:
    if i not in result:
        result.append(i)
    
print(result)


