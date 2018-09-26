
class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def get_name(self):
        return self.name

    def is_dynamic(self):
        # if self.typing == "Dynamic":
        #     return True
        # else:
        #     return False
        return self.typing == "Dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.is_dynamic(),
                                                                           self.year)
