# Hybrid-Image

Algorithm:

Step 1: Compute the cross-correlation of image-1 with image-2 (often called a kernel) that returns an image of the same dimensions as the input image.
Step 2: Determine the 2D convolution between image-1 and image-2. 2D convolution can be visualized as cross-correlation between image-1 and flipped image-2.
Step 3: Construct a gaussian blur filter for image-2 such that convolving it with image-1 results in a gaussian-blurred image.
Step 4: Create a low-pass filter that suppresses the higher frequency components of a given image.
Step 5: Create a high-pass filter that suppresses the lower frequency components of a given image.
Step 6: Build an integration function that adds the two images to create the desired hybrid image based on user-defined parameters


# Reference:

(1) https://github.com/rhthomas/hybrid-images
(2) https://github.com/namangoy/computer-vision/tree/master/Hybrid_Images
