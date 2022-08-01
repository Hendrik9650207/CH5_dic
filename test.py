def square_sum(num):
    sum1 = 0
    for i in num:
        sum1 = sum1 + i ** 2
    return sum1


def square_sum2(numbers):
    return sum(x ** 2 for x in numbers)


print(square_sum([1, 2]))
print(square_sum([0, 3, 4, 5]))
print()


print(square_sum2([1, 2, 3, 4]))

a = str(input("Enter an integer:"))

print(type(a))
for i in a:
    print(i)


dic2 = {'True': 'Yes', 'False': 'No'}
b = str(input("Enter the boolean:"))
try:
    print(dic2[b])
except KeyError:
    print('enter the boolean!')


