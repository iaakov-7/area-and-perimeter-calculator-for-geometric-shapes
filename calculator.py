class Shape:
    def get_area(self):
       pass
    
    def get_perimeter(self):
       pass 

    def __str__(self):
       return f"Shape: {self.__class__.__name__}\narea: {self.get_area():.1f}\nperimeter: {self.get_perimeter():.1f}"
    
    def __repr__(self):
        parms = "|".join(f"{k}={v}" for k,v in self.__dict__.items())
        return f"Shape: {self.__class__.__name__}\n{parms}"
    
    def validation(self,*args):
       for value in args:
            if not isinstance(value,(int,float)):
                raise TypeError("Any value most be numbers")
            if value <= 0:
                raise ValueError("Any value most be > 0")               