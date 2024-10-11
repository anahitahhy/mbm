import numpy as np
import matplotlib.pyplot as plt

# تابعی برای ایجاد گرادیان رنگ بین دو رنگ
def interpolate_color(color1, color2, t):
    return (1 - t) * np.array(color1) + t * np.array(color2)

# تابعی برای رسم تصویر با گرادیان رنگ
def draw_gradient(point1, point2, color1, color2):
    width, height = 400, 400
    image = np.zeros((height, width, 3))

    # محاسبه شیب خط
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    length = np.sqrt(dx**2 + dy**2)

    for y in range(height):
        for x in range(width):
            # محاسبه فاصله از نقطه اول
            d1 = np.sqrt((x - point1[0])**2 + (y - point1[1])**2)
            d2 = np.sqrt((x - point2[0])**2 + (y - point2[1])**2)

            # محاسبه t برای رنگ
            if d1 + d2 != 0:
                t = d1 / (d1 + d2)
                image[y, x] = interpolate_color(color1, color2, t)

    return image

# نقاط و رنگ‌ها
point1 = (200,100 )  # نقطه اول
point2 = (100, 300)  # نقطه دوم
color1 = (0, 0, 1)   # رنگ آبی (RGB)
color2 = (1, 0, 0)   # رنگ قرمز (RGB)

# رسم تصویر
image = draw_gradient(point1, point2, color1, color2)

# نمایش تصویر
plt.imshow(image)
plt.axis('off')  # حذف محور
plt.show()
