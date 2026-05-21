# Q1. Hidden Object Recovery
a. The object in the image is barely visible (in <img src="images\input\1-a.jpg.jpeg" \> and <img src="images\input\1-b.jpg.jpeg" \>). Why?
b. Explain how will you do and apply:
i. Recover the object clearly
ii. Make it suitable for edge detection

# 2. Noise Filtering
Task: 
a. Identify the noise in these 3 images (<img src="images\input\2-a.jpg.jpeg" \>, <img src="images\input\2-b.jpg.jpeg" \> and <img src="images\input\2-c.jpg.jpeg" \>)
i. Identify noise type
ii. Apply optimal filtering
iii. Justify your technique

# Q3. Object Extraction with Imperfect Mask
Task:
Apply techniques to extract the object? Explain How you did?
(in image <img src="images\input\3-a.jpg.jpeg" \> – Person, In image <img src="images\input\3-b.jpg.jpeg" \> suitcase)

# 4. Dark Image
The image suffers from:
• Uneven illumination (bright + dark regions)
• Loss of details in shadow areas
• The images are <img src="images\input\4-a.jpg.jpeg" \> and <img src="images\input\4-b.jpg.jpeg" \>
Task:
a. You are Asked to
i. Correct the illumination
ii. Enhance hidden details in dark regions
iii. Make the image suitable for further processing (edge detection /
segmentation)
iv. Justify your approach?

# Q5. Image Enhancement
 <img src="images\input\5-a.jpg.jpeg" \>, <img src="images\input\5-b.jpg.jpeg" \> and <img src="images\input\5-c.jpg.jpeg" \>
Task:
a. Explain why this image is degraded?
b. Restore the image as much as possible?
c. Enhance edges and fine details?
d. Make text or object readable?

# Q6. Edge Detection
Task:
The detected edges of an object are Broken / discontinuous, and Contain gaps and
noise <img src="images\input\6-a.jpg.jpeg" \>
a. Reconstruct continuous object boundaries
b. Remove false edges (noise)
c. Prepare the image for object detection or contour extraction
d. Explain the technique

# Q7. Analysis of Image Enhancement Techniques
Apply for given grayscale images representing different conditions.
<img src="images\input\A.jpeg" \> <img src="images\input\B.jpeg" \> <img src="images\input\C.jpeg" \>
Tasks:
a) Apply the following point processing techniques:
• Image Negative
• Log Transformation
• Gamma Correction (use at least two different gamma values)
• Contrast Stretching
b) For each technique:
• Display the original and processed images
• Plot the corresponding histograms
c) Analyze the results and explain:
• How each technique affects image intensity distribution
• Which method is most suitable for each type of image and why

# Q8. Histogram Equalization: Theory and Implementation
Tasks:
a) Starting from the definition of histogram, derive the histogram equalization transformation using the cumulative distribution function (CDF).
b) Consider the given small 8-bit grayscale image. <img src="images\input\8bit.png" \>
• Compute the histogram
• Calculate probability distribution
• Determine the CDF
• Obtain the equalized intensity values manually
c) Implement histogram equalization using:
• A built-in function
• A manual algorithm (without using library functions)
d) Compare and discuss the results in terms of contrast improvement