import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_image_and_hist(img, title, position):
    """Helper function to plot image and its histogram."""
    # Plot Image
    plt.subplot(3, 4, 2 * position -1)
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.title(title)
    plt.axis('off')
    
    # Plot Histogram
    plt.subplot(3, 4, position * 2)
    plt.hist(img.ravel(), 256, [0, 256], color='Blue')
    plt.title(f'Histogram: {title}')
    plt.xlim([0, 256])

def process_and_display(image_path):
    # 1. Load Original Image in Grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error loading {image_path}")
        return

    plt.figure(figsize=(12, 8))

    # Original
    plot_image_and_hist(img, "Original Image", 1)

    # 2. Image Negative
    # Formula: s = (L - 1) - r
    img_neg = 255 - img
    plot_image_and_hist(img_neg, "Image Negative", 2)

    # 3. Log Transformation
    # Formula: s = c * log(1 + r)
    c = 255 / np.log(1 + np.max(img))
    img_log = c * (np.log(img + 1))
    img_log = np.array(img_log, dtype=np.uint8)
    plot_image_and_hist(img_log, "Log Transformation", 3)

    # 4. Gamma Correction (Gamma = 0.5 and Gamma = 2.0)
    # Formula: s = c * r^gamma
    gamma_low = 0.5
    img_gamma_low = np.array(255 * (img / 255) ** gamma_low, dtype=np.uint8)
    plot_image_and_hist(img_gamma_low, f"Gamma Correction (γ={gamma_low})", 4)

    gamma_high = 2.0
    img_gamma_high = np.array(255 * (img / 255) ** gamma_high, dtype=np.uint8)
    plot_image_and_hist(img_gamma_high, f"Gamma Correction (γ={gamma_high})", 5)

    # 5. Contrast Stretching
    # Formula: s = (r - min) * (255 / (max - min))
    min_val = np.min(img)
    max_val = np.max(img)
    img_stretch = np.array((img - min_val) * (255.0 / (max_val - min_val)), dtype=np.uint8)
    plot_image_and_hist(img_stretch, f"Contrast Stretching", 6)

    # Optional: Plot Contrast Stretching in a new figure
    plt.tight_layout()
    plt.show()

# Process each image
images = ['Computer-Vision/images/input/A.jpeg', 'Computer-Vision/images/input/B.jpeg', 'Computer-Vision/images/input/C.jpeg']
for img_name in images:
    print(f"Processing {img_name}...")
    process_and_display(img_name)