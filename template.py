import copy

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is an inverted version of the input image. That is to say each 
    pixel's grayscale value should be inverted relative to the maximum value of 255.
'''
def invert(image):
    return image


'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a blurred version of the input image. The blur function 
    uses a weighted kernel which is applied the pixels centered on 
    image[i][j]. The value in the kernel is multiplied by the corresponding
    pixels in the image and the eighted average is used as new_image[i][j].
'''
def blur(image):
    kernel = [
        [1, 1, 1],
        [1, 7, 1],
        [1, 1, 1],
    ]
    return image

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a vertically flipped version of the input image. 
'''
def flip(image):
    return image

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a 2x2 tiled version of the input image. The tile function
    will group pixels in groups of 4 and map each one to one of the 4 tiles
    based on their relative position in the group. That is to say in 
    [[1, 2],
     [3, 4]]
    the number 1 will be in the top left tile, 2 in the top right tile, 
    and so on. Because nearby pixels are similar this will create an image 
    which loops like 4 copies of the same image but slightly different.

    To make the transformation, consider 4 pixels in each iteration 
    of the loop and map them to the corresponding tiles. Each tile will be
    half the length and half the width of the input image.
'''
def tile(image):
    return image














