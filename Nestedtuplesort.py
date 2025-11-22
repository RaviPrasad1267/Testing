# List of nested tuples
nested_tuples = [(3, 1, 4), (1, 5, 9), (2, 6, 5), (3, 5, 8)]
nested_tuples.sort(key=lambda x:x[0])  #first element sort
print(nested_tuples)

print('Tuple sorted using sorted method ')
res =sorted(nested_tuples,key=lambda x:x[1]) #second element
print(res)

