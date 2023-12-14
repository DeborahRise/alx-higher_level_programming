#!/usr/bin/python3
""" My first class
Rectangle
"""


from models.base import Base
""" importing from the super class
"""


class Rectangle(Base):
    """ instantiation of the Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The base class constructor
        method
        """

        # if not isinstance(width, int):
        #     raise TypeError("width must be an integer")
        # if not isinstance(height, int):
        #     raise TypeError("height must be an integer")
        # if width <= 0:
        #     raise ValueError("width must be > 0")
        # if height <= 0:
        #     raise ValueError("width must be > 0")
        self.width = width
        self.height = height
        # if not isinstance(x, int):
        #     raise TypeError("x must be an integer")
        # if not isinstance(y, int):
        #     raise TypeError("y must be an integer")
        # if x < 0:
        #     raise ValueError("x must be >= 0")
        # if y < 0:
        #     raise ValueError("y must be >= 0")

        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """private getter width"""

        return self.__width

    @width.setter
    def width(self, value):
        """private setter width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """private getter height"""

        return self.__height

    @height.setter
    def height(self, value):
        """private setter height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """private getter x"""

        return self.__x

    @x.setter
    def x(self, value):
        """private setter x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """private getter y"""

        return self.__y

    @y.setter
    def y(self, value):
        """private setter y"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ width * height """

        return self.__width * self.__height

    def display(self):
        """ printing to stdout """

        for m in range(self.__y):
            print()
        for i in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ displays text to stdout in format """

        return (
                "[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id, self.__x, self.__y, self.__width, self.__height)
                )

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dic representation of
        a rect
        """

        return {
                'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
                }
