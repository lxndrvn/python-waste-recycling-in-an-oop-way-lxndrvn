from garbage import Garbage


class PlasticGarbage(Garbage):
    def __init__(self, name, is_clean):
        super(PlasticGarbage, self).__init__(name)  # kerdes
        self.is_clean = is_clean

    def clean(self):
        self.is_clean = True
