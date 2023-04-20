<h1>Instapy</h1>

Instapy is a Python package turning your image of choice into a dramatic grayscale or nostalgic sepia image.



<h3>Installation</h3>

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the instapy package. 

```bash
python3 -m pip install .
```


<h3>Usage</h3>

Installing the package ensures that its functions and modules are added to the python path, allowing you to run e.g.:

```python
from instapy.python_filters import python_color2gray
```

You can use a commando-line interface to pass arguments to the ```instapy``` filter functions. The commando-line
interface can be called using:

```bash
# option 1
python3 -m instapy <arguments>
# or option 2
instapy <arguments>
```

For timing our filter implementations, you can execute: 

```bash
python3 -m instapy.timing
```

This will show the image being used, including its dimensions, and will save a report **```timing-report.txt```** that 
gives the runtimes of each implementation compared against each other. 

Lastly, instapy´s unit tests perform a sanity check on the return values, checking that the filter functions return numpy
arrays with the expected shape and dtype. Further, they check that the filters have been applied correctly to a few selected pixels.
It also verify that your different filter functions produce the same results as each other.


You can check that your tests pass by using the testing framework ```pytest```.


<h3>Contributing</h3>

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


<h3>License</h3>

[MIT](https://choosealicense.com/licenses/mit/)
