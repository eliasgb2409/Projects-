from instapy.numba_filters import numba_color2gray, numba_color2sepia

import numpy.testing as nt
import numpy as np 

def test_color2gray(image, reference_gray):
    """
    In this test we will take out three pixels from the original "image"
    and compare its RGB values to the "grayscale image".

    The test will also check if the result has the right shape, type and 
    if the RGB values in the graycale image is uniform. 
    """

    # run color2gray
    grayImg_array = numba_color2gray(image)

    # check that the result has the right shape, type
    assert grayImg_array.shape == image.shape
    assert grayImg_array.dtype == "uint8"

    np.testing.assert_allclose(grayImg_array, reference_gray)

def test_color2sepia(image, reference_sepia):
    
    # run color2sepia
    sepiaImg_array = numba_color2sepia(image)

    # check that the result has the right shape, type
    assert sepiaImg_array.shape == image.shape
    assert sepiaImg_array.dtype == "uint8"

    np.testing.assert_allclose(sepiaImg_array, reference_sepia)

