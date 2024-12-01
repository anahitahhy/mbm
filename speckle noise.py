import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_speckle_noise(image, mean=0, var=0.1):

    # Ensure the image is in float32 format for proper noise addition
    image = image.astype(np.float32) / 255.0
    # Create speckle noise
    noise = np.random.normal(mean, np.sqrt(var), image.shape)
    noisy_image = image + image * noise
    # Clip values to be in the valid range [0, 1]
    noisy_image = np.clip(noisy_image, 0, 1)
    # Convert back to 8-bit image
    noisy_image = (noisy_image * 255).astype(np.uint8)
    return noisy_image

# Load an image
image = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)

# Add speckle noise
noisy_image = add_speckle_noise(image, mean=0, var=0.04)

# Display the original and noisy images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Image with Speckle Noise")
plt.imshow(noisy_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
