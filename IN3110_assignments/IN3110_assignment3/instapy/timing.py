"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""
import time
import instapy
from . import io
from typing import Callable
import numpy as np
from PIL import Image
from instapy import get_filter

def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    #Start time
    timeStart = time.time()
    for i in range(calls):
        # run the filter function `calls` times
        filter_function(*arguments)
    #End time
    timeEnd= time.time()

    total = timeEnd - timeStart
    averageTime = total/calls
    
    # return the _average_ time of one call
    return float(averageTime)
    

def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use

    My assumtion with this task is that I create a file and write the report results to that file.
    The file is of the name timing-report.txt - I hope this works with your computer as well.
    If it turns out to not work with writing the file, please comment out the lines containing
    file-writing and such. 
    """
    timing_report = open("instapy/timing-report.txt", "w")
    # load the image
    image = np.asarray(Image.open(filename))
    img = Image.open(filename)
    #Show what image being used:
    print(f" \nShowing image being used...  \n")
    io.display(image)
    
    # print the image name, width, height
    print(f"Timing performed using {filename}: {img.width} x {img.height}\n") #må egt være: print("Timing performed using ", image.name,": ", image.width, image.height) 
    timing_report.write(f"Timing performed using {filename}: {str(img.width)} x {str(img.height)} \n")
    # iterate through the filters
    filter_names = ["color2gray", "color2sepia"]  
    for filter_name in filter_names:
        # get the reference filter function
        reference_filter = get_filter(filter_name, "python")
        # time the reference implementation
        reference_time = time_one(reference_filter,image) #Kalle på time_one
        print(
            f"\nReference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=}) \n"
        )
        timing_report.write(f"\nReference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=}) \n")
        # iterate through the implementations
        implementations = ["numpy", "numba"]  
        for implementation in implementations:
            filter = get_filter(filter_name, implementation)
            # time the filter
            filter_time = time_one(filter,image)
            # compare the reference time to the optimized time
            speedup = reference_time/filter_time
            print(
                f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)"
            )
            timing_report.write(f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)\n")

    timing_report.close()
    
if __name__ == "__main__":
    # run as `python -m instapy.timing`
    make_reports()
