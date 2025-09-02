import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Paths
input_path = r"image manipulation/original images/example.jpeg"
output_dir = r"image manipulation/output images/"

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

# 1. Load the Image
image = cv2.imread(input_path)

# 2. Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display grayscale image (optional)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.show()

# Save grayscale
cv2.imwrite(os.path.join(output_dir, "grayscale.jpeg"), gray)

# 3. Crop the Image
cropped = image[100:300, 200:400]   # Adjust numbers to your image size
cv2.imwrite(os.path.join(output_dir, "cropped.jpg"), cropped)

# 4. Rotate the Image (45 degrees)
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, matrix, (w, h))
cv2.imwrite(os.path.join(output_dir, "rotated.jpg"), rotated)

# 5. Adjust Brightness (+50 to all pixels)
brightness = cv2.convertScaleAbs(image, alpha=1, beta=50)
cv2.imwrite(os.path.join(output_dir, "brightened.jpg"), brightness)

print("✅ Transformations completed. Check the 'output_images' folder!")
