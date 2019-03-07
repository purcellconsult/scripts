####################################################
#
# Models the United States currency from the
# usa.gov website.
# https://www.usa.gov/currency#item-213446
# By Doug Purcell
# website: http://www.purcellconsult.com
#
#
#####################################################

def papermoney():
    cash = None
    one_dollar = int(input("How many one dollar bills? "))
    two_dollar = int(input("How many two dollar bills? "))
    five_dollar = int(input("How many five dollar bills? "))
    ten_dollar = int(input("How many ten dollar bills? "))
    twenty_dollar = int(input("How many twenty dollar bills? "))
    fifty_dollar = int(input("How many fifty dollar bills? "))
    hundred_dollar = int(input("How many one hundred dollar bills? "))
    cash = one_dollar * 1 + two_dollar * 2 + five_dollar * 5
    cash += ten_dollar * 10 + twenty_dollar * 20
    cash += fifty_dollar * 50 + hundred_dollar * 100
    print('${}'.format(cash))

def coins():
    coins = None
    penny = int(input("How many pennies? "))
    nickels = int(input("How many nickels? "))
    dimes = int(input("How many dimes? "))
    quarters = int(input("How many quarters? "))
    half_dollars = int(input("How many half dollars? "))
    dollar_coin = int(input("How many dollar coins? "))
    coins = penny * .01 + nickels * .05 + dimes * .1
    coins += quarters * .25 + half_dollars * .50
    coins += dollar_coin * 1.00
    if coins < 1.00:
        print('\u00A2{}'.format(round(coins, 2)))
    else:
        print('${}'.format(round(coins)))


if __name__ == '__main__':
    a = papermoney()
    b = coins()

