"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from . import io
from instapy import get_filter

#Changed the paramter name file to file_name and filter to filter_name
def run_filter(
    file_name: str,
    out_file: str = None,
    implementation: str = "python",
    filter_name: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = Image.open(file_name)
    if scale != 1:
        # Resize image, if needed
        # My assumtion with scaling the image is that if the user writes in the argument e.g. "-sc 2"  , the image will scale with the following:
        image = image.resize((image.width // 2, image.height // 2))

    # Apply the filter
    pixels = np.asarray(image)#io.read_image(image.filename)
    filterType = get_filter(filter_name, implementation)      
    filtered = filterType(pixels)
    if out_file:
        # save the file
        filtered = io.write_image(filtered, out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    all_implementations = {'python': 'python',
                    'numpy': 'numpy',
                    'numba': 'numba'}

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    # Add required arguments
   
    #Options: 
    parser.add_argument("-o", "--out", default= None, help="The output filename")
    parser.add_argument("-g", "--gray", default="color2gray", action="store_const", const="color2gray",help="Select gray filter")
    parser.add_argument("-se", "--sepia",action="store_const", const="color2sepia",help="Select sepia filter")
    parser.add_argument("-sc", "--scale", default= 1, type=int, help="Scale factor to resize image")
    parser.add_argument("-i ", "--implementation", choices=all_implementations, default="python", help="The implementation")
 
    # parse arguments and call run_filter
    args = parser.parse_args()

    print(args.file)
    print(args.out)
    print(args.gray)
    print(args.sepia)
    print(args.scale)
    print(args.implementation)

    if args.sepia:
        run_filter(args.file, args.out, args.implementation, args.sepia, args.scale)
    else:
        run_filter(args.file, args.out, args.implementation, args.gray, args.scale)
   
    
    
