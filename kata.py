# 1 remove first and last char from comma separated string
def arr(string):
    if len(string) == 0:
        return None
    if len(string.split(',')) <= 2:
        return None
    if len(string.split(',')) > 2:
        x = string.split(',')
        x = ' '.join(x[1: -1])
        return x
    

# print(arr('1'))
# print(arr('1, 3'))
# print(arr('1,2,3'))
# print(arr('1,2,3,4'))


# 2 always return 5
def unusual_five():
    return len(['one', 'two', 'three', 'four', 'five'])

# print(unusual_five())

# 3
def largest_pair_sum(numbers): 
    x = max(numbers)
    numbers.remove(x)
    y = max(numbers)
    return int(y) + int(x)

print(largest_pair_sum([10,14,2,23,19]))
print(largest_pair_sum([1,2,3,4,6,-1,2]))
print(largest_pair_sum([-100,-29,-24,-19,19]))

elements =  {"hydrogen": {"number": 1,
                          "weight": 1.00794,
                          "symbol": 'H'},
               "helium": {"number": 2,
                          "weight": 4.002602,
                          "symbol": "He"}, 
               "oxygen": {"number": 8, 
                          "weight": 15.999, 
                          "symbol": "O"}}
import pprint
print(pprint.pformat(elements))

xampdic = {'john': 'name', 'mary': 'nickname'}

x = xampdic.get('john')

print(x)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

for name in names:
    name = str(name).lower()
    name = name.split()
    name = '_'.join(name)
    usernames.append(name)
print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for i in range(len(tokens)):
    if tokens[i][0] == '<':
        count += 1
print(count)

items = ['first string', 'second string','third string']

html_str = '<ul>\n'

for i in range(len(items)):
    items[i] = f'<li>{items[i]}</li>\n'
    html_str += items[i]
html_str += '</ul>\n'

print(html_str)

print(list(range(0,-5)))



result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add the value (number of fruits) to result

result = 0
for k, v in basket_items.items():
    if k in fruits:
        result = result + v

print(result)
    

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for l,x,y,z in zip(labels, x_coord, y_coord, z_coord):
    points.append('{}: {}, {}, {}'.format(l, x, y, z))

for point in points:
    print(point)


data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
zipped = tuple(zip(*data))
print(zipped)


names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [x.split()[0] for x in names]
print(first_names)

man = {'john': {1: 'one', 2: 'two', 'three': 3}}
# print(man['john']['three'])

words = "if any or any or any"
pos = words.find('any')
print(pos, 'any??')

x = 3
if (x > 2):
    x = x * 2;
if (x > 4):
    x = 0;
print(x)

# matrix - transposing

list_of_list = [[1,2,3], [4,5,6], [7,8,9]]
xz = [[1,2], [5,6], [8,9]]
iop = [[3,4,5], [8,9,10]]


# for i in range(len(list_of_list)):
#     for j in range(len(list_of_list[0])):
#         result[i][j] = list_of_list[j][i]

def transpose_matrix(nested_list):
    result = [[0 for _ in range(len(nested_list))] for _ in range (len(nested_list[0]))]
    for i in range(len(nested_list)):
        for j in range(len(nested_list[0])):
            result[j][i] = nested_list[i][j]
    return result

print(transpose_matrix(list_of_list))
print(transpose_matrix(xz))
print(transpose_matrix(iop))

# add numbers and return as binary in string
def add_binary(a,b):
    x = a + b
    x = list(str(bin(x)))
    return ''.join(x[2:])

print(add_binary(5,9))


ary2 = [1,2,3,4,3,2,1]

def find_even_index(arr):

    for i in range(0, len(arr)):
        left= sum(arr[: i])
        # print('left',left)
        right= sum(arr[i+1:])
        # print('right', right)
        if right == left:
            return i
    return -1

print('start')
print(find_even_index(ary2))


midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

f_g = [max(grades) for grades in zip(midterms, finals)]
f_g = dict(zip(students, f_g))
print(f_g)

def interleave(x, y):
    x = list(zip(list(x), list(y)))
    x = [''.join(list(i)) for i in x]
    x = ''.join(x)
    print(x)
interleave('hi', 'ha')
interleave('aaa', 'zzz')