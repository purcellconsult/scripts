##############################################
# Food Energy Converter:
# Converts between calories and other common food
# energy units:
# By Doug Purcell
# http://www.purcellconsult.com
#
# 1 kilocalorie (kcal) to 1000 calorie (cal)
# 1 kilocalorie (kcal) to 4.184 Kilojoules (kJ)
# 1 kilocalorie (kcal) to 4184 joules (J)
#
# 1 calorie (cal) to 0.001 kilocalorie (kcal)
# 1 calorie (cal) to 0.004184 kilojoules (kj)
# 1 calorie (cal) to 4.184 joules (J)
#
# 1 Kilojoules (kj) to 0.239 (kcal)
# 1 Kilojoules (kj) to 239.0057 calorie (cal)
# 1 Kilojoules (kj) to 1000 joules (J)
#
################################################


def kilocalorie_conversions(amount, unit):
    """ converts kilocalorie to various energy units.
    units equals:
    cal -> calorie
    kj -> kilojoules
    j -> joules """
    unit = unit.lower()
    if unit == 'cal':
        conversion = amount * 1000
        return '{} {}'.format(conversion, 'cal')
    elif unit == 'kj':
        conversion = amount * 4.184
        return '{} {}'.format(conversion, 'kj')
    elif unit == 'j':
        conversion = amount * 4184
        return '{} {}'.format(conversion, 'J')


def calorie_conversions(amount, unit):
    """ converts calorie to various food energy units.
    cal -> calorie
    kj -> kilojoules
    j -> joules
    """
    unit = unit.lower()
    if unit == 'kcal':
        conversion = amount * 0.001
        return '{} {}'.format(conversion, 'kcal')
    elif unit == 'kj':
        conversion = amount * 0.004184
        return '{} {}'.format(conversion, 'kj')
    elif unit == 'j':
        conversion = amount * 4.184
        return '{} {}'.format(conversion, 'J')


def kilojoules_conversions(amount, unit):
    """ converts kilojoules to various food energy units.
    cal -> calorie
    kj -> kilojoules
    j -> joules
    """
    unit = unit.lower()
    if unit == 'kcal':
        conversion = amount * 0.239
        return '{} {}'.format(conversion, 'kcal')
    elif unit == 'cal':
        conversion = amount * 239.0057
        return '{} {}'.format(conversion, 'cal')
    elif unit == 'j':
        conversion = amount * 1000
        return '{} {}'.format(conversion, 'J')


if __name__ == '__main__':
    print(kilocalorie_conversions(10, 'CAL'))
    print(calorie_conversions(20, 'kj'))
    print(kilojoules_conversions(54.2, 'cal'))
