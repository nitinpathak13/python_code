a=100
b=233
print(a+b)
my_str='abcdefghijklmn'
print(my_str)

print('Following are example of slicing\n\n')

print(my_str[3]) # this will print character number 3 of string
print(my_str[:5]) # this will print upto 5th character of the string
print(my_str[4:]) # this will print 4th letter onwards of the string
print(my_str[2:9]) # this will print 2nd to 8th letter of the string
print(my_str[2:9:3]) #this will print every 3rd character between 2md and 9th character
print(my_str[::-1]) # this will print reverse of the string

# Following are string examples

str_1='noopur'
print(str_1[3:])
str_1='pur' + str_1[3:]
print(str_1)
print(str_1.split('r'))


# Formatiing string

a='afterlife'
b='seinfeld'
c='celiphate'
str_2='the shows I am watching are {} {} {}.'.format(a,b,c)
print('\n\n')
print(str_2)
print(f'other way of showinmg my series {a} {b} {c}') 
