class Allergies:
    def __init__(self, score):
        self.score = score
        self.allergens = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128,
        }

    def allergic_to(self, item):
        if self.score & self.allergens[item]:
            return True
        return False

    @property
    def lst(self):
        have_allergies_to = []
        for item in self.allergens:
            if self.allergic_to(item):
                have_allergies_to.append(item)
        return have_allergies_to
