import sys
import cv2
import numpy as np

def cross_correlation_2d(img, kernel):

    m, n = kernel.shape
    new_image = np.empty(img.shape)

    if len(img.shape) == 2:
        # If the image is a gray-scale image
        image_height, image_width = img.shape
        pseudo_image = np.zeros((image_height + m - 1, image_width + n - 1))
        pseudo_image[(m - 1) / 2:image_height + (m - 1) / 2, (n - 1) / 2:image_width + (n - 1) / 2] = img
        for i in range(image_width):
            for j in range(image_height):
                temp = kernel * pseudo_image[j:j + m, i:i + n]
                new_image[j, i] = temp.sum()

    elif len(img.shape) == 3:
        # If the image is an rgb image
        image_height, image_width, color_axis = img.shape
        pseudo_image = np.zeros((image_height + m - 1, image_width + n - 1, color_axis))
        pseudo_image[(m - 1) / 2:image_height + (m - 1) / 2, (n - 1) / 2:image_width + (n - 1) / 2] = img
        for i in range(image_width):
            for j in range(image_height):
                for k in range(color_axis):
                    temp = kernel * pseudo_image[:, :, k][j:j + m, i:i + n]
                    new_image[:, :, k][j, i] = temp.sum()

    return (new_image)

    

def convolve_2d(img, kernel):

    flipped_image = np.flip(kernel, (0, 1))
    return cross_correlation_2d(img, flipped_image)


def gaussian_blur_kernel_2d(sigma, height, width):

    pseudo_image = np.zeros((height, width))

    c_x = int(height/2)
    c_y = int(width/2)
    const = 1/(2*np.pi*(sigma**2))
    exp_den = 2*(sigma**2)

    for x in range(height):
        for y in range(width):
            exp_num = ((x - c_x)**2) + ((y - c_y)**2)
            exponent = (-1)*exp_num/float(exp_den)
            pseudo_image[x, y] = const * np.exp(exponent)

    gaussian_blur = pseudo_image/pseudo_image.sum()
    return gaussian_blur


def low_pass(img, sigma, size):
   
    kernel = gaussian_blur_kernel_2d(sigma, size, size)
    low_pass_image = convolve_2d(img, kernel)
    return low_pass_image

   
def high_pass(img, sigma, size):
   
    high_pass_image = img - low_pass(img, sigma, size)
    return high_pass_image
   

def create_hybrid_image(img1, img2, sigma1, size1, high_low1, sigma2, size2, high_low2, mixin_ratio, scale_factor):
 
    high_low1 = high_low1.lower()
    high_low2 = high_low2.lower()

    if img1.dtype == np.uint8:
        img1 = img1.astype(np.float32) / 255.0
        img2 = img2.astype(np.float32) / 255.0

    if high_low1 == 'low':
        img1 = low_pass(img1, sigma1, size1)
    else:
        img1 = high_pass(img1, sigma1, size1)

    if high_low2 == 'low':
        img2 = low_pass(img2, sigma2, size2)
    else:
        img2 = high_pass(img2, sigma2, size2)

    img1 *=  (1 - mixin_ratio)
    img2 *= mixin_ratio
    hybrid_img = (img1 + img2) * scale_factor
    return (hybrid_img * 255).clip(0, 255).astype(np.uint8)


if __name__ == "__main__":
   image_1 = ndimage.imread("1.png", flatten=True)
   image_2 = ndimage.imread("2.png", flatten=True)

   hybrid = create_hybrid_image()
   misc.imsave("result.png", numpy.real(hybrid))