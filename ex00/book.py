from recipe import Recipe
import datetime


class Book:
    """name
    last_update
    creation_date
    recipes_list"""

    def __init__(self, name, rcp_lst):
        """Init Book with name and some recipes"""
        if isinstance(name, str) is True:
            self.name = name
        else:
            print("Name is a", type(name), "I need a string")
            exit(1)
        self.creation_time = datetime.datetime.now()
        self.last_update = self.creation_time
        self.recipes_list = rcp_lst

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        if isinstance(name, str) is False:
            print("Name is a", type(name), "I need a str")
            exit(1)
        for elem in self.recipes_list["dessert"]:
            if name is elem.name:
                print(str(elem))
                return elem

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe) is not True:
            print("Recipe is a", type(recipe), "not a Recipe")
            return
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
            return self

    def get_recipes_by_types(self, recipe_type):
        if isinstance(recipe_type, str) is False:
            print("Recipe_type is a", type(recipe_type), "I need a string")
            exit(1)
        if recipe_type is not "starter"\
            and recipe_type is not "lunch"\
                and recipe_type is not "dessert":
                print("Not a valid recipe_type")
                exit(1)
        ret = []
        for elem in self.recipes_list[recipe_type]:
            ret.append(elem)
        return ret
