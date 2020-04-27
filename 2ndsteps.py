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
myfile=open('examples.txt')
# print(myfile.readlines())
myfile.seek(0)
myfile.close()


# Statements

if True:
    print('Its True\n')

list_sum=0
list_2=[1,2,3,4,5]

for i in list_2:
    list_sum += i
    print(list_sum)

# Important, use of for in an unassigned counter
# We use _
for _ in 'Noopur Mishra':
    print('Hot!!')

# tuple unpacking
list_3=[(1,2),(3,4),(5,6),(7,8)]
for a,b in list_3:
    print(f'{a} is a pair of {b}')
