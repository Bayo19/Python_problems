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


# Highest word Score

# helper function
def to_num(char):
    return ord(char) - 96

def high(x):
    
    st_nums = [list(word) for word in x.split(' ')]
    res_1 = []
    for i in st_nums:
        res_1.append({'word': ''.join(i), 'number': sum([to_num(z) for z in i ])})
    
    res_2 = max(res_1, key=lambda n: n['number'])
    return res_2['word']

# Which are in?

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

def in_array(array1, array2):
    inner = []
    for i in array1:
        for j in array2:
            if i in j:
                inner.append(i)
    inner_dic = {}
    for i in inner:
        if i in inner_dic:
            continue
        else:
            inner_dic[i] = 1
    res = [k for k, v in inner_dic.items()]
    res.sort()
    return res
            


print(in_array(a1, a2))


# First non-repeating character

def first_non_repeating_letter(string):
    if string == '': return ''

    dick = {}

    for i in string.lower():
        if i in dick:
            dick[i] += 1
        else:
            dick[i] = 1
    
    res = [k for k,v in dick.items() if v == 1]

    if len(res) == 0:
        return ''

    if res[0] in string:
        return res[0]
    else: return res[0].upper()


print(first_non_repeating_letter('sTreSS'))

ltest = [ {'name': 'Bart'}, {'name': 'Jack'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
# Format a string of names like 'Bart, Lisa & Maggie'
def namelist(names):
    if len(names) == 0: return ''

    name_str = []

    for i in names:
        for k, v in i.items():
            name_str.append(v)
    if len(name_str) == 1:
        return ''.join(name_str)
    if len(name_str) == 2:
        return ' & '.join(name_str)
    else:
        x = ', '.join(name_str[: -2])
        y = ' & '.join(name_str[-2:])
        return f'{x}, {y}'



print(namelist(ltest))

# Turn String Input into Hash

ting = "a=1, b=2, c=3, d=4"

def str_to_hash(st):
    if st == '': return {}
    one = st.split(', ')
    two = [x.split('=') for x in one]
    three = [[i[0], int(i[1])] for i in two]
    dick = {}
    for i in three:
        dick[i[0]] = i[1]
    return dick

print(str_to_hash(ting))

# Encrypt this
def encrypt_this(text):
    if text == '': return ''
    one = list(text)
    two = []
    three = ''
    four = ''
    five = ''
    six = []
    for i in range(len(one)):
        if i == 0:
            two.append(ord(one[i]))
        elif i == 1:
            three += one[i]
        elif i == len(one) - 1:
            five += one[i]
        else:
            four += one[i]
    if ' ' in text:
        temp = text.split(' ')
        for i in temp:
            six.append(encrypt_this(i))
        res2 = ' '.join(six)
        return res2
    res = f'{two[0]}{five}{four}{three}'
    return res


print(encrypt_this('Thank you Piotr for all your help'))
# print(encrypt_this('good'))
# print(encrypt_this('hello world'))

# Permute a Palindrome

def permute_a_palindrome (input_s): 
    input_s = input_s.replace(' ', '').lower()
    
    d = dict()

    for i in input_s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd = 0

    for k, v in d.items():
        if v % 2 != 0 and odd == 0:
            odd += 1
        elif v % 2 != 0 and odd > 0:
            return False
    return True

print(permute_a_palindrome('too t'))
print(permute_a_palindrome('madam'))
print(permute_a_palindrome('adamm'))
print(permute_a_palindrome('junk'))


# Valid Credit Card Number

def validate(n):

    even = []
    even2 = []
    odd = []
    odd2 = []
    if len(str(n)) % 2 == 0:
        even += list(str(n))
        even = [int(i) for i in even]
        for i in range(len(even)):
            if (i + 1) % 2 != 0:
                even2.append(even[i]*2)
            else:
                even2.append(even[i])
        for i in range(len(even2)):
            if even2[i] > 9:
                even2[i] -=9
        return sum(even2) % 10 == 0
    else:
        odd += list(str(n))
        odd = [int(i) for i in odd]
        for i in range(len(odd)):
            if (i+1) % 2 == 0:
                odd2.append(odd[i]*2)
            else:
                odd2.append(odd[i])

        for i in range(len(odd2)):
            if odd2[i] > 9:
                odd2[i] -=9
        return sum(odd2) % 10 == 0
            

            
print('\n'*5)
print(validate(123))
print(validate(1))
print(validate(2121))
print(validate(1230))


# 5kyu - Scramblies

def scramble(s1, s2):

    s3 = ''
    if len(s1) == len(s2) and ''.join(sorted(s1)) != ''.join(sorted(s2)):
        return False
        
    for i in s2:
        if i in s1:
            s3 +=i
    if s3 == s2: return True
    return False
            
    
# print('\n'*10)
print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))


# Extract domain name from a URL 5kyu

def domain_name(url):
    res = ''
    if '://' not in url:
        x = url.split('.')
        if x[0] == 'www':
            res += x[1]
            return res
        else:
            res += x[0]
            return res

    x = url.split('://')
    x = x[1:]
    x = ''.join(x)
    x = x.split('.')

    if x[0] == 'www':
        res+=x[1]
    else: res+=x[0]
    return res

print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print(domain_name("www.xakep.ru"))
print(domain_name("icann.org"))
print(domain_name("uc9g02k.de/error"))

