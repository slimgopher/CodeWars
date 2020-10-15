# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def spin_words(sentence):
    words = sentence.split()
    words = [i[::-1] if len(i) >= 5 else i for i in words]
    return (' '.join(words))


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


if __name__ == '__main__':
    spin_words('Welcome to the new World')
    descending_order(12345678908888888)
    test = [-9389797, -9026027, 6327831, 6373475, -5554271, -7435669, -8887181, 9384397, 3863837, -7883155, 481091, 5402303, -8287403, -6419639, 5597323, -7762075, 6251463, 9420991, 2688943, -9825699, 5142127, 6466529, -1171355, -9070572, -1566215, -6422497, -4654287, -3881211, 2088499, -1769659, -1099745, -6270655, 4831613, 9184077, 9213829, 1372509, -3635365, 2333827, -8365951, -1902437, 4842871, -1632977, 2094909, -6950575, 3610875, -4619445, -9347, 7152827]
    test1 = [-6809788, 6645684, -6226194, -9038856, 6797029, -77004, 2469356, 6210854, 9726686, 2989036, 9070486, -5178516, -1816962, 1400890, 6484552, 8125876, -3614350, -4208254, -6098586, 5232534, -8244586, -1775262, 8552310, -7197652, -5994004, 216222, 9892368, -8998126, 7793586, 5321590, -2299684, -1488850, 6681318, -1356860, -5169840, -9973626]
    find_outlier(test1)
    solution(10)

