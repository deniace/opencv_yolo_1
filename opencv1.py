import cv2
import matplotlib.pyplot as plt

# read image as grayscale
cb_img = cv2.imread('image/checkerboard_18x18.png', 0)
print(cb_img)

# print the size of image
print("Image size (H, W) is : ", cb_img.shape)

# print data type of image
print("Data type image is : ", cb_img.dtype)

# Display image using matplotlib
plt.imshow(cb_img)
plt.show()

# set color map to gray scale for proper rendering
plt.imshow(cb_img, cmap="gray")
plt.show()