####################################################
# True or False quiz script in python.
# Currently shows questions in a sequential fashion
# and computes stats at the end.
#
# Name: Doug Purcell
# Website: http://www.purcellconsult.com
#
#####################################################


class Quiz:
    """" quiz script written in python. """

    def questions(self):

        bank = [
            ['T', 'Guido van Rossum is the creator of python.'],
            ['T', 'A dictionary is a built in data type in python.'],
            ['T', 'Python is a scripting language.'],
            ['T',  "Python is an interpreted language. It can also be compiled."],
            ['T', 'The most popular implementation of python is cpython.'],
            ['F', 'Python is a strictly typed language.'],
            ['F', 'Python has no frameworks for web development.'],
            ['F', 'Python is built from C++.'],
            ['F', 'Python is not a popular language for machine learning.'],
            ['F', 'Python does not have a C variant.']
        ]
        return bank

if __name__ == '__main__':
        q = Quiz()
        b = q.questions()
        count, correct, wrong = 0, 0, 0
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        print('Start quiz...')
        for x in b:
            print('#{}.{}'.format(count, x[1]))
            your_input = input("Type 'T' for True or 'F' for False: ")
            your_input = your_input.upper()
            if your_input == x[0]:
                print('Correct!')
                correct += 1
                count += 1
            else:
                print('Wrong')
                count += 1
                wrong += 1
        print('----------')
        print('{} {} quiz summary:'.format(first_name, last_name))
        print("Your Score {}".format((correct/(count))*100))
        print("Correct: {}".format(correct))
        print("Wrong: {}".format(wrong))
        print("Questions asked: {}".format(count))
