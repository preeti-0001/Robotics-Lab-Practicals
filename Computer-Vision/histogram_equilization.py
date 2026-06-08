import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

img = np.array((
    [52, 55, 61, 59, 79, 61, 61], 
    [62, 59, 55,104, 94, 89, 71],
    [63, 65, 66,113,144,104, 62],
    [64, 70, 70,126,154,109, 63],
    [67, 73, 68,106,122, 88, 68],
    [68, 79, 60, 70, 77, 68, 75],
    [89, 65, 64, 58, 55, 61, 83],
    [70, 87, 69, 65, 73, 78, 90]
    ), dtype="uint8")


def custom_equalize_histogram(image):
    image_shape = image.shape
    equalized_image = np.zeros(image_shape, dtype="uint8")
    frequency = np.bincount(image.ravel(), minlength=256)
    cdf = frequency.cumsum()
    cdf = cdf / cdf[-1]
    cdf_min = cdf[np.nonzero(cdf)].min()
    lut = ((cdf - cdf_min) / (1 - cdf_min) * 255)
    lut = np.clip(lut, 0, 255).astype("uint8")
    equalized_image = lut[image]
    return equalized_image

def plot_histogram(histogram):
    plt.bar(range(256), histogram)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

def main():
    custom_equalized_img = custom_equalize_histogram(img)

    equalized_img = cv2.equalizeHist(img)
    equalized_frequency = np.bincount(equalized_img.ravel(), minlength=256)
    manual_frequency = np.bincount(custom_equalized_img.ravel(), minlength=256)
    frequency = np.bincount(img.ravel(), minlength=256)
    

    plt.figure(figsize=(12,6))
    plt.subplot(2,3,1)
    plot_histogram(frequency)
    plt.title("Actual Histogram")
    plt.subplot(2,3,2)
    plot_histogram(manual_frequency)
    plt.title("Manual Equalize Histogram")
    plt.subplot(2,3,3)
    plot_histogram(equalized_frequency)
    plt.title("In-Built Histogram")
    plt.subplot(2,3,4)
    plt.imshow(img, cmap="gray")
    plt.subplot(2,3,5)
    plt.imshow(custom_equalized_img, cmap="gray")
    plt.subplot(2,3,6)
    plt.imshow(equalized_img, cmap="gray")
    
    plt.show()

if __name__ == "__main__":
    main()
