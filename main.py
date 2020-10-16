
def spin_words(sentence):
    words = sentence.split()
    words = [i[::-1] if len(i) >= 5 else i for i in words]
    return ' '.join(words)

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

def add_binary(a, b):
    return bin(a + b).replace('0b', '')

def find_outlier(integers: list):
    check = sum([int(bin(i)[-1]) for i in integers[:3]])
    for i in integers:
        if check > 1:
            if i % 2 == 0:
                return i
        elif i % 2 != 0:
            return i

def bin_row(row):
    for i in range(row):
        print('even' if i % 2 == 0 else '', i, bin(i)[-1])

def solution(n):

    return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)

def narcissistic(value):

    summa = sum(int(i )**len(str(value)) for i in str(value))
    return summa == value

def namelist(names):

    if len(names) > 1:
        return ', '.join(names[i]['name'] for i in range(len(names ) -1)) + f' & {names[-1]["name"]}'
    elif len(names) == 1:
        return names[0]['name']
    return

def bouncing_ball(h , bounce, window):
    res = 1
    while h > window:
        res += 1
        h *= bounce
    return res

def find_missing_letter(chars):

    res = (ord(chars[i] ) +1 for i in range(len(chars ) -1) if ord(chars[i] ) + 1 <ord(chars[ i +1]))
    return chr(res.__next__())


def valid_parentheses1(string):

    res = [i for i in string if i in ('(', ')')]
    while len(res) != 0:
        if res[-1] == ')':
            if res[0] != ')':
                res.pop()
                res.reverse()
                res.remove('(')
                res.reverse()
            else:
                return False
        else:
            return False
    return True

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(':
            cnt += 1
        if char == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return True if cnt == 0 else False

def rot13(message):
    res = ''
    for i in message:
        if ord(i) in range(65, 78) or ord(i) in range(97, 110):
            res += chr(ord(i)+13)
        elif ord(i) in range(78, 91) or ord(i) in range(110, 123):
            res += chr(ord(i) - 13)
        else:
            res += i
    return res

def duplicate_encode(word):

    word = ''.join(')' if word.lower().count(i) > 1 else '(' for i in word.lower())
    return word

def find_uniq1(arr):
    # your code here
    return max(arr) if arr.count(max(arr)) == 1 else min(arr)

def find_uniq(arr):
    a, b = set(arr)
    print(a,b)
    return a if arr.count(a) == 1 else b

    #return max(arr) if arr.count(max(arr)) == 1 else min(arr)


def ascii_code(string):
    return ord(string)


if __name__ == '__main__':


    string = 'z'


    print(find_uniq([ 0, 0, 0.55, 0, 0 ]))