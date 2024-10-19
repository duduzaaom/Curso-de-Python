def process_file(filename: str) -> dict:
    recipes = {}
    start = True

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if start == True:
                recipe_name = line
                recipes[recipe_name] = []
                start = False
                continue
            if line == '':
                start = True
                continue
            else:
                recipes[recipe_name].append(line)
            
    return recipes

def search_by_name(filename: str, word: str) -> list:
    recipes = process_file(filename)
    search_result = []

    for recipe in recipes:
        if word.lower() in recipe.lower():
            search_result.append(recipe)

    return search_result


def search_by_time(filename: str, prep_time: int) -> list:
    recipes = process_file(filename)
    search_result = []

    for recipe, info in recipes.items():
        if int(info[0]) <= prep_time:
            search_result.append(f'{recipe}, preparation time {int(info[0])} min')

    return search_result


def search_by_ingredient(filename: str, ingredient: str) -> list:
    recipes = process_file(filename)
    search_result = []

    for recipe, info in recipes.items():
        if ingredient in info:
            search_result.append(f'{recipe}, preparation time {int(info[0])} min')

    return search_result


if __name__ == '__main__':
    found_recipes = search_by_ingredient("recipes1.txt", "milk")

    for recipe in found_recipes:
        print(recipe)

