import math


def square(side):
    result = side * side
    if result != int(result):
        return math.ceil(result)
    return int(result)


print(square(4))
print(square(3.5))
