# Wine-Extraction-

<h3> Installation </h3>

The main packages used are opencv (computer vision for processing images) and pytesseract(a wrapper for the tesseract OCR engine) but also make sure you can run python3. 


<pre>
  <code>
  pip install opencv-python
  pip install pytesseract
  </code>
</pre>

<h3> Running the OCR </h3> 

First, clone or download the repository. 

<pre>
  <code>
  git clone https://github.com/LouieChen24/Wine-Extraction-.git
  </code>
</pre>

Unzip the file and open up the terminal and go to the directory. 

Add image files and run the bash script (which runs all images with the extension .jpg)


<pre>
  <code>
  chmod +x all_images.sh
  ./all_images.sh
  </code>
</pre>

This gives you 3 outputs: a .png which shows the bounding boxes of each image called [img_name].png, two texts files: data (bounding box location, line number, etc) called [img_name].txt and a text output (output of the text from the image) called [img_name]text_only.txt 

