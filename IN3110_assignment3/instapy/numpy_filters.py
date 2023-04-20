"""numpy implementation of image filters"""

from typing import Optional
import numpy as np

from PIL import Image #er dette lov her?



def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image

    How it works:
        We slice the different arrays of the numpy array and apply weights to the
        color channels in the right index according to the order: r, g, b

        When we have applied the weight we add the values together to
        give the color channels the same weighted value. 
    """


    gray_image = np.empty_like(image)
  
    red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]
    #gray_image = [0.21 * red, 0.72 * green, 0.07 * blue]

    gray_image[:,:,0] = red * 0.21 + green * 0.72 + blue * 0.07
    gray_image[:,:,1] = red * 0.21 + green * 0.72 + blue * 0.07
    gray_image[:,:,2] = red * 0.21 + green * 0.72 + blue * 0.07
    
    # Return image (make sure it's the right type!)
    gray_image = gray_image.astype("uint8")

    return gray_image 


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image

    How it works:

        Firstly we slice the arrays in the image for each r,g,b color channel.

        Then we apply the weighted values to the color channels with einsum. 
        The weights are based on the values from the sepia_matrix.
        
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_image = np.empty_like(image)

    red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]
    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    sepia_matrix = [
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.349, 0.349],
    [ 0.272, 0.534, 0.131],
    ]

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter    

    sepia_image = np.einsum('ij,klj->kli',sepia_matrix,image[:,:], optimize='greedy')

    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255

    height = len(image)  
    width = len(image[0])

    for i in range(height): 
        for j in range(width): 
            red = sepia_image[i][j][0]
            green = sepia_image[i][j][1]
            blue = sepia_image[i][j][2]
            sepia_image[i][j] = (min(255,red), min(255,green), min(255,blue))
     
    sepia_image = sepia_image.astype("uint8")
   
    # Return image (make sure it's the right type!)
    return sepia_image
