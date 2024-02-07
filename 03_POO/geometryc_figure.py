import re

from numpy import double


class GeometryFigure() :

    def __init__(self, side1: int, side2: int) -> None:
        self.__side1 = side1
        self.__side2 = side2
    
    @property
    def side1(self) -> int:
        return self.__side1

    @side1.setter
    def side1(self, size : int) -> None:
        self.__side1 = size

    @property
    def side2(self) -> int:
        return self.__side2

    @side2.setter
    def side2(self, size: int) -> None:
        self.__side2 = size

    @property
    def area(self) -> int:
        return self.side1 * self.side2
    
    @staticmethod
    def info() -> str:
        return "This is a Geometry Figure"

    def __str__(self) -> str:
        return f"Figure: {self.side1} {self.side2} with a {self.area} Area"


class Triangle(GeometryFigure):

    def __init__(self, side1: int, side2: int, height: int) -> None:
        super().__init__(side1, side2)
        self.__height = height

    @property
    def height(self) -> int:
        return self.__height
    
    @height.setter
    def height(self, size: int) -> None:
        self.__height = size

    @property
    def area(self) -> double:
        return (self.side1* self.height)/2