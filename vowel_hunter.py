################################################
# Counts the number of vowels in a string
# By Doug Purcell
# Owner of http://www.purcellconsult.com
#
##################################################

class Vowels:
    """" counts the number of vowels in a string """

    def __init__(self):
        self.text = input("Enter in some text: ")
        self.vowels = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0,
        'y': 0
    }

    def count_vowels(self):
        """ count the vowels """
        for x in self.text:
            for y in self.vowels:
                if x == y:
                    self.vowels[x] = self.vowels[x] + 1
        for vow, count in self.vowels.items():
            print('{0}:{1}'.format(vow, count))

v = Vowels()
v.count_vowels()