import math

class Circle:
  def __init__(self, radius):
    # __변수 : private
    self.__radius = radius
  
  def get_circumference(self):
    return 2 * math.pi * self.__radius
  
  def get_circle_area(self):
    return math.pi * (self.__radius ** 2)
  
circle = Circle(10)
print("원 둘레 : ", circle.get_circumference())
print("원 면적 : ", circle.get_circle_area())
