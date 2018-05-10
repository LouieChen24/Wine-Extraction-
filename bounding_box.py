import os
import sys
import cv2
import pytesseract

# Take command line inputs for filename and output 
file_name = sys.argv[1]
img_id = file_name[:-4]
output_name = img_id + ".png"
print(output_name)

# read the image and get the dimensions
img = cv2.imread(file_name)
h, w, _ = img.shape # assumes color image

# run tesseract, returning the bounding boxes
boxes = pytesseract.image_to_boxes(img) # also include any config options you use

# draw the bounding boxes on the image
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

# show annotated image and wait for keypress
cv2.imwrite(output_name, img)
# this outputs it to screen  cv2.imshow(file_name, img)
cv2.waitKey(0)

