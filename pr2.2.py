import math
print('Task 2 : ')
x1 = int(input('x1 = '))
y1= int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

#the distance between these points AB = √(x2 - x1)**2 + (y2 - y1)**2
print('distance between points = ', math.sqrt((x2-x1)**2+(y2-y1)**2))

#the slope of the line from the first point to the second
a = int((y2-y1)/(x2-x1))
print('slope of the line from the first point to the second = ', math.atan(a))

#whether both points lie on the same line from the origin (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)

#whether the first point is above the second
print('Is the first point above the second? = ' ,  (y1 > y2) )

#what quadrant the first point lies in (1st, 2nd, 3rd, or 4th)
def quadrant(x,y):

    if x > 0 and y > 0:
        return 1
    elif x < 0 < y:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 > y:
        return 4
print('Quadrant in which first point lies = ', quadrant(x1 , y1))

#whether the two points lie in the same quadrant
print('Do this two points lie in the same quadrant? = ', quadrant(x1, y1) == quadrant(x2, y2))





