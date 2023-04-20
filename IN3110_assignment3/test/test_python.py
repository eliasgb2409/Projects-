from instapy.python_filters import python_color2gray, python_color2sepia
from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
from instapy.numba_filters import numba_color2gray, numba_color2sepia

import numpy as np 


def test_color2gray(image):
    """
    In this test we will take out three pixels from the original "image"
    and compare its RGB values to the "grayscale image".

    The test will also check if the result has the right shape, type and 
    if the RGB values in the graycale image is uniform. 
    """

    # run color2gray
    pixels = np.asarray(image)
    grayImg_array = python_color2gray(pixels)

    # check that the result has the right shape, type
    assert grayImg_array.shape == pixels.shape
    assert grayImg_array.dtype == "uint8"

    #Upper left corner
    red = pixels[0][0][0] * 0.21
    green = pixels[0][0][1] * 0.72
    blue = pixels[0][0][2] * 0.07

    #Upper right corner
    red2 = pixels[0][-1][0] * 0.21
    green2 = pixels[0][-1][1] * 0.72
    blue2 = pixels[0][-1][2] * 0.07

    #Bottom left corner
    red3 = pixels[-1][0][0] * 0.21
    green3 = pixels[-1][0][1] * 0.72
    blue3 = pixels[-1][0][2] * 0.07

    #Bottom right corner 
    red4 = pixels[-1][-1][0] * 0.21
    green4 = pixels[-1][-1][1] * 0.72
    blue4 = pixels[-1][-1][2] * 0.07

    sum1 = red + green + blue
    sum2 = red2 + green2 + blue2
    sum3 = red3 + green3 + blue3
    sum4 = red4 + green4 + blue4

    sum1 = sum1.astype("uint8")
    sum2 = sum2.astype("uint8")
    sum3 = sum3.astype("uint8")
    sum4 = sum4.astype("uint8")

    #Check pixels from grayscale image and see if they are of the right weighted value 
    assert grayImg_array[0][0][0] == sum1 
    assert grayImg_array[0][-1][0] == sum2 
    assert all(grayImg_array[-1][0] == sum3)
    assert grayImg_array[-1][-1][0] == sum4

    # assert uniform r,g,b values  
    h = len(grayImg_array)  
    w = len(grayImg_array[0])
    for i in range(h): 
        for j in range(w):
            assert all(grayImg_array[i][j][:-1] == grayImg_array[i][j][1:])
    
    numpyGray_array = numpy_color2gray(pixels)
    numbaGray_array = numba_color2gray(pixels)

    np.testing.assert_allclose(grayImg_array, numpyGray_array)
    np.testing.assert_allclose(grayImg_array, numbaGray_array)



def test_color2sepia(image):
    """
    In this test we will take out four pixels from the original "image"
    and compare its RGB values to the "sepia image".

    The test will also check if the result has the right shape, type and 
    if the RGB values in the sepia image is correct according to the sepia matrix.     
    """
    # run color2sepia
    pixels = np.asarray(image)
    sepiaImg_array = python_color2sepia(pixels)

    # check that the result has the right shape, type
    assert sepiaImg_array.shape == pixels.shape
    assert sepiaImg_array.dtype == "uint8"


    # verify some individual pixel samples
    # according to the sepia matrix

    #Upper left corner
    red1 = pixels[0][0][0]
    green1 = pixels[0][0][1]
    blue1 = pixels[0][0][2]

    sumRed = red1 * 0.393 + green1 * 0.769 + blue1 * 0.189
    sumRed = min(255, sumRed).astype("uint8")

    sumGreen = red1 * 0.349 + green1 * 0.349 + blue1 * 0.349
    sumGreen = min(255, sumGreen).astype("uint8")

    sumBlue = red1 * 0.272 + green1 * 0.534 + blue1 * 0.131
    sumBlue = min(255, sumBlue).astype("uint8")

    assert sepiaImg_array[0][0][0] == sumRed
    assert sepiaImg_array[0][0][1] == sumGreen
    assert sepiaImg_array[0][0][2] == sumBlue

    #Upper right corner
    red2 = pixels[0][-1][0]
    green2 = pixels[0][-1][1]
    blue2 = pixels[0][-1][2]

    sumRed2 = red2 * 0.393 + green2 * 0.769 + blue2 * 0.189
    sumRed2 = min(255, sumRed2).astype("uint8") 
    
    sumGreen2 = red2 * 0.349 + green2 * 0.349 + blue2 * 0.349
    sumGreen2 = min(255, sumGreen2).astype("uint8")

    sumBlue2 = red2 * 0.272 + green2 * 0.534 + blue2 * 0.131
    sumBlue2 = min(255, sumBlue2).astype("uint8")

    assert sepiaImg_array[0][-1][0] == sumRed2
    assert sepiaImg_array[0][-1][1] == sumGreen2
    assert sepiaImg_array[0][-1][2] == sumBlue2
    
    #Bottom left corner:
    red3 = pixels[-1][0][0]
    green3 = pixels[-1][0][1]
    blue3 = pixels[-1][0][2]

    sumRed3 = red3 * 0.393 + green3 * 0.769 + blue3 * 0.189
    sumRed3 = min(255, sumRed3).astype("uint8")

    sumGreen3 = red3 * 0.349 + green3 * 0.349 + blue3 * 0.349
    sumGreen3 = min(255, sumGreen3).astype("uint8")

    sumBlue3 = red3 * 0.272 + green3 * 0.534 + blue3 * 0.131
    sumBlue3 = min(255, sumBlue3).astype("uint8")

    assert sepiaImg_array[-1][0][0] == sumRed3
    assert sepiaImg_array[-1][0][1] == sumGreen3
    assert sepiaImg_array[-1][0][2] == sumBlue3

    #Bottom right corner 
    red4 = pixels[-1][-1][0]
    green4 = pixels[-1][-1][1]
    blue4 = pixels[-1][-1][2]

    sumRed4 = red4 * 0.393 + green4 * 0.769 + blue4 * 0.189
    sumRed4 = min(255, sumRed4).astype("uint8")

    sumGreen4 = red4 * 0.349 + green4 * 0.349 + blue4 * 0.349
    sumGreen4 = min(255, sumGreen4).astype("uint8")

    sumBlue4 = red4 * 0.272 + green4 * 0.534 + blue4 * 0.131
    sumBlue4 = min(255, sumBlue4).astype("uint8")

    assert sepiaImg_array[-1][-1][0] == sumRed4
    assert sepiaImg_array[-1][-1][1] == sumGreen4
    assert sepiaImg_array[-1][-1][2] == sumBlue4

    numpy_sepia = numpy_color2sepia(pixels)
    numba_sepia = numba_color2sepia(pixels)

    np.testing.assert_allclose(sepiaImg_array, numpy_sepia)
    np.testing.assert_allclose(sepiaImg_array, numba_sepia)
