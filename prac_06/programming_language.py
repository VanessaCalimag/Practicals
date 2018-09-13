
class ProgrammingLanguage:
    def __init__(self, program="", typing="", reflection="", year=""):

        self.program = program
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} typing, reflection={}, introduced in year={}".format(self.program, self.typing,
                                                                            self.reflection, self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"

