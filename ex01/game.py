class GotCharacter:
    """Create a GotCharacter"""
    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = is_alive

    def parent_print(self):
        print("This is a parent print")


class Stark(GotCharacter):
    """Child class representing a GotCharacter"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
