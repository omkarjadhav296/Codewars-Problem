'''
You are given the length and width of a 4-sided polygon. 
The polygon can either be a rectangle or a square. If it is 
a square, return its area. If it is a rectangle, return its perimeter.
'''


def area_or_perimeter(l , w):
    if (l==w):
        print ("It is a square and its area is :")
        return l*l
    else:
        print("It is a rectangle and its perimeter is :")
        return 2*(l+w)