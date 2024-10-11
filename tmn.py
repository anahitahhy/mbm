import numpy as np
import matplotlib.pyplot as plt


def interpolate_color(color1, color2, t):
    return (1 - t) * np.array(color1) + t * np.array(color2)


def draw_gradient(point1, point2, color1, color2):
    width, height = 400, 400
    image = np.zeros((height, width, 3))

    
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    length = np.sqrt(dx**2 + dy**2)

    for y in range(height):
        for x in range(width):
        
            d1 = np.sqrt((x - point1[0])**2 + (y - point1[1])**2)
            d2 = np.sqrt((x - point2[0])**2 + (y - point2[1])**2)

        
            if d1 + d2 != 0:
                t = d1 / (d1 + d2)
                image[y, x] = interpolate_color(color1, color2, t)

    return image


point1 = (200,100 )  
point2 = (100, 300)  
color1 = (0, 0, 1)  
color2 = (1, 0, 0)   

image = draw_gradient(point1, point2, color1, color2)

plt.imshow(image)
plt.axis('off') 
plt.show()
