####################################################
# A body mass index calculator:
# By Doug Purcell
# http://www.purcellconsult.com
# National Heart, Lung, and Blood
# Institute: https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm
# Body mass index is a measure of body fat based on
# height and weight that applies to adult men and
# women. Enter your weight/height using standard
# or metric measures.
#
#  BMI categories:
#  underweight = < 18.5
#  normal weight = 18.5 - 24.9
#  overweight = 25 - 29.9
#  obesity = BMI of 30 or greater
#
####################################################


def bmi_categories(bmi):
    if bmi < 18.5:
        result = 'underweight'
    elif bmi >= 18.5 and bmi <= 24.9:
        result = 'normal weight'
    elif bmi >= 25 and bmi <= 29.9:
        result = 'overweight'
    else:
        result = 'obesity'
    print(result)

####################################################
# Enter height and weight using standard measures
# formula using lbs/inches
# 703 x weight / height^2
#####################################################

def standard():
    result = None
    feet = int(input("enter height in feet "))
    inches = int(input("enter height in inches "))
    weight = float(input("enter weight in pounds "))
    height_to_inches = feet * 12
    height_to_inches += inches
    bmi = round(703 * weight / (height_to_inches ** 2), 2)
    print('BMI = {}'.format(bmi))
    bmi_categories(bmi)

###################################################
# Enter height and weight using metric measures
# weight -> kg
# height -> cm
# Formula: (weight/ height^2) * 10,000
###################################################


def metric():
    weight_kg = float(input("weight in kilograms "))
    height_in_cm = float(input("height in centimeters "))
    bmi_metric = round((weight_kg / (height_in_cm ** 2) * 10000), 2)
    print(bmi_metric)
    bmi_categories(bmi_metric)


if __name__ == '__main__':
    choice = input("""Type 's' for standard measurement (lbs/inches) \nor 'm' for metric: """)
    choice = choice.lower()
    if choice == 's':
        standard()
    elif choice == 'm':
        metric()
    else:
        print("Invalid input")
