# Varun Shourie, CIS345, Tuesday/Thursday, 12:00PM-1:15PM, PE11

import cv2
from PIL import Image

filename = "my_img.jpg"

# Resizing the original image and overwriting it so it will not consume as much memory.
original_img = Image.open(filename)
new_img = original_img.resize((605, 454))
new_img.save(filename, "JPEG")

# Read in image object, create/position window, and display the resized picture waiting for keypress.
img = cv2.imread(filename)
cv2.namedWindow("My Front Yard")
cv2.moveWindow("My Front Yard", 0, 0)
cv2.imshow("My Front Yard", img)
cv2.waitKey(0)

# Creates 4 different versions of the original image to be shown to the user.
version1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
version2 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
version3 = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
version4 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Opens up the grayscale, CIE Lab, hue lightness saturation, and hue saturation value versions of my original BGR
# picture with the option to save the new versions if I press "s" only.
cv2.imshow("My Front Yard - Version 1", version1)
key = cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("BGR2GRAY_"+filename, version1)

cv2.imshow("My Front Yard - Version 2", version2)
key = cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("BGR2LAB_"+filename, version2)

cv2.imshow("My Front Yard - Version 3", version3)
key = cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("BGR2HLS_"+filename, version3)

cv2.imshow("My Front Yard - Version 4", version4)
key = cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("BGR2HSV_"+filename, version4)

cv2.destroyAllWindows()

# Objects used to create and reference a thumbnail version of my original BGR picture.
thumb_nail_size = (128, 128)
thumb_nail = "thumbnail_" + filename

# Attempts to save a thumbnail version of my original BGR picture to memory.
try:
    img = Image.open(filename)
    img.thumbnail(thumb_nail_size)
    img.save(thumb_nail, "JPEG")
except IOError:
    print(f"Cannot create thumbnail for {filename}.")
