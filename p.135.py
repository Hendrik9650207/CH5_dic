# dic method
spam = {'color': 'red', 'ingredient': 'pork', 'age': 42}

# values()
for v in spam.values():
    print(v)

print()
# keys()
for u in spam.keys():
    print(u)

print()
# items()
for i in spam.items():
    print(i)
print()

# dic to list
dic1 = {'color': 'red', 'age': 25}
for k, v in spam.items():
    print('Key: ' + k + ' Value ' + str(v))

# in, not in :Test key value exist in dic or not and return boolean value
print('name' in dic1.keys())
print('color' in dic1.keys())
print()

# get method in dic
picnicItems = {'apple': 5, 'cups': 2}
print(picnicItems.get('apple', 0))
print(picnicItems.get('cups', 0))
print(picnicItems.get('anchovy', 0))


# new item in dic
dic3 = {'name': 'Joe', 'age': 25}
print()
dic3['color'] = 'black'
print(dic3)
print()


# setdefault method in dic (another way to new item in dic)
dic4 = {'name': 'Pooka', 'age': 5}
print(dic4, '\n')
dic4.setdefault('color', 'black')
print(dic4)
print(dic4['name'])
print()
dic4.setdefault('name', 'John')  # 如果dic中已有key值，則dic中value不會有變化
print(dic4)
print()


# Count character number in string
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    print(count)
print(count)
print()
