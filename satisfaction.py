from db import DB
from optimizer import Optimizer

class Satisfaction:
    def __init__(self):
        self.__db = DB("data.json")
        self.__opt = Optimizer(self.__db)

    def items(self, *args):
        print("calling !items with", len(args), "arguments:", ', '.join(args))

        if len(args) == 0:
            out = []
            for item in sorted(self.__db.items()):
                out.append(item)
            return '\n'.join(out)
        if len(args) == 1:
            item = args[0]
            if item not in self.__db.items():
                return "Unknown item: " + item
            return self.__db.items()[item].details()

    def recipes(self, *args):
        print("calling !recipes with", len(args), "arguments:", ', '.join(args))

        if len(args) == 0:
            out = []
            for recipe in sorted(self.__db.recipes()):
                out.append(recipe)
            return '\n'.join(out)
        if len(args) == 1:
            arg = args[0]
            if arg not in self.__db.items() and arg not in self.__db.recipes():
                return "Unknown recipe or item: " + arg
            if arg in self.__db.recipes():
                return self.__db.recipes()[arg].details()
            if arg in self.__db.items():
                out = []
                out.append("Recipes producing item:")
                for recipe in self.__db.recipes_for_product(arg):
                    out.append(recipe.details())
                out.append("Recipes requiring item:")
                for recipe in self.__db.recipes_for_ingredient(arg):
                    out.append(recipe.details())
                return '\n'.join(out)

    def min(self, *args):
        print("calling !min with", len(args), "arguments:", ', '.join(args))
        return self.__opt.optimize(False, *args)

    def max(self, *args):
        print("calling !max with", len(args), "arguments:", ', '.join(args))
        return self.__opt.optimize(True, *args)