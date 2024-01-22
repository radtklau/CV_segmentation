import os
import cv2


def crop_images():

    for file in os.listdir('./data/val/'):
        print(f'saving {file}')
        cropcrop(f'./data/val/{file}', file)


def cropcrop(path, filename):
    img = cv2.imread(path)  # Use cv2.imread to read the image with OpenCV
    img1 = img[:, :256]  # Crop the left half of the image
    img2 = img[:, 256:512]  # Crop the right half of the image

    cv2.imwrite(f'./data/images/{filename}', img1)
    cv2.imwrite(f'./data/labels/{filename}', img2)


crop_images()
