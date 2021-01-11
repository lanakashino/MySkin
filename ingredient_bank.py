import glob
import os
import numpy as np


class IngredientBank:

    # check for similar meaning ingredients
    def __init__(self, name):
        self._name = name
        file = glob.glob(os.curdir + "\\Data\\" + name + ".npy")
        if file:
            self._whitelist = np.load(file[0], allow_pickle=True).item()
            self._greylist = np.load(file[0], allow_pickle=True).item()
        else:
            self._greylist = {}
            self._whitelist = {}

    def add_product(self, ingredients, compatible):
        if compatible:
            for ingredient in ingredients:
                self.add_to_whitelist(ingredient)
        else:
            for ingredient in ingredients:
                self.add_to_greylist(ingredient)

    # Bad unrepresentative name
    def add_to_greylist(self, ingredient):
        if self._whitelist.get(ingredient):
            self._whitelist[ingredient] = (self._whitelist.get(ingredient)[0], self._whitelist.get(ingredient)[1] + 1)
        else:
            if self._greylist.get(ingredient):
                self._greylist[ingredient] = (self._greylist.get(ingredient)[0], self._greylist.get(ingredient)[1] + 1)
            else:
                self._greylist.update({ingredient: (0, 1)})

    def add_to_whitelist(self, ingredient):
        if self._whitelist.get(ingredient):
            self._whitelist[ingredient] = (self._whitelist.get(ingredient)[0] + 1, self._whitelist.get(ingredient)[1])
        else:
            if self._greylist.get(ingredient):
                self._whitelist[ingredient] = (self._greylist.get(ingredient)[0] + 1, self._greylist.get(ingredient)[1])
            else:
                self._whitelist.update({ingredient: (1, 0)})
            self._greylist.pop(ingredient, None)

    def check_product(self, ingredients):
        yellow = []
        new = []
        for ingredient in ingredients:
            if ingredient in self._greylist:
                yellow.append(ingredient)
            elif ingredient not in self._whitelist:
                new.append(ingredient)
        print("ingredients you tried that are not whitelisted:")
        print("\t{}".format(yellow))
        print("new ingredients that you've never tried:")
        print("\t{}".format(new))

    def close(self):
        np.save(os.curdir + "\\Data\\" + self._name + ".npy", self._whitelist)
        np.save(os.curdir + "\\Data\\" + self._name + ".npy", self._greylist)
