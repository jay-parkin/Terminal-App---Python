class Ingredients:
    def __init__(self, _name, _amount, _unit=""):
        self._name = _name
        self._amount = _amount
        self._unit = _unit

    def display_info(self):
        print(f"Ingredient: {self.name}")
        print(f"Amount: {self._amount} {self.unit}")

        if self.description:
            print(f"Description: {self.description}")