class Recipe:
    """name
    cooking_lvl
    cooking_time
    ingredients
    description
    recipe_type"""

    def __init__(self, name, c_lvl, c_tme, ingdt, dscrpt, rcp_type):
        """Init the recipe"""
        if isinstance(name, str) is True:
            self.name = name
        else:
            print("Name is a", type(name), "I need a string")
            exit(1)
        if isinstance(c_lvl, int) is True:
            if c_lvl >= 1 and c_lvl <= 5:
                self.cooking_lvl = c_lvl
            else:
                print("Cooking_lvl is", c_lvl, "Must be beetween 1-5")
                exit(1)
        else:
            print("Cooking_lvl is a", type(c_lvl), "I need an integer")
            exit(1)
        if isinstance(c_tme, int) is True:
            if c_tme >= 0:
                self.cooking_time = c_tme
            else:
                print("No negative value for cooking_time")
                exit(1)
        else:
            print("Coking_time,is a", type(c_tme), "I need a positive integer")
        if isinstance(ingdt, list):
            if len(ingdt) > 0:
                self.ingredients = ingdt
            else:
                print("Can't have 0 ingredients")
                exit(1)
        else:
            print("list is a", type(ingdt), "I need a list")
            exit(1)
        if dscrpt is None:
            self.description = "No description"
        else:
            if isinstance(dscrpt, str) is True:
                self.description = dscrpt
            else:
                print("Description is a", type(str), "Must be a string")
        if isinstance(rcp_type, str) is True:
            if rcp_type is "starter" or rcp_type is "lunch"\
                    or rcp_type is "dessert":
                self.recipe_type = rcp_type
            else:
                print("Type's", rcp_type, "Choice : starter, lunch or dessert")
                exit(1)
        else:
            print("Recipe_type is a", type(rcp_type), "Needs a string")
            exit(1)

    def __str__(self):
        """Return the string to print with the recipe info"""
        line = "Name : " + self.name + "\n"
        line = line + "Cooking_lvl: " + str(self.cooking_lvl) + "\n"
        line = line + "Cooking time: " + str(self.cooking_time) + "\n"
        line = line + "Ingredients: "
        for ingr in self.ingredients:
            line = line + ingr + ", "
        line = line.rstrip(', ')
        line = line + "\n"
        line = line + "Description: " + self.description + "\n"
        line = line + "Type: " + self.recipe_type
        return line
