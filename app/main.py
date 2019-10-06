import cv2
import numpy as np



def rotate(points, angle):
    new_points = []
    count = 0
    if len(points) == 3:
        for x, y in points:
            count += 1
            if count == 1:
                new_points.append((int(x + (angle * 1.5)), y))
            elif count == 2:
                new_points.append((x + angle, y + angle))
            else:
                new_points.append((x + angle, int(y + (angle / 2))))
    else:
        for x, y in points:
            count += 1
            if count == 1:
                new_points.append((x, int(y + (angle / 3))))
            elif count == 2:
                new_points.append((x, int(y + ((2 * angle) / 3))))
            elif count == 3:
                new_points.append((x + angle, int(y + ((2 * angle) / 3))))
            else:
                new_points.append((x + angle, y))

    return new_points

def translate(points, tx = 0, ty = 0):
    return [(x + tx, y + ty) for x, y in points]

# canvas = np.ones((300, 400, 3)) * 255 #imagem 400x300, com fundo branco e 3 canais para as cores
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)
# image = cv2.imread(path)
border_color = (0, 0, 0)
border_px = 2
# path
path = r'girassol.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Center coordinates
center_coordinates = (135, 130)
radius = 50

# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, border_color, border_px)
radius = 35
image = cv2.circle(image, center_coordinates, radius, border_color, border_px)
radius = 25
image = cv2.circle(image, center_coordinates, radius, border_color, border_px)
radius = 10
image = cv2.circle(image, center_coordinates, radius, border_color, border_px)

triangle = [(125, 10), (130, 30), (120, 30)]
cv2.drawContours(image, [np.array(triangle)], 0, border_color, border_px)

rectangle = [(120, 80), (130, 80), (130, 30), (120, 30)]
cv2.drawContours(image, [np.array(rectangle)], 0, border_color, border_px)

cv2.drawContours(image, [np.array(translate(triangle, 12, 0))], 0, border_color, border_px)
cv2.drawContours(image, [np.array(translate(rectangle, 12, 0))], 0, border_color, border_px)

cv2.drawContours(image, [np.array(rotate(translate(triangle, 24, 0), 3))], 0, border_color, border_px)
cv2.drawContours(image, [np.array(rotate(translate(rectangle, 24, 0), 3))], 0, border_color, border_px)

cv2.drawContours(image, [np.array(rotate(translate(triangle, 36), 6))], 0, border_color, border_px)
cv2.drawContours(image, [np.array(rotate(translate(rectangle, 36, 3), 6))], 0, border_color, border_px)

cv2.drawContours(image, [np.array(rotate(translate(triangle, 40, 0), 15))], 0, border_color, border_px)
cv2.drawContours(image, [np.array(rotate(translate(rectangle, 40, 3), 15))], 0, border_color, border_px)

cv2.drawContours(image, [np.array(rotate(translate(triangle, 48, 0), 21))], 0, border_color, border_px)
cv2.drawContours(image, [np.array(rotate(translate(rectangle, 48, 6), 21))], 0, border_color, border_px)

cv2.drawContours(image, [np.array(rotate(translate(triangle, 68, 12), 28))], 0, border_color, border_px)
cv2.drawContours(image, [np.array(rotate(translate(rectangle, 54, 12), 36))], 0, border_color, border_px)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)


