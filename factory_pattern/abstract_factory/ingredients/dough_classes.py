from abstract_factory.ingredients.dough import Dough



class ThinCrustDough(Dough):

    def __str__(self):
        return "Thin Crust Dough"


class ThickCrustDough(Dough):

    def __str__(self):
        return "Extra thick crust dough"