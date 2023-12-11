#!/usr/bin/python3
""" And Now The Square
"""


from models.rectangle import Rectangle
""" activating/importing the Rectangle class
"""


class Square(Rectangle):
    """ The square inherits every attribute from the
    Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ square class instantiation method """

        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns a string of attribute"""

        return (
                "[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.width)
                )

    @property
    def size(self):
        """ adding the public getter """

        return self.width

    @size.setter
    def size(self, value):
        """ adding public setter """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updating the class square
        by adding public method
        """

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a square
        """

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
