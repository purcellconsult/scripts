######################################################
# A program that models popular statistic
# functions in python. Re-writes some of the
# methods in the statistics module:
# https://docs.python.org/3/library/statistics.html
#
# Also, adds some new ones.
#
# author: Doug Purcell
# owner: http://www.purcellconsult.com
# a bunch of stat goodies: http://onlinestatbook.com/2/
# social science calculators: https://www.socscistatistics.
# com/tests/
#
#######################################################

import math


class Stats:
    """ A simple class for modeling stats using
    python """

    def __init__(self):
        self.count = 0
        self.sum = 0
        self.nums = []

    def enter_nums(self, *input):
        """ reads in numbers to be
        used as the dataset."""
        for x in input:
            self.nums.append(x)
            self.count += 1
        return self.nums

    def sort(self):
        """ helper method """
        return sorted(self.nums)

    def compute_count(self):
        return self.count

    def summation(self):
        for x in self.nums:
            self.sum += x
        return self.sum

    def mean(self):
        return round(self.sum / self.count, 3)

    def harmonic_mean(self, harmonic=0):
        """ computes harmonic mean"""
        for x in self.nums:
            harmonic += 1/x
        return len(self.nums)/harmonic


    def minimum(self):
        return self.sort()[0]

    def maximum(self):
        return self.sort()[-1]

    def median(self):
        """ sorts list then returns the value at
        it's middle index. """
        s = self.sort()
        return s[math.ceil(len(s)/2)-1]

    def sum_of_squares(self):
        """ partitioning sums of squares
        see how it woks: http://onlinestatbook.com
        /2/regression/partitioning.html
        """
        m = self.mean()
        sigma = 0
        for x in self.nums:
            sigma += (x - m) ** 2
        return round(sigma, 3)

    def sample_standard_deviation(self):
        """ determines variation of a set of data
        youtube vid explains: https://www.youtube.com/
        watch?v=09kiX3p5Vek
        """
        sigma = self.sum_of_squares()
        return math.sqrt(sigma/(len(nums)-1))

    def standard_variance(self):
        """ just the standard deviation
        squared. """
        sigma = self.sum_of_squares()
        return sigma / (len(nums) - 1)

    def standard_error_mean(self):
        """ sigma/ sqrt(N) """
        return self.sample_standard_deviation()/math.sqrt(len(self.nums))



if __name__ == '__main__':
    s = Stats()
    nums = s.enter_nums(3,4,4,5,6,8)
    print(nums)
    print(s.compute_count())
    print(s.summation())
    print(s.mean())
    print(s.sort())
    print(s.minimum())
    print(s.maximum())
    print(s.median())
    print(s.sum_of_squares())
    print(s.sample_standard_deviation())
    print(s.standard_variance())
    print(s.standard_error_mean())
    print(s.harmonic_mean())
