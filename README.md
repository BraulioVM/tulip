# tulip
[![Build Status](https://travis-ci.org/BraulioVM/tulip.svg)](https://travis-ci.org/BraulioVM/tulip)
> Display simple images in your terminal

![tulip-capture](https://cloud.githubusercontent.com/assets/715372/12051538/97241142-af05-11e5-8285-0d18eeded333.png)

## Installation
Clone the repository and execute 

````
python setup.py install
````

Make sure you are using python3

## How to use it
````
Usage: tulip [OPTIONS] IMAGE_PATH

Options:
  --width INTEGER                 Width (in characters) of the image shell
                                  representation (defaults to the current
                                  shell width)
  -wp, --width-percentage FLOAT   Percentage of the shell width that will be
                                  used to display the image (will be ignored
                                  if --width is specified)
  --height INTEGER                Height (in characters) of the image shell
                                  representation (defaults to the current
                                  shell height)
  -hp, --height-percentage FLOAT  Percentage of the shell height that will be
                                  used to display the image (will be ignored
                                  if --height is specified)
  --just-ascii                    Display image using just ascii characters
  --help                          Show this message and exit.

````

## Troubleshooting
Submit an issue if something is not working as you expect. I will happily solve the problem as soon as I can :muscle: