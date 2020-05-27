class Vector:
    """lst_vector
    size"""

    def __init__(self, *arg):
        if len(arg) is not 1:
            print("Just One Arg")
            exit(1)
        if isinstance(arg[0], list):
            if len(arg[0]) is 0:
                print("Can't be an empty list")
                exit(1)
            self.lst_vector = arg[0]
            self.size = len(self.lst_vector)
            return
        if isinstance(arg[0], range):
            self.lst_vector = []
            for v in arg[0]:
                self.lst_vector.append(v)
            self.size = len(self.lst_vector)
            return
        if isinstance(arg[0], int):
            if arg[0] <= 0:
                print("can't have negative size")
                exit(1)
            i = 0
            self.lst_vector = []
            self.size = arg[0]
            while i < self.size:
                self.lst_vector.append(i)
                i += 1
            return
        else:
            print("arg is", type(arg[0]), "Must be list, range or int")
            exit(1)

    def __add__(self, v2):
        if isinstance(v2, float) is True or isinstance(v2, int) is True:
            i = 0
            ret = Vector(self.size)
            while i < self.size:
                ret.lst_vector[i] = self.lst_vector[i] + v2
                i += 1
            return ret
        if isinstance(v2, Vector) is True:
            if self.size is not v2.size:
                print("Can't add two vectors of different size")
                exit(1)
            i = 0
            ret = Vector(self.size)
            while i < self.size:
                ret.lst_vector[i] = self.lst_vector[i] + v2.lst_vector[i]
                i += 1
            return ret
        else:
            print("Bad type: ", type(v2), "Only Vector or Float")
            exit(1)

    def __radd__(self, scl):
        return self.__add__(scl)

    def __sub__(self, v2):
        if isinstance(v2, float) is True or isinstance(v2, int) is True:
            i = 0
            ret = Vector(self.size)
            while i < self.size:
                ret.lst_vector[i] = self.lst_vector[i] - v2
                i += 1
            return ret
        if isinstance(v2, Vector) is True:
            if self.size is not v2.size:
                print("Can't sub two vectors of different size")
                exit(1)
            i = 0
            ret = Vector(self.size)
            while i < self.size:
                ret.lst_vector[i] = self.lst_vector[i] - v2.lst_vector[i]
                i += 1
            return ret
        else:
            print("Bad type: ", type(v2), "Only Vector or Float")
            exit(1)

    def __rsub__(self, scl):
        return self.__sub__(scl)

    def __truediv__(self, v2):
        if isinstance(v2, float) is True or isinstance(v2, int) is True:
            i = 0
            ret = Vector(self.size)
            while i < self.size:
                ret.lst_vector[i] = self.lst_vector[i] / v2
                i += 1
            return ret
        else:
            print("Bad type: is a", type(v2), "Must be a float or int")
            exit(1)

    def __rtruediv__(self, v2):
        return self.__truediv__(v2)

    def __mul__(self, v2):
        if isinstance(v2, float) is True or isinstance(v2, int) is True:
            i = 0
            ret = Vector(self.size)
            while i < self.size:
                ret.lst_vector[i] = self.lst_vector[i] * v2
                i += 1
            return ret
        if isinstance(v2, Vector) is True:
            if self.size is not v2.size:
                print("Can't multiply two vectors of different size")
                exit(1)
            i = 0
            ret = 0
            while i < self.size:
                ret = ret + self.lst_vector[i] * v2.lst_vector[i]
                i += 1
            return ret
        else:
            print("Bad type: ", type(v2), "Only Vector or Float")
            exit(1)

    def __rmul__(self, v2):
        return self.__mul__(v2)
