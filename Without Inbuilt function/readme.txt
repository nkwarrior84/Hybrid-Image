numpy==1.16.0
opencv-python==4.0.0.21

Steps followed:
  (1) convert the input images to grayscale
  (2) align the input images (resulting in equal dimensions)
  (3) create two gaussian circles: one for the low-frequency content, and the other for the high-frequency content 
  (4) convert the input images to the frequency domain 
  (5) multiply the frequency-domain images by their respective gaussian circles (which removes low-frequency content in one, and high-frequency content in the other)
  (6) convert the frequency-domain images back into the spatial domain 
  (7) combine the spatial-domain images by doing an element-wise average




Low Pass Filter : left(2).png
Left Image Sigma : 10.0
Left Image Kernel Size : 25

High Pass Filter : right(2).png
Left Image Sigma : 10.0
Left Image Kernel Size : 25

Mix-in Ratio : 0.70

Scale Factor : 2.0