"""
documentation
"""

name,age=('telang', 44)
age = str(age)
print('hello ' + input("What is your name?: "))
print(f'my data is {name} and {age}')
print(type(name))
print(name.capitalize())

'''
lists
'''

fruits = ['apples', 'oranges', 'grapes', 'pears']
fruits.insert(2, 'strawberries')
print(fruits[2])

'''
tuples & sets - 
tuples are ordered, cannot be changed.
sets is un-ordered and unindexed. 
'''
fruits1 = ('apples', 'oranges', 'grapes')
print(fruits1[2])

fruits2 = {'apples', 'oranges', 'grapes'}
fruits2.add('mango')
print('apples' in fruits2)
print(fruits2)

'''
dictionary
'''
person = {'firstName': 'Ninad', 'lastName': 'Telang', 'age': 44, 'phoneNumber': '555-555-5555'}
del(person['phoneNumber'])
person2 = person.copy()
print(person.get('phoneNumber'), type(person))

'''
list of dict
'''
people = [
    {'name': 'ninad telang', 'age': 44},
    {'name': 'thomas wales', 'age': 41}
]
print(people[1]['name'])

'''
functions
'''

def sayHello(name='Sam'):
    print(f'Hello function {name}')

def getSum(num1, num2):
    total = num1 + num2
    return total

getNewSum = lambda num1, num2 : num1 + num2

sayHello('Ninad Telang')
print(getSum(2,3))
print(getNewSum(2,5))

x = 7
y = 5

if x > y and x > 0:
    print('true')
else:
    print('false')

''' elif x==y: for else if'''
''' or for OR '''
''' if not(x ==y): '''

''' Membership operators '''

numbers = [1,3,5,6]
print(x in numbers)

''' not in '''

if x is y:
    print(x is y)

''' for loop '''
people = ['john', 'bob', 'sam']
for person in people: #range() is another option
    if person == 'sam':
        continue #break is another option
    print(f'current person: {person}')

count = 0
while count <= 10:
    print(f'Count: {count}')
    count +=1