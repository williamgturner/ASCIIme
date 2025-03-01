from PIL import Image
import numpy as np

image = Image.open('test2.jpg')
width, height = image.size
image = image.resize((int(width * 0.3), int(height * 0.3)))
width, height = image.size
grey = image.convert('L')
pixel_array = np.array(grey)

with open('ascii.txt', 'w') as file:
    
    for i in range(height):
        for j in range(width):
            px = pixel_array[i, j]
            if px > 0 and px < 25:
                file.write('@')
            elif px < 50:
                file.write('#')
            elif px < 75:
                file.write('$')
            elif px < 100:
                file.write('*')
            elif px < 125:
                file.write('%')
            elif px < 150:
                file.write('?')
            elif px < 175:
                file.write('+')
            elif px < 200:
                file.write('^')
            elif px < 225:
                file.write('-')
            elif px <= 255:
                file.write('.')
        file.write('\n')
