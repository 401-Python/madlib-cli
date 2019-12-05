"""
Mad Libs
The user is prompted to input random words which
will be used to form a story with a default text file
"""

import re


def greeting():
    """Greet the user and provide instructions."""
    print("Welcome to Madlib! You'll be prompted to come up with")
    print(" different words to customize your story, once you're done")
    print(" I'll show you how it turned out!")


def read_file(path):
    """Read path and return the data as a string."""
    with open(path, 'r') as rf:
        return rf.read()


def write_file(path, out):
    """Write a file back to the given path."""
    with open(path, 'w') as wf:
        return wf.write(out)


