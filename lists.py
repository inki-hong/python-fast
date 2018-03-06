fruits = ['apple', 'orange', 'banana']
print( fruits )

states = ['012345678', '123456780']
n = len( states )
print(n)

states.append('123405678')
print(states)

new_list = states  # aliasing
new_list.append('23456780')

print(new_list)
print(states)

print('-'*40)

third_list = states[:]  # list copy
third_list.append('345678012')
print(third_list)
print(states)

print('-'*40)

list_4 = states[0:2]  # copy but sublist
print(list_4)
print(states)

list_5 = states[-4:-2]  # copy but sublist
print(list_5)
print(states)

print('-'*40)

a_fruit = fruits[2]
last_fruit = fruits[-1]
print(fruits)
print(a_fruit)
print(last_fruit)

fruits[0] = 'peach'
print(fruits)

del fruits[0]
print(fruits)

print('-'*40)

fruits.append('apple')
fruits.append('mango')
fruits.append('kiwi')
print(fruits)

last_fruit = fruits[-1]
del fruits[-1]
print(fruits)
print(last_fruit)

last_fruit = fruits.pop()
print(last_fruit)

print('-'*40)
print(fruits)

fruits.insert(1, 'lemon')
print(fruits)

tf = 'apple' in fruits
print(tf)
tf = 'watermelon' in fruits
print(tf)

state = '123405678'
i = state.index('0')  # str thing
print(i)

i = fruits.index('banana')  # list thing
print(i)
