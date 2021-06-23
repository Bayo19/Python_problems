# learning enumerate method - python

# for loop

values = ['a', 'b', 'c']

# for val in values:
#     print(val)

# index = 0
# for value in values:
#     print(index, value)
#     index += 1

# for index in range(len(values)):
#     value = values[index]
#     print(index, value)

#pythonic way
for count, value in enumerate(values, start=1):
    print(count, value)
    

# practicing enumerate 

names = ['jake', 'mary', 'tayo', 'felicity', 'xavier', 'zander', 'goldstein']

# def evens(array):
#     values = []
#     for index, item in enumerate(array):
#         if index % 2 == 0:
#             values.append(item)
#     return values

# print(evens(names))

# more pythonic version of the function above

def evens(array):
    # return [item for index, item in enumerate(array) if index % 2 == 0]
    return array[0::2]

print(evens(names))

seq = list(range(0,10))
# pythonic way to get index of particular intervals below is every second index, starting from 0
print(seq[0::2])