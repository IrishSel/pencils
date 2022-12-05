from skimage.measure import label, regionprops
from skimage.morphology import binary_closing
import cv2
import os

pencils = 0
for path in os.listdir('images'):

    image = cv2.imread(f'images/{path}')
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grey[grey > 125] = 0
    grey[grey != 0] = 255
    grey = binary_closing(binary_closing(grey))
    labeled = label(grey)
    regions = regionprops(labeled)
    figures = []
    for i in range(len(regions)):
        area = regions[i].image.shape[0] * regions[i].image.shape[1]
        if area > 10000:
            figures.append(regions[i])
    k = 0
    for img in figures:
        if round(img.eccentricity, 3) >= 0.998 and img.area > 250000:
            k += 1
    pencils += k
    print(path, k)
    cv2.destroyAllWindows()
print(f'{pencils} pencils')
