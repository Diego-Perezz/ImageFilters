import copy

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is an inverted version of the input image. That is to say each 
    pixel's grayscale value should be inverted relative to the maximum value of 255.
'''
def invert(image):
    nimage = image.copy() 
    for row in range(0,len(image)):
        for col in range(0,(len(image[row]))):
            nimage[row][col] = (255 - image[row][col])    
    return nimage


'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a blurred version of the input image. The blur function 
    uses a weighted kernel which is applied the pixels centered on 
    image[i][j]. The value in the kernel is multiplied by the corresponding
    pixels in the image and the eighted average is used as new_image[i][j].
'''
def blur(image):
    newimage = []
    kernel = [
        [1, 1, 1],
        [1, 7, 1],
        [1, 1, 1],
    ]

    for y in range(0,len(image)):
        col = []
        for x in range(0,len(image[y])):

            if y == 0 or y == (len(image)-1) or x == 0 or x == (len(image[y])-1):
                weighted_average = 0 
                col.append(weighted_average)

            else:
                
                weighted_sum = (
                    image[y-1][x-1] * kernel[0][0]   +   image[y-1][ x ] * kernel[0][1]   +   image[y-1][x+1] * kernel[0][2]   +   
                    image[ y ][x-1] * kernel[1][0]   +   image[ y ][ x ] * kernel[1][1]   +   image[ y ][x+1] * kernel[1][2]   +
                    image[y+1][x-1] * kernel[2][0]   +   image[y+1][ x ] * kernel[2][1]   +   image[y+1][x+1] * kernel[2][2] 
                    )
                
                total_weights = (
                    kernel[0][0]   +   kernel[0][1]   +   kernel[0][2]   +
                    kernel[1][0]   +   kernel[1][1]   +   kernel[1][2]   +
                    kernel[2][0]   +   kernel[2][1]   +   kernel[2][2] 
                    )
                
                weighted_average = weighted_sum // total_weights
                col.append(weighted_average)
        newimage.append(col)
    return newimage

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a vertically flipped version of the input image. 
'''
def flip(image):
    newimage = (image[::-1])
    return newimage

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



def getTile(list):
    A_Tile=[]
    for rowindex in range(0 , (len(list)) , 2):
        unaFila = []
        for colindex in range(0 , (len(list[rowindex])) , 2):
            promedioDe4Pixels = ( (list[  rowindex  ][  colindex  ]) //4 + (list[1 + rowindex][  colindex  ]) //4 +  
                                  (list[  rowindex  ][1 + colindex]) //4 + (list[1 + rowindex][1 + colindex]) //4 ) 
            unaFila.append( promedioDe4Pixels )
        A_Tile.append(unaFila)
    return A_Tile


def place4Tiles(tile):
    twoTiles = tile + tile
    fourTiles = []
    for fila in twoTiles:
        fourTiles.append( fila + fila)
    return fourTiles


def tile(image):
    newimage =place4Tiles(getTile(image))
    return newimage 





