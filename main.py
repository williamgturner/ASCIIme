from PIL import Image
import numpy as np
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3 main.py <imagePath>")
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print("Error: File not found. Please check the path and try again.")
    sys.exit(1)

image = Image.open(sys.argv[1])
width, height = image.size
aspectRatio = height/width
new_width = 50
new_height = int(aspectRatio * new_width * 0.5)
image = image.resize((new_width, new_height))
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
