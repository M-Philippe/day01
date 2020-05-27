from recipe import Recipe
from book import Book
import time

lst = ["Pates", "Sauce Tomate", "Viande"]
rcp = Recipe("Lasagne", 3, 45, lst, None, "lunch")
lst2 = ["Cereales", "Lait"]
rcp2 = Recipe("Cereales", 1, 0, lst2, None, "starter")
#print(str(rcp))
#print(str(rcp2))
dico_recipes= {
	"starter": [rcp2],
	"lunch": [rcp],
	"dessert": [],
}

ck = Book("Cookbook", dico_recipes)
rcp2 = Recipe("ABCD", 5, 100, lst, None, "dessert")
ck.add_recipe(rcp2)
#ck.get_recipe_by_name("ABCD")
print(ck.creation_time)
#time.sleep(1)
rcp4 = Recipe("New_Lasagne", 3, 45, lst, None, "lunch")
#ck.add_recipe(rcp4)
print(ck.last_update)
rcp4 = Recipe("Morning_Lasagne", 3, 45, lst, None, "starter")
ck.add_recipe(rcp4)
lst = ck.get_recipes_by_types("starter")
for elem in lst:
	print(str(elem))
#print(ck.creation_time)
