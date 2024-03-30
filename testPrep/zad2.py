def draw_tower(height):
    if height > 10:
        print('The height can not be greater than 10!')

    else:    
        for i in range(1, height + 1):
            print('A' * i)
    
    
height = int(input('Provide a height of the tower: '))

draw_tower(height)