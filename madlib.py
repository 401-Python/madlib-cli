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


def get_keys(format_string):
    """
    The text file contains several words classes
    surrounded by curly braces.
    This function will use those curly braces to
    create keys for each of them.
    First, to find out how many keys I need I run a count
    on the input string for all the open curly braces
    Then, I form the keys by finding the index of
    each set of curlys and slicing out substring
    of each.
    The end result should be an array of each word contained
    in two curly braces
    """
    keys = []
    end = 0

    word_count = format_string.count('{')
    for i in range(word_count):
        # +1 so we get the first char inside the curly
        start = format_string.find('{', end) + 1
        end = format_string.find('}', start)
        key = format_string[start:end]
        keys.append(key)
    return keys


def remove_word_classes(format_string):
    """
    Removes the word classes (anything inside a set of curly braces) 
    from the default text file
    """
    regex = r"\{.*?\}"
    output = re.sub(regex, '{}', format_string)
    return output


def get_responses(prompts):

    """
    This function accetps an array of strings (generated from the get_keys function)
    And for each string, prompts the user for a word, then appends that word
    to a list to be added to the output txt file
    
    """
    responses = []
    
    for prompt in prompts:
        response = input(f'Enter {prompt}: ')
        responses.append(response)
    return responses

def create_madlib(default):
    """
      This function combines all of our helper functions to produce the final
      madlib story.
      First we get the prompts by calling get keys on the default.txt file
      Next we santize the txt by removing all of the keys
      Next we gather the user responses and store them in a variable
      Lastly we run the .format() method on our sanitized text, we pass
      in the responses which will be added to the story, store it in a variable
      and return it
      
    """
    prompts = get_keys(default)
    sanitized = remove_word_classes(default)
    responses = get_responses(prompts)
    madlib = sanitized.format(*responses)
    return madlib


if __name__ == "__main__":
    greeting()
    default = read_file('default.txt')
    story = create_madlib(default)
    write_file('madlib.txt', story)
