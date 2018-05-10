from PIL import Image
import sys 
import cv2
import pytesseract 

# Get the image from command line
image_name = sys.argv[1]
img_id = image_name[:-4]
output_name = img_id + ".txt"

file_name = cv2.imread(image_name)

# Create data file which lists bounding box coordinates, confidence internval, and line number
text = pytesseract.image_to_data(file_name)
f = open(output_name, "w+")
f.write(text)
f.close() 

# Convert the image text into a text file 
text_only  = pytesseract.image_to_string(file_name)
output_name = img_id + "text_only.txt"
f = open(output_name, "w+")
f.write(text_only)
f.close()

