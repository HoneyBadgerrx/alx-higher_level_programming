#!/usr/bin/python3
"""
module containing rectanfle module
"""


Base = __import__("base").Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """returns area of rect"""
        return self.width * self.height

    def display(self):
        """displays rect with # with coordinates x,y"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args):
        """updates values of objects"""
        try:
            self.id = args[0]
        except IndexError:
            pass
        try:
            self.width = args[1]
        except IndexError:
            pass
        try:
            self.height = args[2]
        except IndexError:
            pass
        try:
            self.x = args[3]
        except IndexError:
            pass
        try:
            self.y = args[4]
        except IndexError:
            pass

    @property
    def x(self):
        """return x"""
        return self.__x
    @x.setter
    def x(self, x):
        """sets x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """return y"""
        return self.__y
    @y.setter
    def y(self, y):
        """sets y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """return width"""
        return self.__width
    @width.setter
    def width(self, width):
        """sets width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """returna height"""
        return self.__height
    @height.setter
    def height(self, height):
        """sets height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    def __str__(self):
        """returns informal string repr of object"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y,\
                 self.width, self.height)
k = Rectangle(5,5,5,0,5)
print(vars(k))
k.update(1,1,1)
print(vars(k))
