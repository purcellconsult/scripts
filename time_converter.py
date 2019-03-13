##############################################################
# Time converter script written in python.
# By Doug Purcell
# http://www.purcellconsult.com
#
# units the script worked with:
# nanosecond, microsecond, millisecond, second,
# minute, hour, day, week, work weeks, month, year, decade,
# century.
#
##############################################################

class Time:
    """a script that converts various time units and also includes some
    additional methods for modeling them. The inputs to be read are
    as follow:
    nanosecond -> nano
    microsecond -> micro
    millisecond -> milli
    second -> sec
    minute -> min
    hour -> h
    day -> d
    week -> w
    work week -> ww
    month -> m
    year -> y
    decade  -> dec
    century -> cen
    """


    def to_nanoseconds(self, units, magnitude):
        """ converts from various
        time units to nanoseconds. """
        time_units = units.lower()
        if time_units == 'micro':
            number = magnitude * 1000
            return '{} {}'.format(number, 'nano')
        elif time_units == 'milli':
            number = magnitude * 10e6
            return '{} {}'.format(number, 'nano')
        elif time_units == 'sec':
            number = magnitude * 1e9
            return '{} {}'.format(number, 'nano')
        elif time_units == 'min':
            number = magnitude * 6e10
            return '{} {}'.format(number, 'nano')
        elif time_units == 'h':
            number = magnitude * 3.6e12
            return '{} {}'.format(number, 'nano')
        elif time_units == 'd':
            number = magnitude * 8.64e13
            return '{} {}'.format(number, 'nano')
        elif time_units == 'w':
            number = magnitude * 6.048e14
            return '{} {}'.format(number, 'nano')
        elif time_units == 'ww':
            number = magnitude * 1.44e14
            return '{} {}'.format(number, 'nano')
        elif time_units == 'm':
            number = magnitude * 2.628e15
            return '{} {}'.format(number, 'nano')
        elif time_units == 'y':
            number = magnitude * 3.154e16
            return '{} {}'.format(number, 'nano')
        elif time_units == 'dec':
            number = magnitude * 3.154e17
            return '{} {}'.format(number, 'nano')
        elif time_units == 'cen':
            number = magnitude * 3.154e18
            return '{} {}'.format(number, 'nano')

    def to_microseconds(self, units, magnitude):
        """ converts from various
        time units to nanoseconds. """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 0.001
            return '{} {}'.format(number, 'micro')
        elif time_units == 'milli':
            number = magnitude * 1000
            return '{} {}'.format(number, 'micro')
        elif time_units == 'sec':
            number = magnitude * 1e6
            return '{} {}'.format(number, 'micro')
        elif time_units == 'min':
            number = magnitude * 6e7
            return '{} {}'.format(number, 'micro')
        elif time_units == 'h':
            number = magnitude * 3.6e9
            return '{} {}'.format(number, 'micro')
        elif time_units == 'd':
            number = magnitude * 8.64e10
            return '{} {}'.format(number, 'micro')
        elif time_units == 'w':
            number = magnitude * 6.048e11
            return '{} {}'.format(number, 'micro')
        elif time_units == 'ww':
            number = magnitude * 1.44e11
            return '{} {}'.format(number, 'nano')
        elif time_units == 'm':
            number = magnitude * 2.628e12
            return '{} {}'.format(number, 'micro')
        elif time_units == 'y':
            number = magnitude * 3.154e13
            return '{} {}'.format(number, 'micro')
        elif time_units == 'dec':
            number = magnitude * 3.154e14
            return '{} {}'.format(number, 'micro')
        elif time_units == 'cen':
            number = magnitude * 3.154e15
            return '{} {}'.format(number, 'micro')

    def to_milliseconds(self, units, magnitude):
        """ converts from various
        time units to milliseconds. """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 1e-6
            return '{} {}'.format(number, 'milli')
        elif time_units == 'micro':
            number = magnitude * .001
            return '{} {}'.format(number, 'milli')
        elif time_units == 'sec':
            number = magnitude * 1000
            return '{} {}'.format(number, 'milli')
        elif time_units == 'min':
            number = magnitude * 60000
            return '{} {}'.format(number, 'milli')
        elif time_units == 'h':
            number = magnitude * 3.6e6
            return '{} {}'.format(number, 'milli')
        elif time_units == 'd':
            number = magnitude * 8.64e7
            return '{} {}'.format(number, 'milli')
        elif time_units == 'w':
            number = magnitude * 6.048e8
            return '{} {}'.format(number, 'milli')
        elif time_units == 'ww':
            number = magnitude * 1.44e8
            return '{} {}'.format(number, 'milli')
        elif time_units == 'm':
            number = magnitude * 2.628e9
            return '{} {}'.format(number, 'milli')
        elif time_units == 'y':
            number = magnitude * 3.154e10
            return '{} {}'.format(number, 'milli')
        elif time_units == 'dec':
            number = magnitude * 3.154e11
            return '{} {}'.format(number, 'milli')
        elif time_units == 'cen':
            number = magnitude * 3.154e12
            return '{} {}'.format(number, 'milli')

    def to_seconds(self, units, magnitude):
        """ converts from various
        time units to seconds. """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 1e-9
            return '{} {}'.format(number, 'sec')
        elif time_units == 'micro':
            number = magnitude * 1e-6
            return '{} {}'.format(number, 'sec')
        # could also divide by 1000
        elif time_units == 'milli':
            number = magnitude * .001
            return '{} {}'.format(number, 'sec')
        elif time_units == 'min':
            number = magnitude * 60
            return '{} {}'.format(number, 'sec')
        elif time_units == 'h':
            number = magnitude * 3600
            return '{} {}'.format(number, 'sec')
        elif time_units == 'd':
            number = magnitude * 86400
            return '{} {}'.format(number, 'sec')
        elif time_units == 'w':
            number = magnitude * 604800
            return '{} {}'.format(number, 'sec')
        elif time_units == 'ww':
            number = magnitude * 144000
            return '{} {}'.format(number, 'sec')
        elif time_units == 'm':
            number = magnitude * 2.628e6
            return '{} {}'.format(number, 'sec')
        elif time_units == 'y':
            number = magnitude * 3.154e7
            return '{} {}'.format(number, 'sec')
        elif time_units == 'dec':
            number = magnitude * 3.154e8
            return '{} {}'.format(number, 'sec')
        elif time_units == 'cen':
            number = magnitude * 3.154e9
            return '{} {}'.format(number, 'sec')

    def to_minutes(self, units, magnitude):
        """ converts from various
        time units to minutes. """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 1.66667e-11
            return '{} {}'.format(number, 'min')
        elif time_units == 'micro':
            number = magnitude * 1.66667e-8
            return '{} {}'.format(number, 'min')
        elif time_units == 'milli':
            number = magnitude * 1.6667e-5
            return '{} {}'.format(number, 'min')
        elif time_units == 'sec':
            number = magnitude * 0.0166667
            return '{} {}'.format(number, 'min')
        elif time_units == 'h':
            number = magnitude * 60
            return '{} {}'.format(number, 'min')
        elif time_units == 'd':
            number = magnitude * 1440
            return '{} {}'.format(number, 'min')
        elif time_units == 'w':
            number = magnitude * 10080
            return '{} {}'.format(number, 'min')
        elif time_units == 'ww':
            number = magnitude * 2400
            return '{} {}'.format(number, 'min')
        elif time_units == 'm':
            number = magnitude * 43800
            return '{} {}'.format(number, 'min')
        elif time_units == 'y':
            number = magnitude * 525600
            return '{} {}'.format(number, 'min')
        elif time_units == 'dec':
            number = magnitude * 5.256e+6
            return '{} {}'.format(number, 'min')
        elif time_units == 'cen':
            number = magnitude * 5.256e+7
            return '{} {}'.format(number, 'min')

    def to_hours(self, units, magnitude):
        """ converts from various
        time units to hours. """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 2.77778e-13
            return '{} {}'.format(number, 'h')
        elif time_units == 'micro':
            number = magnitude * 2.77778e-10
            return '{} {}'.format(number, 'h')
        elif time_units == 'milli':
            number = magnitude * 2.77778e-7
            return '{} {}'.format(number, 'h')
        elif time_units == 'sec':
            number = magnitude * 0.000277778
            return '{} {}'.format(number, 'h')
        elif time_units == 'min':
            number = magnitude * 0.0166667
            return '{} {}'.format(number, 'h')
        elif time_units == 'd':
            number = magnitude * 24
            return '{} {}'.format(number, 'h')
        elif time_units == 'w':
            number = magnitude * 168
            return '{} {}'.format(number, 'h')
        elif time_units == 'ww':
            number = magnitude * 40
            return '{} {}'.format(number, 'h')
        elif time_units == 'm':
            number = magnitude * 730.001
            return '{} {}'.format(number, 'h')
        elif time_units == 'y':
            number = magnitude * 8760
            return '{} {}'.format(number, 'h')
        elif time_units == 'dec':
            number = magnitude * 87600
            return '{} {}'.format(number, 'h')
        elif time_units == 'cen':
            number = magnitude * 876000
            return '{} {}'.format(number, 'h')

    def to_days(self, units, magnitude):
        """ converts from various
        time units to days. """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 1.15741e-14
            return '{} {}'.format(number, 'd')
        elif time_units == 'micro':
            number = magnitude * 1.15741e-11
            return '{} {}'.format(number, 'd')
        elif time_units == 'milli':
            number = magnitude * 1.15741e-8
            return '{} {}'.format(number, 'd')
        elif time_units == 'sec':
            number = magnitude * 1.15741e-5
            return '{} {}'.format(number, 'd')
        elif time_units == 'min':
            number = magnitude * 0.000694444
            return '{} {}'.format(number, 'd')
        elif time_units == 'h':
            number = magnitude * 0.0416667
            return '{} {}'.format(number, 'd')
        elif time_units == 'w':
            number = magnitude * 7
            return '{} {}'.format(number, 'd')
        elif time_units == 'ww':
            number = magnitude * 1.66667
            return '{} {}'.format(number, 'd')
        elif time_units == 'm':
            number = magnitude * 30.4167
            return '{} {}'.format(number, 'd')
        elif time_units == 'y':
            number = magnitude * 365
            return '{} {}'.format(number, 'd')
        elif time_units == 'dec':
            number = magnitude * 3650
            return '{} {}'.format(number, 'd')
        elif time_units == 'cen':
            number = magnitude * 36500
            return '{} {}'.format(number, 'd')

    def to_weeks(self, units, magnitude):
        """ converts from various
        time units to weeks. """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 1.65344e-15
            return '{} {}'.format(number, 'w')
        elif time_units == 'micro':
            number = magnitude * 1.65344e-12
            return '{} {}'.format(number, 'w')
        elif time_units == 'milli':
            number = magnitude * 1.65344e-9
            return '{} {}'.format(number, 'w')
        elif time_units == 'sec':
            number = magnitude * 1.65344e-6
            return '{} {}'.format(number, 'w')
        elif time_units == 'min':
            number = magnitude * 9.92063e-5
            return '{} {}'.format(number, 'w')
        elif time_units == 'h':
            number = magnitude * 0.00595238
            return '{} {}'.format(number, 'w')
        elif time_units == 'd':
            number = magnitude * 0.142857
            return '{} {}'.format(number, 'w')
        elif time_units == 'ww':
            number = magnitude * 0.238095
            return '{} {}'.format(number, 'w')
        elif time_units == 'm':
            number = magnitude * 4.34524
            return '{} {}'.format(number, 'w')
        elif time_units == 'y':
            number = magnitude * 52.1429
            return '{} {}'.format(number, 'w')
        elif time_units == 'dec':
            number = magnitude * 521.429
            return '{} {}'.format(number, 'w')
        elif time_units == 'cen':
            number = magnitude * 5214.29
            return '{} {}'.format(number, 'w')

    def to_work_weeks(self, units, magnitude):
        """ converts from various
        time units to work weeks.  A work week in the US is generally
        around 40 hours per week. """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 1.44e+14
            return '{} {}'.format(number, 'ww')
        elif time_units == 'micro':
            number = magnitude * 1.44e+11
            return '{} {}'.format(number, 'ww')
        elif time_units == 'milli':
            number = magnitude * 1.44e+8
            return '{} {}'.format(number, 'ww')
        elif time_units == 'sec':
            number = magnitude * 144000
            return '{} {}'.format(number, 'ww')
        elif time_units == 'min':
            number = magnitude * 2400
            return '{} {}'.format(number, 'ww')
        elif time_units == 'h':
            number = magnitude * 0.025
            return '{} {}'.format(number, 'ww')
        elif time_units == 'd':
            number = magnitude * 1.66667
            return '{} {}'.format(number, 'ww')
        elif time_units == 'w':
            number = magnitude * 0.238095
            return '{} {}'.format(number, 'ww')
        elif time_units == 'm':
            number = magnitude * 0.0547945
            return '{} {}'.format(number, 'ww')
        elif time_units == 'y':
            number = magnitude * 0.00456621
            return '{} {}'.format(number, 'ww')
        elif time_units == 'dec':
            number = magnitude * 0.000456621
            return '{} {}'.format(number, 'ww')
        elif time_units == 'cen':
            number = magnitude * 4.5662e-5
            return '{} {}'.format(number, 'ww')

    def to_months(self, units, magnitude):
        """ converts from various
        time units to months.
        """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 3.80517e-16
            return '{} {}'.format(number, 'm')
        elif time_units == 'micro':
            number = magnitude * 3.80517e-13
            return '{} {}'.format(number, 'm')
        elif time_units == 'milli':
            number = magnitude * 3.80517e-10
            return '{} {}'.format(number, 'm')
        elif time_units == 'sec':
            number = magnitude * 3.80517e-7
            return '{} {}'.format(number, 'm')
        elif time_units == 'min':
            number = magnitude * 2.2831e-5
            return '{} {}'.format(number, 'm')
        elif time_units == 'h':
            number = magnitude * 0.00136986
            return '{} {}'.format(number, 'm')
        elif time_units == 'd':
            number = magnitude * 0.0328767
            return '{} {}'.format(number, 'm')
        elif time_units == 'w':
            number = magnitude * 0.230137
            return '{} {}'.format(number, 'm')
        elif time_units == 'ww':
            number = magnitude * 0.0547945
            return '{} {}'.format(number, 'm')
        elif time_units == 'y':
            number = magnitude * 12
            return '{} {}'.format(number, 'm')
        elif time_units == 'dec':
            number = magnitude * 120
            return '{} {}'.format(number, 'm')
        elif time_units == 'cen':
            number = magnitude * 1200
            return '{} {}'.format(number, 'm')

    def to_year(self, units, magnitude):
        """ converts from various
        time units to years.
        """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 3.17098e-17
            return '{} {}'.format(number, 'y')
        elif time_units == 'micro':
            number = magnitude * 3.17098e-14
            return '{} {}'.format(number, 'y')
        elif time_units == 'milli':
            number = magnitude * 3.17098e-11
            return '{} {}'.format(number, 'y')
        elif time_units == 'sec':
            number = magnitude * 3.17098e-8
            return '{} {}'.format(number, 'y')
        elif time_units == 'min':
            number = magnitude * 1.90259e-6
            return '{} {}'.format(number, 'y')
        elif time_units == 'h':
            number = magnitude * 0.000114155
            return '{} {}'.format(number, 'y')
        elif time_units == 'd':
            number = magnitude * 365
            return '{} {}'.format(number, 'y')
        elif time_units == 'w':
            number = magnitude * 52.1429
            return '{} {}'.format(number, 'y')
        elif time_units == 'ww':
            number = magnitude * 0.00456621
            return '{} {}'.format(number, 'y')
        elif time_units == 'm':
            number = magnitude * 0.08333341
            return '{} {}'.format(number, 'y')
        elif time_units == 'dec':
            number = magnitude * 0.1
            return '{} {}'.format(number, 'y')
        elif time_units == 'cen':
            number = magnitude * 0.01
            return '{} {}'.format(number, 'y')

    def to_decade(self, units, magnitude):
        """ converts from various
        time units to decade.
        """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 3.17098e-18
            return '{} {}'.format(number, 'cen')
        elif time_units == 'micro':
            number = magnitude * 3.17098e-16
            return '{} {}'.format(number, 'dec')
        elif time_units == 'milli':
            number = magnitude * 3.17098e-13
            return '{} {}'.format(number, 'dec')
        elif time_units == 'sec':
            number = magnitude * 3.17098e-10
            return '{} {}'.format(number, 'dec')
        elif time_units == 'min':
            number = magnitude * 1.90259e-8
            return '{} {}'.format(number, 'dec')
        elif time_units == 'h':
            number = magnitude * 1.14155e-5
            return '{} {}'.format(number, 'dec')
        elif time_units == 'd':
            number = magnitude * 0.000273973
            return '{} {}'.format(number, 'dec')
        elif time_units == 'w':
            number = magnitude * 0.00191781
            return '{} {}'.format(number, 'dec')
        elif time_units == 'ww':
            number = magnitude * 0.000456621
            return '{} {}'.format(number, 'dec')
        elif time_units == 'm':
            number = magnitude * 0.00833334
            return '{} {}'.format(number, 'dec')
        elif time_units == 'y':
            number = magnitude * 0.1
            return '{} {}'.format(number, 'dec')
        elif time_units == 'cen':
            number = magnitude * 10
            return '{} {}'.format(number, 'dec')


    def to_century(self, units, magnitude):
        """ converts from various
        time units to century.
        """
        time_units = units.lower()
        if time_units == 'nano':
            number = magnitude * 3.17098e-19
            return '{} {}'.format(number, 'cen')
        elif time_units == 'micro':
            number = magnitude * 3.17098e-16
            return '{} {}'.format(number, 'cen')
        elif time_units == 'milli':
            number = magnitude * 3.17098e-13
            return '{} {}'.format(number, 'cen')
        elif time_units == 'sec':
            number = magnitude * 3.17098e-10
            return '{} {}'.format(number, 'cen')
        elif time_units == 'min':
            number = magnitude * 1.90259e-8
            return '{} {}'.format(number, 'cen')
        elif time_units == 'h':
            number = magnitude * 1.14155e-6
            return '{} {}'.format(number, 'cen')
        elif time_units == 'd':
            number = magnitude * 2.73973e-5
            return '{} {}'.format(number, 'cen')
        elif time_units == 'w':
            number = magnitude * 0.000191781
            return '{} {}'.format(number, 'cen')
        elif time_units == 'ww':
            number = magnitude * 4.5662e-5
            return '{} {}'.format(number, 'cen')
        elif time_units == 'y':
            number = magnitude * 0.01
            return '{} {}'.format(number, 'cen')
        elif time_units == 'm':
            number = magnitude * 0.000833334
            return '{} {}'.format(number, 'cen')
        elif time_units == 'dec':
            number = magnitude * 0.1
            return '{} {}'.format(number, 'cen')


if __name__ == '__main__':

    t = Time()
    nano = t.to_nanoseconds('w', 4)
    micro = t.to_microseconds('h', 5)
    century = t.to_century('m', 10)
    print(micro)
    print(century)