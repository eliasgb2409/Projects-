"""pure Python implementation of image filters"""

import numpy as np
from PIL import Image #er dette lov her?


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image

    How it works:
        We iterate thorugh the different arrays and apply weights to the
        color channels in the right index according to the order: r, g, b

        When we have applied the weight we add the values together to
        give the color channels the same weighted value. 
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


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image

    How it works:
        Again we iterate thorugh the different arrays and apply weights to the
        color channels in the right index according to the order: r, g, b

        This time the weight is based on the values in sepia_matrix and color channel values.

        When we have applied the weight to the right color channels, there will be assigned
        a new red, green and blue value to the array in the position [i][j]. 

        We are also truncate the pixel-value to 255
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

            newRed = red * 0.393 + green * 0.769 + blue * 0.189  #kan bruke indekser 
            newGreen = red * 0.349 + green * 0.349 + blue * 0.349
            newBlue = red * 0.272 + green *  0.534 + blue * 0.131

            sepia_image[i][j] = (min(255,newRed), min(255,newGreen), min(255,newBlue))
     
    sepia_image = sepia_image.astype("uint8")
    #image = Image.fromarray(sepia_image)
    #image.save("sepia_image_python.jpg")
    #im = Image.open(r"sepia_image_python.jpg")
    #im.show()

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image
