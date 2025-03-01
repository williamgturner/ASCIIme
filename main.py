from PIL import Image
import numpy as np

image = Image.open('test2.jpg')
width, height = image.size

grey = image.convert('L')
pixel_array = np.array(grey)

with open('ascii.txt', 'w') as file:
    
    for i in range(height):
        for j in range(width):
            px = pixel_array[i, j]
            char = '|'
            if px > 0 and px < 50:
                char = '@'
            elif px < 75:
                char = '%'
            elif px < 100:
                char = '*'
            elif px < 125:
                char = '$'
            elif px < 150:
                char = '&'
            elif px < 175:
                char = '?'
            elif px < 200:
                char = '+'
            elif px < 225:
                char = '{'
            elif px <= 255:
                char = '.'
            file.write(char)
        file.write('\n')

