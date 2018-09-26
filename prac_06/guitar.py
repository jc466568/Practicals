
class Guitar:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost
        self.guitar_age = 0

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        self.guitar_age = 2018 - self.year
        return self.guitar_age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
