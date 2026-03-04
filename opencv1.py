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

# read image as color
coke_img = cv2.imread('image/coca-cola-logo.png', 1)

# print the size of image
print("Image size (H, W, C) is : ", coke_img.shape)

# print datatype of image
print("Data type of image", coke_img.dtype)

plt.imshow(coke_img)
plt.show()  

# merubah skema warna dari BGR ke RGB
coke_img_rgb = cv2.cvtColor(coke_img, cv2.COLOR_BGR2RGB)
plt.imshow(coke_img_rgb)    
plt.show()
