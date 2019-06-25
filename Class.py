class AClass():
    name = "Uasya"

    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name


    def __setattr__ (self, name, value):
        print(name, value, "Ystanovka")
        super(). __seatler__(name, value)


if __name__ == '__main__':
    a = AClass("A", "Object")
    b = AClass("B", "Object")
    a.attr1 = 1
    print(dir(a))
    print(dir(b))
    print(a.__dict__)
    print(b.__dict__)
    print(dir(a.name))
    print(dir(b.name))
    print(a.first_name)
    print(b.first_name)
    print(a)
    print(b)
