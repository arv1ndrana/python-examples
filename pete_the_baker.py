def cakes(recipe, available):
    recipe_list = list(recipe.keys())
    available_list = list(available.keys())

    check = all(i in available_list for i in recipe_list)

    if not check:
        return 0
    else:
        common = []
        bakeable = []
        for item in available_list:
            if item in recipe_list:
                common.append(item)
        for item in common:
            can_bake = int(available.get(item)) // int(recipe.get(item))
            bakeable.append(can_bake)
        return min(bakeable)
