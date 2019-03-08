##################################################
# A random quote generator
# Includes some of my favorite quotes curated
# from various sources online.
# Doesn't parse any info, or use any databases
# Instead uses a dictionary to store the strings.
#
# By Doug Purcell
# Website: http://www.purcellconsult.com
#
##################################################


import random

class RandomQuote:
    """ random quotes in python"""
    quotes = {
        '"Albert Einstein"': "A person who never made a mistake never tried anything new.",
        '"WARREN BUFFETT"': "BE FEARFUL WHEN OTHERS ARE GREEDY, AND BE GREEDY WHEN OTHERS ARE FEARFUL",
        '"Malcolm McLaren (1946-2010)"': "BETTER A SPECTACULAR FAILURE, THAN A BENIGN SUCCESS",
        '"JOHN QUINCY ADAMS (1767-1848)"': "EVERY PROBLEM IS AN OPPORTUNITY IN DISGUISE",
        '"Peter O\'Toole (1932-2013)"': "I DO NOT CHOOSE TO BE A COMMON MAN ... IT IS MY RIGHT TO BE UNCOMMON — IF I CAN ... I SEEK OPPORTUNITY — NOT SECURITY ... \nI WANT TO TAKE THE CALCULATED RISK; TO DREAM AND TO BUILD, TO FAIL AND TO SUCCEED ... TO REFUSE TO BARTER INCENTIVE\nFOR A DOLE ... I PREFER THE CHALLENGES OF LIFE TO THE GUARANTEED EXISTENCE, THE THRILL OF FULFILLMENT TO THE STALE\nCALM OF UTOPIAS ...",
        '"Stephen Hawking"': "Intelligence is the ability to adapt to change.",
        '"Richard P. Feynman"': "I got a fancy reputation. During high school, every puzzle that was known to man must have come to me. Every damn, crazy conundrum that people had invented, I knew.",
        '"YVES SAINT LAURENT"': "I WISH I HAD INVENTED BLUE JEANS. THEY HAVE SEX APPEAL & SIMPLICITY - ALL I HOPE FOR IN MY CLOTHES - French fashion",
        '"STEVE JOBS (1955-2011)"': "STAY HUNGRY, STAY FOOLISH.",
        '"BARACK OBAMA (1961-)"' : "YES, WE CAN! ",
        '"Bryan Tracy"': "Successful people are just those with successful habits",
        '"Winston Churchill"': "Success is the ability to go from failure to failure without losing your enthusiasm.",
        '"Mark Cuban"': "It doesn’t matter how many times you fail. You only have to be right once and then everyone can tell you that you are an overnight success.",
        '"Mark Twain"': "All you need in this life is ignorance and confidence, and then success is sure.",
        '"Albert Ellis"': "The best years of your life are the ones in which you decide your problems are your own. You do not blame them on your\n mother, the ecology, or the president. You realize that you control your own destiny.",
        '"Herman Cain"': "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be\n successful.",
        '"Hellen Keller"': "Life is either a daring adventure or nothing.",
        '"Heraclitus"': "There is nothing permanent except change.",
        '"Indira Gandhi"': "You cannot shake hands with a clenched fist.",
        '"Amelia Earhart"': "The most difficult thing is the decision to act, the rest is merely tenacity. The fears are paper tigers. You can do anything you decide to do. You can act to change and control your life; and the procedure, the process is its own reward.",
        '"Henry James"': "Do not mind anything that anyone tells you about anyone else. Judge everyone and everything for yourself.",
        '"Leonardo da Vinci"': "Learning never exhausts the mind.",
        '"Thomas Carlyle"': "Permanence, perseverance and persistence in spite of all obstacles, discouragements, and impossibilities:\nIt is this, that in all things distinguishes the strong soul from the weak.",
        '"Susan B. Anthony"': "Independence is happiness.",
        '"Sun Tzu"': "The supreme art of war is to subdue the enemy without fighting.",
        '"John Galsworthy"': "Love has no age, no limit; and no death.",
        '"Aldous Huxley"': "There is only one corner of the universe you can be certain of improving, and that's your own self.",
        '"Thomas Jefferson"': "Honesty is the first chapter in the book of wisdom.",
        '"Jesus Christ"': "A new command I give you: Love one another. As I have loved you, so you must love one another.",
        '"Voltaire"': "God gave us the gift of life; it is up to us to give ourselves the gift of living well.",
        '"Simone de Beauvoir"': "Change your life today. Don't gamble on the future, act now, without delay.",
        '"J. R. R. Tolkien"': "Not all those who wander are lost.",
        '"Benjamin Franklin"': "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
        '"Buddha"': "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
        '"Robert Louis Stevenson"': "Don't judge each day by the harvest you reap but by the seeds that you plant.",
        '"Maya Angelou"': "Try to be a rainbow in someone's cloud.",
        '"Aristotle"': "It is during our darkest moments that we must focus to see the light.",
        '"Helen Keller"': "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart."
    }


r = RandomQuote()
quote = random.choice(list(r.quotes.items()))

def quote_length(self, size=100):
    """ returns only quotes that are greater
    than 100 characters by default. You can modify
    the default size to fit your preference. """
    quotes = []
    for x in r.quotes.values():
        if len(x) >= size:
            quotes.append(x)
        else:
            continue
    for y in quotes:
        print(y)


def get_random_quote(self):
    print(quote[1])
    print(quote[0])


if __name__ == '__main__':
    r = RandomQuote()
    get_random_quote(r)
    quote_length(r)




