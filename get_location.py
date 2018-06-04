from io import StringIO
import sys
import math
import cv2
import pytesseract 
import pandas as pd

image_name = sys.argv[1]
img_id = image_name[:-4]

file_name = cv2.imread(image_name)

text = pytesseract.image_to_data(file_name)
location = StringIO()
location.write(text)
location.seek(0)
data = pd.read_csv(location, sep='\t', header=None)

# data[11] = text, #data[7] = top, #data[6] = left
# Function to check if string can turn into a float 
def isfloat(value):
    try: 
       float(value)
       return True
    except ValueError:
       return False

def build_array(value):
    arr = []
    value = int(value) - 15
    for i in range(0,30):
        arr.append(str(value + i))
    return arr

count_floats = 0
counter = 0
dict = {}
for number in data[11]:
    #NaN is considered float, so filter those out 
    if type(number) is str:
        # Make sure string can turn into a float and is not an int
        if (isfloat(number)) and not number.isdigit():
            count_floats += 1
            dict[number] = data[7][counter]
    counter += 1	
#print(count_floats)

if count_floats > 3:
    print("True")
    names = []
    bottle = []
    case = []
    itr = 0
    for key,value in dict.items():
        wine_name = ""
        arr = build_array(value)
        x = data.loc[data[7].isin(arr)]
        # Sort by left margin
        x.sort_values(6)
        print(x)
        priced = False
        for te in x[11]:
             break
             if type(te) is str:
                 if (isfloat(te)) and not te.isdigit():
                     if len(bottle) == itr + 1:
                         case.append(te)
                     else:
                         bottle.append(te)
                         priced  = True
                 elif not priced:
                     wine_name = wine_name + te + " "
        names.append(wine_name)
else:
    print("FALSE")

