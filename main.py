from pprint import pprint

cook_book = {}
with open('recipes.txt') as file:
    for recipe in file.read().split('\n\n'):
        name, q, *args = recipe.split('\n')
        recipe_list = []
        for arg in args:
            ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
            recipe_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[name] = recipe_list
pprint(cook_book, width=100)
print()


def get_shop_list_by_dishes(dishes, person):
    dishes_dict = {}
    for i in dishes:
        if i not in cook_book.keys():
            print(f'Блюда {i} нет в меню!')
        else:
            ingredients_list = cook_book[i]
            for i in ingredients_list:
                x = i.setdefault('ingredient_name')
                y = {'measure': i.setdefault('measure'), 'quantity': i.setdefault('quantity') * person}
                if x not in dishes_dict.keys():
                    dishes_dict[x] = y
                else:
                    dishes_dict[x] = {'measure': i.setdefault('measure'),
                                      'quantity': i.setdefault('quantity') * person + dishes_dict[x]['quantity']}
    pprint(dishes_dict)
    return


get_shop_list_by_dishes(['Запеченный картофель', 'Лазанья', 'Омлет' ], 2)

