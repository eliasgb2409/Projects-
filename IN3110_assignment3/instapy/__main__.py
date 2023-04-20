"""This file is used when invoked as `python -m instapy`"""

#def main():
    #from .cli import main
    #main()

#For some reason not working when trying to call "instapy <arguments>"". I dont know if this a issue with just my pc. 

if __name__ == "__main__":
    from .cli import main

    main()
