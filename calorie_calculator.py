####################################################################
# Calorie Calculator.
# A simple calorie calculator script based off
# some of the common foods.
# By Doug Purcell
# Website: http://www.purcellconsult.com
#
# Calories in common foods was taken from
# this script: https://www.calculator.net/calorie-calculator.html
#
#
####################################################################

class FoodCalculator:
    """ The class that holds the data and methods for the common
    food."""
    calories = 0
    # kilojoules. Energy from food/drink
    kj = 0

    def fruit(self, fruit, fruit_serving_size=1):
        """ computes calories and kJ for fruit based off
        the serving size.
        Lists of fruits: apple, banana, grapes, orange, pear,
        peach, pineapple, strawberry, watermelon.
        """
        fruit = fruit.lower()
        if fruit == 'apple':
            apple_calories = 59
            apple_kj = 247
            self.calories = fruit_serving_size * apple_calories
            self.kj = apple_kj * fruit_serving_size
        elif fruit == 'orange':
            banana_calories = 151
            banana_kj = 632
            self.calories = fruit_serving_size * banana_calories
            self.kj = banana_kj * fruit_serving_size
        elif fruit == 'grapes':
            grapes_calories = 100
            grapes_kj = 419
            self.calories = fruit_serving_size * grapes_calories
            self.kj = grapes_kj * fruit_serving_size
        elif fruit == 'orange':
            orange_calories = 53
            orange_kj = 222
            self.calories = fruit_serving_size * orange_calories
            self.kj = orange_kj * fruit_serving_size
        elif fruit == 'pear':
            pear_calories = 82
            pear_kj = 343
            self.calories = fruit_serving_size * pear_calories
            self.kj = pear_kj * fruit_serving_size
        elif fruit == 'peach':
            peach_calories = 67
            peach_kj = 281
            self.calories = fruit_serving_size * peach_calories
            self.kj = peach_kj * fruit_serving_size
        elif fruit == 'pineapple':
            pineapple_calories = 82
            pineapple_kj = 343
            self.calories = fruit_serving_size * pineapple_calories
            self.kj = pineapple_kj * fruit_serving_size
        elif fruit == 'strawberry':
            strawberry_calories = 53
            strawberry_kj = 222
            self.calories = fruit_serving_size * strawberry_calories
            self.kj = strawberry_kj * fruit_serving_size
        elif fruit == 'watermelon':
            watermelon_calories = 50
            watermelon_kj = 209
            self.calories = fruit_serving_size * watermelon_calories
            self.kj = watermelon_kj * fruit_serving_size

    def vegetable(self, veggie, veggie_serving_size=1):
            """ computes calories and kJ for vegetables based off
            the serving size.
            Lists of veggies: asparagus, broccoli, carrots, cucumber,
            eggplant, lettuce, tomato.
            """
            veggie = veggie.lower()
            if veggie == 'asparagus':
                asp_calories = 27
                asp_kj = 113
                self.calories = veggie_serving_size * asp_calories
                self.kj = asp_kj * veggie_serving_size
            elif veggie == 'broccoli':
                broccoli_calories = 45
                broccoli_kj = 188
                self.calories = veggie_serving_size * broccoli_calories
                self.kj = broccoli_kj * veggie_serving_size
            elif veggie == 'carrots':
                carrot_calories = 50
                carrot_kj = 209
                self.calories = veggie_serving_size * carrot_calories
                self.kj = carrot_kj * veggie_serving_size
            elif veggie == 'cucumber':
                cucumber_calories = 17
                cucumber_kj = 71
                self.calories = veggie_serving_size * cucumber_calories
                self.kj = cucumber_kj * veggie_serving_size
            elif veggie == 'eggplant':
                eggplant_calories = 35
                eggplant_kj = 147
                self.calories = veggie_serving_size * eggplant_calories
                self.kj = eggplant_kj * veggie_serving_size
            elif veggie == 'lettuce':
                lettuce_calories = 5
                lettuce_kj = 21
                self.calories = veggie_serving_size * lettuce_calories
                self.kj = lettuce_kj * veggie_serving_size
            elif veggie == 'tomato':
                tomato_calories = 22
                tomato_kj = 92
                self.calories = veggie_serving_size * tomato_calories
                self.kj = tomato_kj * veggie_serving_size

    def proteins(self, proteins, protein_serving_size=1):
        """ computes calories and kJ for proteins based off
        the serving size.
        Lists of proteins: beef(cooked), chicken(cooked), tofu, egg,
        fish(catfish), pork(cooked), shrimp(cooked).
        """
        proteins = proteins.lower()
        if proteins == 'beef':
            beef_calories = 142
            beef_kj = 595
            self.calories = protein_serving_size * beef_calories
            self.kj = beef_kj * protein_serving_size
        elif proteins == 'chicken':
            chicken_calories = 136
            chicken_kj = 569
            self.calories = protein_serving_size * chicken_calories
            self.kj = chicken_kj * protein_serving_size
        elif proteins == 'tofu':
            tofu_calories = 86
            tofu_kj = 360
            self.calories = protein_serving_size * tofu_calories
            self.kj = tofu_kj * protein_serving_size
        elif proteins == 'egg':
            egg_calories = 78
            egg_kj = 327
            self.calories = protein_serving_size * egg_calories
            self.kj = egg_kj * protein_serving_size
        elif proteins == 'fish':
            fish_calories = 136
            fish_kj = 569
            self.calories = protein_serving_size * fish_calories
            self.kj = fish_kj * protein_serving_size
        elif proteins == 'pork':
            pork_calories = 137
            pork_kj = 574
            self.calories = protein_serving_size * pork_calories
            self.kj = pork_kj * protein_serving_size
        elif proteins == 'shrimp':
            shrimp_calories = 56
            shrimp_kj = 234
            self.calories = protein_serving_size * shrimp_calories
            self.kj = shrimp_kj * protein_serving_size

    def common_meals(self, common_meals, common_meals_serving_size=1):
        """ computes calories and kJ for common meals and snacks
            based off the serving size.
            Lists of meals/snacks: bread, butter, caesar salad, cheeseburger,
            hamburger, dark chocolate, corn, pizza, potato, rice, sandwich.
               """
        common_meals = common_meals.lower()
        if common_meals == 'bread':
            bread_calories = 75
            bread_kj = 314
            self.calories = common_meals_serving_size * bread_calories
            self.kj = bread_kj * common_meals_serving_size
        elif common_meals == 'butter':
            butter_calories = 102
            butter_kj = 427
            self.calories = common_meals_serving_size * butter_calories
            self.kj = butter_kj * common_meals_serving_size
        elif common_meals == 'caesar_salad':
            caesar_calories = 481
            caesar_kj = 2014
            self.calories = common_meals_serving_size * caesar_calories
            self.kj = caesar_kj * common_meals_serving_size
        elif common_meals == 'cheeseburger':
            cheeseburger_calories = 285
            cheeseburger_kj = 1193
            self.calories = common_meals_serving_size * cheeseburger_calories
            self.kj = cheeseburger_kj * common_meals_serving_size
        elif common_meals == 'hamburger':
            hamburger_calories = 250
            hamburger_kj = 1047
            self.calories = common_meals_serving_size * hamburger_calories
            self.kj = hamburger_kj * common_meals_serving_size
        elif common_meals == 'dark_chocolate':
            dark_chocolate = 155
            dark_chocolate_kj = 649
            self.calories = common_meals_serving_size * dark_chocolate
            self.kj = dark_chocolate_kj * common_meals_serving_size
        elif common_meals == 'corn':
            corn_calories = 132
            corn_kj = 553
            self.calories = common_meals_serving_size * corn_calories
            self.kj = corn_kj * common_meals_serving_size
        elif common_meals == 'pizza':
            pizza_calories = 285
            pizza_kj = 1193
            self.calories = common_meals_serving_size * pizza_calories
            self.kj = pizza_kj * common_meals_serving_size
        elif common_meals == 'potato':
            potato_calories = 130
            potato_kj = 544
            self.calories = common_meals_serving_size * potato_calories
            self.kj = potato_kj * common_meals_serving_size
        elif common_meals == 'rice':
            rice_calories = 206
            rice_kj = 862
            self.calories = common_meals_serving_size * rice_calories
            self.kj = rice_kj * common_meals_serving_size
        elif common_meals == 'sandwich':
            sandwich_calories = 200
            sandwich_kj = 837
            self.calories = common_meals_serving_size * sandwich_calories
            self.kj = sandwich_kj * common_meals_serving_size


    def beverages(self, beverages, beverages_serving_size=1):
        """ computes calories and kJ for beverages based off
        the serving size.
        Lists of beverages: beer, coca-cola, diet coke, milk 1%,
        milk %2, mike(whole), orange, apple cider, yogurt (low-fat),
        yogurt (non-fat).
        """
        beverages = beverages.lower()
        if beverages == 'beer':
            beer_calories = 154
            beer_kj = 645
            self.calories = beverages_serving_size * beer_calories
            self.kj = beer_kj * beverages_serving_size
        elif beverages == 'coca cola' or beverages == 'cola-cola':
            coca_cola_calories = 150
            coca_cola_kj = 628
            self.calories = beverages_serving_size * coca_cola_calories
            self.kj = coca_cola_kj * beverages_serving_size
        elif beverages == 'diet coke' or beverages == 'diet-coke':
            diet_coke_beverages = 0
            diet_coke_kj = 0
            self.calories = beverages_serving_size * diet_coke_beverages
            self.kj = diet_coke_kj * beverages_serving_size
        elif beverages == 'milk one percent' \
                or beverages == 'one percent milk':
            one_percent_milk = 102
            one_percent_milk_kj = 427
            self.calories = beverages_serving_size * one_percent_milk
            self.kj = one_percent_milk_kj * beverages_serving_size
        elif beverages == 'milk two percent' \
                or beverages == 'two percent milk':
            two_percent_milk = 122
            two_percent_milk_kj = 511
            self.calories = beverages_serving_size * two_percent_milk
            self.kj = two_percent_milk_kj * beverages_serving_size
        elif beverages == 'milk' \
                or beverages == 'whole milk':
            whole_milk = 146
            whole_milk_kj = 611
            self.calories = beverages_serving_size * whole_milk
            self.kj = whole_milk_kj * beverages_serving_size
        elif beverages == 'orange' \
                or beverages == 'orange juice':
            orange_juice = 111
            orange_juice_kj = 465
            self.calories = beverages_serving_size * orange_juice
            self.kj = orange_juice_kj * beverages_serving_size
        elif beverages == 'apple cider':
            apple_cider = 117
            apple_cider_kj = 490
            self.calories = beverages_serving_size * apple_cider
            self.kj = apple_cider_kj * beverages_serving_size
        elif beverages == 'yogurt low fat' \
                or beverages == 'non fat yogurt'\
                or beverages == 'non-fat-yogurt':
            low_fat_yogurt = 154
            low_fat_yogurt_kj = 645
            self.calories = beverages_serving_size * low_fat_yogurt
            self.kj = low_fat_yogurt_kj * beverages_serving_size
        elif beverages == 'nonfat yogurt' \
                or beverages == 'non-fat yogurt'\
                or beverages == 'non fat-yogurt':
            non_fat_yogurt = 110
            non_fat_yogurt_kj = 461
            self.calories = beverages_serving_size * non_fat_yogurt
            self.kj = non_fat_yogurt_kj * beverages_serving_size


if __name__ == '__main__':
    food = FoodCalculator()
    food.fruit('apple')
    print(food.calories)
    print(food.kj)
    meal = FoodCalculator()
    meal.common_meals('pizza')
    print(meal.calories)
    print(meal.kj)