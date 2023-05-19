from pprint import pprint

with open('recipes.txt') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredient_count = int(file.readline())
        dish = []
        for i in range(ingredient_count):
            book = file.readline()
            ing, count, unit = book.strip().split(' | ')
            dishes = {
                'ingredient_name': ing,
                'quantity': count,
                'measure': unit
            }
            dish.append(dishes)
        file.readline()
        cook_book[dish_name] = dish
    pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        recipe = cook_book[dish]
        for ingredient in recipe:
            name = ingredient['ingredient_name']
            if name not in shop_list:
                shop_list_1 = {
                    'measure': ingredient['measure'],
                    'quantity': int(ingredient['quantity']) * person_count
                }
                shop_list[name] = shop_list_1
            else:
                shop_list[name]['quantity'] += int(ingredient['quantity']) * person_count

    pprint(shop_list, sort_dicts=False)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)