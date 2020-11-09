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
    summa = sum(int(i) ** len(str(value)) for i in str(value))
    return summa == value


def namelist(names):
    if len(names) > 1:
        return ', '.join(names[i]['name'] for i in range(len(names) - 1)) + f' & {names[-1]["name"]}'
    elif len(names) == 1:
        return names[0]['name']
    return


def bouncing_ball(h, bounce, window):
    res = 1
    while h > window:
        res += 1
        h *= bounce
    return res


def find_missing_letter(chars):
    res = (ord(chars[i]) + 1 for i in range(len(chars) - 1) if ord(chars[i]) + 1 < ord(chars[i + 1]))
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
            res += chr(ord(i) + 13)
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
    print(a, b)
    return a if arr.count(a) == 1 else b

    # return max(arr) if arr.count(max(arr)) == 1 else min(arr)


def ascii_code(string):
    return ord(string)


def rgb(r, g, b):
    res = [r, g, b]
    for i in range(len(res)):
        if res[i] < 0:
            res[i] = f'0{hex(0)[2:]}'
        elif res[i] > 255:
            res[i] = hex(255)[2:]
        elif res[i] < 16:
            res[i] = f'0{hex(res[i])[2:]}'
        else:
            res[i] = hex(res[i])[2:]

    return ''.join(i.upper() for i in res)


from math import prod


def format_duration(x):
    if x > 0:

        names = ['years', 'days', 'hours', 'minutes', 'seconds']
        datas = []
        ls = [1, 60, 60, 24, 365]
        for i in range(len(names) - 1):
            datas.append((x % prod(ls[:i + 2])) // prod(ls[:i + 1]))
        datas.append(x // prod(ls))
        datas = list(reversed(datas))

        res = ', '.join([f'{datas[i]} {names[i]}' if datas[i] > 1 else f'{datas[i]} {names[i][:-1]}'
                         for i in range(len(datas)) if datas[i] != 0])
        if res.rfind(',') > 0:
            return res[:(res.rfind(','))] + ' and' + res[(res.rfind(',') + 1):]
        return res
    return 'now'


""" Shortest Knight Path """


def onboard_check(*args):
    print('onboard_check')
    for i in args:
        if i not in range(8):
            return False
    return True


def parse(string):
    print('parse(string)')
    hor = int(chr(ord(string[0]) - 49))
    vert = int(string[1]) - 1

    if not onboard_check(hor, vert):
        raise ValueError('wrong input: coords are out of chessboard')
    return hor, vert


def next_move(chessboard: list, pos, count):
    print('next_move')
    coord = [-1, 1, -2, 2]

    for i in coord:
        for j in coord:
            if abs(j) != abs(i) and onboard_check(pos[0] + i, pos[1] + j):
                if chessboard[pos[0] + i][pos[1] + j] == 0:
                    chessboard[pos[0] + i][pos[1] + j] = count
                if chessboard[pos[0] + i][pos[1] + j] == 'end':
                    return count

def knight(start, end):
    print('knight')
    start = parse(start)
    end = parse(end)
    chessboard = [[0 for i in range(8)] for j in range(8)]
    chessboard[end[0]][end[1]] = 'end'

    move = 1
    in_one_move = next_move(chessboard, start, move)

    while in_one_move is None:
        move += 1
        for i in range(len(chessboard)):
            for j in range(len(chessboard[i])):
                if chessboard[i][j] == move - 1:
                    ans = next_move(chessboard, (i, j), move)
                    if ans is not None:
                        return ans
    return in_one_move


if __name__ == '__main__':
    print('start')
    knight('a1', 'h7')
    print('end')