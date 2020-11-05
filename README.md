# JAVEC
Just another virtual environment creator

## Installation

Clone the repository

    git clone https://github.com/BartlomiejF/JAVEC

The code is based on Python standard library so no additional packages are required

## Usage

### No arguments
If you run main.py with no additional arguments:

    python3 /path/to/JAVEC/main.py

It will create virtual environment in current working directory with the same name as current working directory, but with dot in front (hidden file in Linux). To run the virtual environment run:

    source ./.virenvFolder/bin/activate

### -a
Running main.py with -a argument:

    python3 /path/to/JAVEC/main.py -a

In addition to creation of virtual environment it causes creation of script shell named ".activator.sh". Now activation of virtual environment will require running following code:

    source .activator.sh

### -g, --gitignore
Running main.py with -g argument:

    python3 /path/to/JAVEC/main.py -g

In addition to creation of virtual environment it causes creation of .gitignore file. The .gitignore file is a copy of gitignore_example provided in the repository. It was taken from [this repository](https://github.com/github/gitignore).

### --swap-gitignore \<path\>
It is possible to change the gitignore_example from this repository file with one you commonly use by using --swap-gitignore path:

    python3 /path/to/JAVEC/main.py --swap-gitignore /path/to/your/own/.gitignore

If used with -g argument the first action will be swapping gitignore_example and then creation of .gitignore in the current working directory.

### -i, --install \<packages\>
Install given packages. This argument will simply call the following command:

    /path/to/virtualenvironment/bin/python3 -m pip install <packages>

Moreover packages names will be added to requirements_javec.txt file.

## TODO
1. package the tool

## Further simplification
To avoid typing 

    python3 /path/to/JAVEC/main.py

Add an alias to your .bashrc or .bash_aliases by adding:

    alias javec="python3 /path/to/JAVEC/main.py"

then usage would look like:

    javec -a
    javec -g
    javec -a -g

or

    alias javec="python3 /path/to/JAVEC/main.py -a"

or 

    alias javec="python3 /path/to/JAVEC/main.py -g"

or 

    alias javec="python3 /path/to/JAVEC/main.py -a -g"
    

## Have fun!

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)