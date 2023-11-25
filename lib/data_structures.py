spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food=[]
    for name in spicy_foods:
      food.append(name["name"])
    return food
    pass

def get_spiciest_foods(spicy_foods):
    food=[]
    for i in spicy_foods:
        if i["heat_level"]>5:
          food.append(i)
    return food
    pass

def print_spicy_foods(spicy_foods):
    for name in spicy_foods:
     print(f"{name['name']} ({name['cuisine']}) | Heat Level: {'🌶' * name['heat_level']}")

    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"]==cuisine:
            return food
            
    pass

def print_spiciest_foods(spicy_foods):
    for name in spicy_foods:
     if name["heat_level"]>5:
      print(f"{name['name']} ({name['cuisine']}) | Heat Level: {'🌶' * name['heat_level']}")     
        
    pass

def get_average_heat_level(spicy_foods):
    heat_levels = sum([number["heat_level"]for number in spicy_foods])
    average=heat_levels/len(spicy_foods)
    return int(average)
    pass 

def create_spicy_food(spicy_foods, spicy_food):
    spicy_food =  {
                'name': 'Griot',
                'cuisine': 'Haitian',
                'heat_level': 10,
            }
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
