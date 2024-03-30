import math

def draw_pyramid(height):
    if height > 10:
        print('The pyramid can not be greater than 10!')

    else:
        for i in range(1, height * 2 + 1, 2):
            print(' ' * math.floor((height * 2 - i) / 2) + i * 'A' + ' ' * math.floor((height * 2 - i) / 2))
    
    
height = int(input('Provide a height of the pyramid: '))

draw_pyramid(height)