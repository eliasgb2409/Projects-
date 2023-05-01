"""numba-optimized filters"""
from numba import jit
import numpy as np
from PIL import Image #er dette lov her?



@jit
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    
    Same logic as in the functions python_filters.py, this time we use @jit
    """
    gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform
    height = len(image)  
    width = len(image[0])

    for i in range(height):
        for j in range(width): 
            red = image[i][j][0]*0.21
            green = image[i][j][1]*0.72
            blue = image[i][j][2]*0.07
            gray_image[i][j] = red+green+blue

    gray_image = gray_image.astype("uint8")

    return gray_image


@jit
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image

    Same logic as in the functions python_filters.py, this time we use @jit

    """
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix

    sepia_matrix = [
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.349, 0.349],
    [ 0.272, 0.534, 0.131],
    ]

    height = len(image)  
    width = len(image[0])

    for i in range(height): 
        for j in range(width): 
            red = image[i][j][0]
            green = image[i][j][1]
            blue = image[i][j][2]
            
            newRed = red * 0.393 + green * 0.769 + blue * 0.189
            newGreen = red * 0.349 + green * 0.349 + blue * 0.349
            newBlue = red * 0.272 + green *  0.534 + blue * 0.131

            sepia_image[i][j] = (min(255,newRed), min(255,newGreen), min(255,newBlue))
     
    sepia_image = sepia_image.astype("uint8")

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image