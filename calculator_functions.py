######################################################
# Emulates the individual functionality of a
# calculator in python. Has functions for addition,
# subtraction, multiplication, division, squaring,
# and power.
# By Doug Purcell
# website: http://www.purcellconsult.com
#
#######################################################


def subtract(*args):
    value = 0
    for x in args:
        value -= x
    return value


def add(*args):
    value = 0
    for x in args:
        value += x
    return value


def multiply(*args):
    value = 1
    for x in args:
        value *= x
    return value


def divide(*args):
    nums, values = [], None
    for x in args:
        nums.append(x)
    values = nums[0]
    for y in nums[1:]:
        values /= y
    return values


def squared(x):
    return x*x


def power(x, n):
    """ computes x raised to the power of n """
    count, value = 1, 1
    while count <= n:
        count += 1
        value *= x
    return value


# test the functions
if __name__ == '__main__':

    # expected -27
    s1 = subtract(1, 10, 16)

    # expected -3
    s2 = subtract(1, 1, 1)

    # expected -35

    s3 = subtract(5, 10, 20)

    print(s1)
    print(s2)
    print(s3)

    # expected 15
    a1 = add(1, 2, 3, 4, 5)

    # expected 1100
    a2 = add(100, 200, 300, 500)

    # expected 5412.1129200000005
    a3 = add(1.52, 38.282, .08292, 5372.228)

    print(a1)
    print(a2)
    print(a3)

    # expected 6
    m1 = multiply(1, 2, 3)

    # expected 1000
    m2 = multiply(10, 10, 10)

    # expected 791.96
    m3 = multiply(5, 10, 15.8392)

    print(m1)
    print(m2)
    print(m3)

    # 1.66
    d1 = divide(1, 2, 3)
    # .1
    d2 = divide(5, 5, 10)
    # 4.00
    d3 = divide(100, 5, 5)

    print(d1)
    print(d2)
    print(d3)

    # 100
    s1 = squared(10)
    # 1.643524
    s2 = squared(1.282)
    # 144
    s3 = squared(12)
    print(s1)
    print(s2)
    print(s3)

    # 1000
    p1 = power(10, 3)
    # 27
    p2 = power(3, 3)
    # 50625
    p3 = power(15, 4)

    print(p1)
    print(p2)
    print(p3)
