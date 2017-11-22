import pickle

values = ['camembert', 'coulomnier', 'brie']
file = open('cheeses.dat', 'wb')
pickle.dump(values, file)
file.close()

file = open('cheeses.dat', 'rb')
values_to_print = pickle.load(file)
file.close()

print(values_to_print)

to_add = sorted(['munster', 'gruyere'])
for value in to_add:
    values_to_print.append(value)
print(values_to_print)
