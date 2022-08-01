birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    else:
        print('I do not have birthday')
        print('birthday')
        bDay = input()
        birthdays[name] = bDay
        print('birthday db updated')
