import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("Computer-Vision/images/input/1-b.jpeg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("Computer-Vision/images/input/1-b.jpeg", cv2.IMREAD_GRAYSCALE)

img1_hist = cv2.equalizeHist(img1)
img2_hist = cv2.equalizeHist(img2)

clahe_engine = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8,8))
clahe1 = clahe_engine.apply(img1)
clahe2 = clahe_engine.apply(img2)

gamma = 0.8

normalized = img1 / 255.0
gamma_corrected = (normalized ** gamma) * 255
gamma_corrected = gamma_corrected.astype("uint8")


blur = cv2.GaussianBlur(clahe1, (5,5), 0)

edge = cv2.Canny(blur, 120, 120)

plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.imshow(img1, cmap="gray")
plt.title("Image 1")
plt.axis("off")
plt.subplot(2,3,2)
plt.imshow(img1_hist, cmap="gray")
plt.title("Image 1 Equilized")
plt.axis("off")
plt.subplot(2,3,3)
plt.imshow(clahe1, cmap="gray")
plt.title("Image 1 CLAHE")
plt.axis("off")
plt.subplot(2,3,4)
plt.imshow(gamma_corrected, cmap="gray")
plt.title("Image 1 Gamma Corrected")
plt.axis("off")
plt.subplot(2,3,5)
plt.imshow(blur, cmap="gray")
plt.title("Image 1 CLAHE")
plt.axis("off")
plt.subplot(2,3,6)
plt.imshow(edge, cmap="gray")
plt.title("Image 1 Gamma Corrected")
plt.axis("off")



# plt.subplot(2,4,5)
# plt.imshow(img2, cmap="gray")
# plt.title("Image 2")
# plt.axis("off")
# plt.subplot(2,4,6)
# plt.imshow(img2_hist, cmap="gray")
# plt.title("Image 2")
# plt.axis("off")
# plt.subplot(2,4,7)
# plt.imshow(img2, cmap="gray")
# plt.title("Image 2")
# plt.axis("off")
# plt.subplot(2,4,8)
# plt.imshow(img2, cmap="gray")
# plt.title("Image 2")
# plt.axis("off")


plt.show()



blur1 = cv2.GaussianBlur(clahe1, (7,7), 0)
blur2 = cv2.GaussianBlur(clahe2, (7,7), 0)

edge1 = cv2.Canny(blur1, 30, 100)
edge2 = cv2.Canny(blur2, 30, 100)
