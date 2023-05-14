from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredient_count = int(f.readline())
        dish = []
        for i in range(ingredient_count):
            book = f.readline()
            ing, count, unit = book.strip().split(' | ')
            dishes = {
                'ingredient_name': ing, 'quantity': count, 'measure': unit
            }
            dish.append(dishes)
        f.readline()
        cook_book[dish_name] = dish
pprint(cook_book)

