from circle import Circle
from hexagon import Hexagon
from traingle import Traingle
from square import Square
from rectangle import Rectangle


def main():
    try:
        all_shapes = [Rectangle(width=10,height=5),
                    Circle(radius=8),
                    Traingle(base=5,height=10,side_a=6,side_b=5,side_c=6),
                    Hexagon(side=7),
                    Square(side=8)]
    
        for shape in all_shapes:
           print(shape)
           print("***********")
        print(" == Developer Notes == ")
        for shape in all_shapes:
           print(repr(shape))
           print("***********")
    
    except (ValueError,TypeError) as e:
        print(e) 
if __name__ == "__main__":
    main()