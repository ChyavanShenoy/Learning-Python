import math


def paint_calc(height, width, coverage):
    number_of_cans = math.ceil((height*width)/coverage)
    print(f"You will need {number_of_cans} numer of cans to paint the room.")


test_h = int(input("Height of the wall: "))
test_w = int(input("Width of yhe wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, coverage=coverage)
