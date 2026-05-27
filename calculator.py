class Shape:
    def get_area(self):
       pass
    
    def get_perimeter(self):
       pass 

    def __str__(self):
       return f"Shape: {self.__class__.__name__}, area: {self.get_area():.1f}, perimeter: {self.get_perimeter():.1f}"
    