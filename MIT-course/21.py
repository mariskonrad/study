import math

# A regular polygon has n number of sides. Each side has length s.
# The area of a regular polygon is: (0.25 * n * s**2) / (tan(pi / n))
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.

def polysum(n, s):
    '''
    n: number of sides (int or float)
    s: lengh of side (int or float)
    Returns the sum of the area with the square of the perimeter of the regular polygon
    rounded to 4 decimal places.
    '''
    piDivision = math.pi / n
    area = (0.25 * n * s**2) / (math.tan(piDivision))
    perimeter = n * s
    answer = perimeter**2 + area

    return round(answer, 4)

print(polysum(49, 89))
