#!/usr/bin/python3

class square():
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'width':
                    w = value
                if key == 'height':
                    h = value
            if w != h:
                raise ValueError("Width must be equal to height !")
            else:
                setattr(self, "width", w)
                setattr(self, "height", h)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=11, height=14)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
