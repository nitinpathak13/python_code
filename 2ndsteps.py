# We will start with lists

list_1=['alpha','beta','gamma']
list_1.append('delta')
list_1.sort()
print(list_1)

# this is for dictionaries

dict_1 = {'xbox':'229','ps4':'199'}
print(dict_1['xbox'])
print(dict_1.keys())
print(dict_1.values())

# tuples

tup1=(12,34,56)
print ('\n')
print(tup1[0])

# files
myfile=open('myfile.txt')
print(myfile.readlines())
myfile.seek(0)
myfile.close()
