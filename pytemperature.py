#####################################################
# Temperature converter class in python:
# By Doug Purcell
#
# website: http://www.purcellconsult.com
#
# Includes methods for converting between
# Fahrenheit, Celsius, and Kelvin.
# F -> C = (F - 32) x 5/9
# F -> K = (F - 32)/1.8 + 273.15
# C -> F = (C x 9/5) + 32
# C -> K = C + 273.15
# K -> F = (K - 273.15) x 9/5 + 32
# K -> C = K - 273.15
#
######################################################


class Temperature:
    """ Includes methods for converting between
    Fahrenheit, Celsius, and Kelvin. """

    """ Fahrenheit is used as the official temperature
    only in the United States and it's unincorporated
    territories. Wiki page: https://en.wikipedia.org/wiki/Fahrenheit 
    """

    def fahrenheit_to_celsius(self, F):
        """ method for converting between
        fahrenheit and celsius.
        """
        C = (F - 32) * 5/9
        return C

    def fahrenheit_to_kelvin(self, F):
        """ converts from fahrenheit
            to kelvin.
        """
        K = (F - 32) / 1.8 + 273.15
        return K


    """ The Celsius scale is a temperature scale used
    by the International System of Units (SI).It's
    used by all countries except US, Bahamas, Belize,
    Cayman Islands, and Liberia. Wiki page:
    https://en.wikipedia.org/wiki/Celsius """

    def celsius_to_fahrenheit(self, C):
        """ accepts celsius argument
        and returns result in fahrenheit."""
        F = (C * 9/5) + 32
        return F

    def celsius_to_kelvin(self, C):
        K = C + 273.15
        return K

    """ Kelvin conversions. Kelvin is the
    primary unit of temperature measurement in
    the physical sciences. Learn more about Kelvin
    on wikipedia: https://en.wikipedia.org/wiki/Kelvin
    """
    def kelvin_to_fahrenheit(self, K):
        F = (K - 273.15) * 9/5 + 32
        return F

    def kelvin_to_celsius(self, K):
        C = K - 273.15
        return C

    """ A list of common temperatures. Can
    retrieve the temperatures in Fahrenheit,
    Celsius, or Kelvin. """

    def absolute_zero(self, temp):
        temp = temp.upper()
        if temp == 'F':
            return -459.67
        elif temp == 'C':
            return -273.15
        elif temp == 'K':
            return 0
        else:
            return None

    def boiling_point_nitrogen(self, temp):
        temp = temp.upper()
        if temp == "F":
            return -320.4
        elif temp == "C":
            return -195.8
        elif temp == 'K':
            return 77.4
        else:
            return None

    def sublimation_dry_ice(self, temp):
        temp = temp.upper()
        if temp == "F":
            return -108.4
        elif temp == "C":
            return -78
        elif temp == 'K':
            return 195.1
        else:
            return None

    def melting_point_ice(self, temp):
        temp = temp.upper()
        if temp == "F":
            return 31.9998
        elif temp == "C":
            return -0.0001
        elif temp == 'K':
            return 273.1499
        else:
            return None

    def water_triple_point(self, temp):
        temp = temp.upper()
        if temp == "F":
            return 32.018
        elif temp == "C":
            return 0.01
        elif temp == 'K':
            return 273.16
        else:
            return None

    def normal_body_temp(self, temp):
        temp = temp.upper()
        if temp == "F":
            return 98.6
        elif temp == "C":
            return 37.0
        elif temp == 'K':
            return 310.15
        else:
            return None

    def water_boiling_point(self, temp):
        """ at 1 atm. """
        temp = temp.upper()
        if temp == "F":
            return 211.971
        elif temp == "C":
            return 99.9839
        elif temp == 'K':
            return 373.1339
        else:
            return None




