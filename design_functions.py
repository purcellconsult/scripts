""" learn how write your own functions tutorial in python """


def compute_sum(*args):
    """ a replacement function to the builtin sum()
    function in the python api """
    sum = 0
    for x in args:
        sum += x
    return sum


print('a output:')
a1 = compute_sum(1, 2, 5)
a2 = compute_sum(1, 2, 3, 4, 5, 6, 7, 8)
a3 = compute_sum(1.282, 98, 68.29, 0.0292, .172, 87.928, 2772.228)

print(a1)
print(a2)
print(a3,'\n')


def compute_abs(args):
    """ computes the absolute value of any number """
    if args < 0:
        args *= -1
        return args
    else:
        return args


print('b output:')
b1 = compute_abs(-10)
b2 = compute_abs(100)
b3 = compute_abs(-7.282)
b4 = compute_abs(.292020202)
b5 = compute_abs(-.029202029)

print(b1)
print(b2)
print(b3)
print(b4)
print(b5, '\n')


def compute_min(*args):
    """ find the smallest number entered """
    " min has to be iterable, can't be an int"
    min = args[0]
    for x in args:
        if x < min:
            min = x
    return min


print('c output:')
c1 = compute_min(0, 5, 2, 9)
c2 = compute_min(10, 20, 50, 100)
c3 = compute_min(5, 10, 100)
c4 = compute_min(.20302, 1.292029, .292002, .00000289292)
c5 = compute_min(.00292020, 67.28282, 928, 16, 93922)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5, '\n')


def compute_max(*args):
    """ find the maximum number"""
    max = args[0]
    for x in args:
        if x > max:
            max = x
    return max


print('d output:')
d1 = compute_max(0, 5, 2, 9)
d2 = compute_max(10, 20, 50, 100)
d3 = compute_max(5, 10, 100)
d4 = compute_max(.20302, 1.292029, .292002, .00000289292)
d5 = compute_max(.00292020, 67.28282, 928, 16, 93922)
print(d1)
print(d2)
print(d3)
print(d4)
print(d5, '\n')


def is_float(args):
    """ determines if a num is a float """
    convert = str(args)
    for x in convert:
        if x == '.':
            return True
    else:
        return False


e1 = is_float(822.292)
e2 = is_float(10)
e3 = is_float(10.0)
e4 = is_float(3678292922188277827287.0)
e5 = is_float(.020229910202202)

print('e output:')
print(e1)
print(e2)
print(e3)
print(e4)
print(e5, '\n')


def is_int(args):
    """ determines if the number entered is an int """
    convert = str(args)
    for x in convert:
        if x == '.':
            return False
    return True


f1 = is_int(10.0)
f2 = is_int(10)
f3 = is_int(.38292)
f4 = is_int(327.2)
f5 = is_int(1000000000.1)
print()

print('f output:')
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)
print()


def compute_round(args):
    """ rounds a given number: emulates round() """
    convert, rounded_num, count = [], [], 0
    whole = 0
    num_to_string = str(args)
    for x in num_to_string:
        convert.append(x)
    if len(convert) == 3 and int(convert[2]) > 5:
        return 1.0
    elif len(convert) == 3 and int(convert[2]) < 5:
        return 0.0
    if len(convert) > 3:
        rounded_num = num_to_string.split('.')
        a, b = ''.join(rounded_num[0]), ''.join(rounded_num[1])
        if int(b[0]) >= 5:
            a = int(a)
            return a + 1.0
        else:
            a = int(a)
        return a + 0.0


print('g output:')
g1 = compute_round(0.4)
g2 = compute_round(1.23)
g3 = compute_round(.3392020)
g4 = compute_round(19.2882)
g5 = compute_round(159.28)
g6 = compute_round(159.58)
g7 = compute_round(-.3922)
g8 = compute_round(3232.3802832902)

print(g1)
print(g2)
print(g3)
print(g4)
print(g5)
print(g6)
print(g7)
print(g8)


def encrypt(args, key = 3):
    """ enter a letter/character pair to encrypt it """
    test = args

    mappings = (
        ('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6),
        ('g', 7), ('h', 8), ('i', 9), ('j', 10), ('k', 11), ('l', 12),
        ('m', 13), ('n', 14), ('o', 15), ('p', 16), ('q', 17), ('r', 18),
        ('s', 19), ('t', 20), ('u', 21), ('v', 22), ('w', 23), ('x', 24),
        ('y', 25), ('z', 26))

    for letter, num in mappings:
        if letter == test:
            num = (num + key - 1) % 26
            encrypted = mappings[num]
            return encrypted[0]


print('h values:')
h1 = encrypt('a')
h2 = encrypt('f', key=5)
h3 = encrypt('z', key=17)
h4 = encrypt('b', key=100)

print(h1)
print(h2)
print(h3)
print(h4)

