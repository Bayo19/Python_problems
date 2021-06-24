# starting again

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

# Consonant value - 6kyu
# len(ss) > 1 and
def solve(s):
    d = {}
    for i in range(1, 27):
        d[chr(i + 96)] = i
    
    ss = ''

    # removing vowels and separating consonant substrings
    # with a comma
    for i in s:
        if i not in 'aeiou':
            ss+= i
        else:
            if len(ss):
                if ss[-1] != ',':
                    ss += ','
            else:
                continue
    # split the string and put each substring into own array            
    x = ss.split(',')
    x  = [list(i) for i in x]
    
    # change each char in nested array into number
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = d[x[i][j]]

    from functools import reduce
    
    # initialize an empty array
    app = []
    
    # reduce each sub array in x and append to app array
    for i in range(len(x)):
        if x[i] != []:
            f = reduce((lambda a,b: a + b), x[i])
            app.append(f)
    
    # return the largest number in app array
    return max(app)

print(solve("zodiac"))
print(solve("chruschtschov"))
print(solve("khrushchev"))
print(solve("strength"))
print(solve("catchphrase"))
print(solve("twelfthstreet"))
print(solve("mischtschenkoana"))


# +1 Array

def up_array(arr):

    if arr == []: return None
    for i in arr:
        if i < 0 or i >= 10:
            return None

    arr_s = [str(x) for x in arr]
    if arr_s == None: return None
    else:
        arr_s =  list(str(int(''.join(arr_s))+1))
        arr_s_res = [int(x) for x in arr_s]
        print(arr_s_res)

        return arr_s_res


print(up_array([2,3,9]))
print(up_array([4,3,2,5]))
print(up_array([1,-9]))
print(up_array([]))

# Decipher this
import re

def decipher_this(string):
    res = string.split(' ')
    r = [re.split(r'(\d+)', s) for s in res]
    r = [x[1:] for x in r ]
    for i in r:
        i[0] = chr(int(i[0]))
        i[1] = list(i[1])
        i[1][-1], i[1][0] = i[1][0], i[1][-1]
        
    r = ' '.join([i[0]+ ''.join(i[1]) for i in r])
    return r
    
    

print(decipher_this('72olle 103doo 100ya'))
print(decipher_this('82yade 115te 103o'))



def whatday(num):
    d = {
1: 'Sunday',
2: 'Monday',
3: 'Tuesday',
4: 'Wednesday',
5: 'Thursday',
6: 'Friday',
7: 'Saturday'
}

    return d[num]



# string repeat

def repeat_str(repeat, string):
    arr = []
    for i in range(0, repeat):
        arr.append(string)
    return ''.join(arr)


#

def remove_exclamation_marks(s):
   return s.replace('!', '')


print(remove_exclamation_marks('Hello!!!'))

#

def reverse_words(s):
    ss =  s.split(' ')
    return ' '.join(list(reversed(ss)))

print(reverse_words('The greatest victory is that which requires no battle'))


# The Vowel Code

def encode(st):
    v = 'aeiou'
    d = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    l_st = list(st)
    for i in range(len(l_st)):
        if l_st[i] not in v:
            continue
        else:
            l_st[i] = str(d[l_st[i]])
    return ''.join(l_st)


def decode(st):
    n = '12345'
    d = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    l_st = list(st)
    for i in range(len(l_st)):
        if l_st[i] not in n:
            continue
        else:
            l_st[i] = d[l_st[i]]
    return ''.join(l_st)
    

print(encode('hello'))
print(encode('How are you today?'))
print(encode('This is an encoding test.'))
print(decode('h2ll4'))


def is_divisible(n,x,y):
    x = str(n/x).split('.')
    y = str(n/y).split('.')
    if x[1] == '0' and y[1] == '0':
        return True
    return False


print(is_divisible(12, 3, 4))

# Counting Duplicates

def duplicate_count(text):
    # Your code goes here
    if text == '': return 0

    d = {}
    for i in text.lower():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    res = [k for k, v in d.items() if v > 1]
    return len(res)
     

print(duplicate_count(""))
print(duplicate_count("abcde"))
print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))

# Word to binary

def word_to_bin(word):
    # code away!!!
    w = [bin(ord(i)) for i in list(word)]
    return [i.replace('b', '') for i in w]
    
print(word_to_bin('man'))


# rev seq

def reverse_seq(n):
    res = []
    for i in reversed(range(1,n+1)):
        res.append(i)
    return res
        
print(reverse_seq(6))

# Mexican Wave - 6kyu
# skip over spaces
def wave(people):
    r = []
    for i in range(len(people)):
        r.append(list(people))
    
    for i in range(len(r)):
        for j in range(len(r[i])):
            if j == i:
                r[i][j] = r[i][j].upper()
   
    res = [''.join(i) for i in r if ''.join(i) != people]
    return res

print(wave('hello'))
print(wave('two words'))

# Kebabize - Camel case to kebab case 6kyu
def kebabize(string):
    n = '1 2 3 4 5 6 7 8 9 0'
    s = ''
    r = ''
    for i in string:
        if i not in n:
            s += i
        else:
            continue
    for i in s:
        if i == i.lower():
            r += i
        else:
            r += '-'
            r +=  i.lower()
    if len(r) < 1:
        return ''
    elif r[0] == '-':
        return r[1:]
    return r


print(kebabize('camelsHaveThreeHumps'))
print(kebabize('camelsHave3Humps'))
print(kebabize('42'))
print(kebabize('SOS'))


# dashatize it 6kyu

def dashatize(n):
    if type(n) != int:
        return ''
    n_s_l = list(str(n))
    s = ''
    for i in n_s_l:
        if int(i) % 2 == 0:
            s += i
        else:
            if len(s) > 1 and s[-1] == '-':
                s += i
                s+= '-'
            else:
                s += '-'
                s += i
                s+= '-'
    if s[0] == '-' and s[-1] == '-':
        return s[1:-1]
    elif s[-1] == '-':
        return s[:-1]
    elif s[0] == '-':
        return s[1:]

    return s

print(dashatize(274))
print(dashatize(6815))
print(dashatize(5311))
print(dashatize(86320))
print(dashatize(974302))


# Multiplication Tables

def multiplication_table(row,col):
    r = []
    for i in range(row):
        r.append([])
    for i in range(len(r)):
        for j in range(col):
            r[i].append((i+1)*(j+1))
    return r
            
                

print(multiplication_table(2,2))
print(multiplication_table(3,3))
print(multiplication_table(3,4))
print(multiplication_table(4,4))
print(multiplication_table(2,5))

# Count letters in a string

def letter_count(s):
    #your code here
    d = {}
    for i in s:
        if i == i.lower():
            if i in d:
                d[i] += 1
            else:
                d[i] =  1
        else:
            continue
    return d


print(letter_count('codewars'))
<<<<<<< HEAD


# Sort the odd

def sort_array(source_array):
    odds = []
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            odds.append(source_array[i])
            source_array[i] = 'x'

    sorted_odds = sorted(odds)
    
    while len(sorted_odds):
        for i in range(len(source_array)):
            if source_array[i] == 'x':
                source_array[i] = sorted_odds.pop(0)  
            else: continue

    return source_array


print(sort_array([7, 1]))
print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


# PYTHON SCREENING TASK

def is_palindrome(text):
  if len(text) <=1: return True

  text = list(text)
  temp_text = list(text)

  def rev(text):
      for l in range(len(text) // 2):
          r = len(text) - 1 - l
          text[l], text[r] = text[r], text[l]
      return text

  return temp_text == rev(text)
print(is_palindrome('redivider'))
print(is_palindrome('drive'))
print(is_palindrome('kayak'))
print(is_palindrome('11211'))
print(is_palindrome('1115544'))

def find_occurrences(text, itemsList):
    text_list = []
    count = 0
    for i in text:
        text_list.append(i.split())
    
    for i in text_list:
        for j in range(len(i)):
            if itemsList in i[j]:
                count += 1
    return count


print(find_occurrences(["welcome to our Python program", "Python is my favorite language!", "I am afraid of Pythons", "I love Python"], "Python"))

print(find_occurrences(["this is the best day", "Python is the best language for learning programming", "I am learning", "I love learning"], "learning"))

print(find_occurrences(["welcome", "language", "I am", "I love"], "Python"))

print(find_occurrences(["What are you doing?", "you like programming?", "We are students", "We are learners"], "are"))

print(find_occurrences(["welcome welcome", "wikipedia", "wonderland", "we"], "w"))


# replace module 2 function with lambda expression
def is_a_lambda(v):
  LAMBDA = lambda:0
  return isinstance(v, type(LAMBDA)) and v.__name__ == LAMBDA.__name__


def module_2(num):
  return num % 2


m2 = lambda num : num % 2

task_count = 5

def increase_task_count(task_count):
    task_count += 1
    return task_count

print(increase_task_count(task_count))

# try and catch zerodivisionerror

def divide(divisor, dividend):
    try:
        dividend / divisor
    except ZeroDivisionError:
        print('Divison by zero not allowed')


print(divide(0, 10))

# Sum of pairs
# Giacomo Sorbi solution

def sum_pairs(ints, s):
    seen = []
    for item in ints:
        if s-item in seen: return [s-item, item]
        if item not in seen: seen += [item]
    return None    
print(sum_pairs([11,3,7,5], 10))
print(sum_pairs([4,3,2,3,4], 6))
print(sum_pairs([0,0,-2,3], 2))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))

# Reverse inside parentheses
# not correct yet
def reverse_in_parentheses(string):
    r = string[string.find('(')+1:string.rfind(')')]
    res = ''
    if '(' in r and ')' in r:
        return None  
    else:
        return string.replace(r, ''.join(list(reversed(r))))
    

print(reverse_in_parentheses("h(el)lo"))
print(reverse_in_parentheses('h((el)l)o'))
print(reverse_in_parentheses("a ((d e) c b)"))
print(reverse_in_parentheses("one (two (three) four)"))
print(reverse_in_parentheses("one (ruof ((rht)ee) owt)") )

# memoization practice and dynamic programming

def fib(n, prevValues = {}):
    if n in prevValues:
        return prevValues[n]
    
    if n <= 2:
        result = 1
    else:
        result = fib(n -1, prevValues) + fib(n -2, prevValues)
    prevValues[n] = result
    return result

print(fib(11))

# bottom up approach

def bottom_up_fib(n):
    if n <= 2: return 1
    bottom_up = [None] * (n+1)
    
    bottom_up[1] = 1
    bottom_up[2] = 1
    # print(bottom_up)
    
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        # print(bottom_up)
    return bottom_up[n]
    
print(bottom_up_fib(10))


# Multiplation table for number - 8kyu 
def multi_table(number):
    res = ''
    for i in range(1, 11):
        if i != 10:
            res += f'{i} * {number} = {i * number}\n'
        elif i == 10:
            res += f'{i} * {number} = {i * number}'
    return res

print(multi_table(5))

# Twice as old - 8kyu

def twice_as_old(dad_years_old, son_years_old):
    twice_son = son_years_old * 2
    if dad_years_old > twice_son:
        return dad_years_old - twice_son
    elif twice_son == dad_years_old:
        return 0
    else:
        return twice_son - dad_years_old

print(twice_as_old(36, 7))

#
arr = arr = ['a', 'b', 'c', 'd', 'e']
def first(seq, n = 1): 
    return seq[0:n]

print(first(arr))
print(first(arr, 2))
print(first(arr, 3))
print(first(arr, 0))

# Character with longest consecutive repetition -6kyu

def longest_repetition(chars):
    if chars == '': return (', 0')
    if len(chars) == 2 and chars[0] != chars[1]:
        return (chars[0], 1)
    char = ''
    max = 0
    num = 1
    for i in range(1,len(chars)):
        if chars[i] == chars[i-1]:
            num += 1
            if num > max:
                max = num
                char = chars[i]
        elif chars[i] != chars[i-1]:
            num = 1
    return (char, max)
        

print(longest_repetition('aaaabb'))
print(longest_repetition("bbbaaabaaaa"))
print(longest_repetition("cbdeuuu900"))
print(longest_repetition("abbbbb"))
print(longest_repetition("aabb"))
print(longest_repetition("ba"))
print(longest_repetition(""))


# Remove duplicate words

w = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

def remove_duplicate_words(s):
    ret = ''
    
    l_s = s.split(' ')
    for i in l_s:
        if i not in ret:
            ret += i
            ret+=' '
    return ret[:-1]

print(remove_duplicate_words(w))

# Sum two arrays

def sum_arrays(array1, array2):
    
    if len(array1) > 1 and array1[0] == 0:
        while array1[0] == 0:
            array1 = array1[1:]
    if len(array2) > 1 and array2[0] == 0:
        while array2[0] == 0:
            array2 = array2[1:]
            
    if len(array1) < 1 and len(array2) < 1:
        return []
    elif len(array1) < 1 and len(array2) >= 1:
        return array2
    elif len(array2) < 1 and len(array1) >= 1:
        return array1
    
    def to_string(arr):
        for i in range(len(arr)):
            arr[i] = str(arr[i])
        return arr
    
    st_1, st_2 = ''.join(to_string(array1)), ''.join(to_string(array2))
    
    one, two = int(st_1), int(st_2)
    sum = list(str(one + two))
    
    if sum[0] == '-':
        sum[1] = str(int(sum[1]) - (int(sum[1])*2))
        sum = sum[1:]
        
    result =  [int(i) for i in sum]
    
    return result
    
    
    
  
print(sum_arrays([], []))  
print(sum_arrays([3,2,9], [1,2]))
print(sum_arrays([4,7,3],[1,2,3]))
print(sum_arrays([1],[5,7,6]))
print(sum_arrays([3,2,6,6],[-7,2,2,8]))
print(sum_arrays([4,0,7,2,2], []))
print(sum_arrays([-4, 5, 7, 3, 6], [5, 3, 4, 5]))
print(sum_arrays([], [9]))
print(sum_arrays([4], []))
print(sum_arrays([], [0, 2, 6, 3]))
print(sum_arrays([0,0,7,2,0], []))

=======
>>>>>>> 4d8cb77bb1a6bb78ce1f5d050a80aee62d054bfd
