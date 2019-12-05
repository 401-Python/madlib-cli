## Lab 03: MadLib

### Author: Alvian Joseph

### Links and Resources
* [PR]()
* [![Build Status]()
* [front end]()

### Tasks
Keeping in mind the concept of Single Responsibility Principle, build a command line tool which will perform the following:
Print a welcome message to the user, explaining the Madlib process and command line interactions
Read a template Madlib file (Example), and parse that file into usable parts.
You need to decide what components of this file are useful, and how to break those useful pieces apart
Once you know what parts of the template need user input, such as Adjective, prompt the user to submit a series of words to fit each of the required components of the Madlib template.
With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
Write the completed template (Example)to a new file on your file system (in the repo).

### Modules
#### madlib.py
  #### methods
  * ```greeting()```
    Greet the user and provide instructions.  

  * ```read_file(path)```
    Read a file path and return its contents as a string  
  
  * ```write_file(path)```
    Write a file back to the given path


  * ```get_keys(format_string)```
    The default text file contains several words classes
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

   * ```remove_word_classes(format_string)```
     Removes the word classes (anything inside a set of curly braces) from the default text file  

    * ```get_responses(prompts)```
     This function accetps an array of strings (generated from the get_keys function)
    And for each string, prompts the user for a word, then appends that word
    to a list to be added to the output txt file  

    * ```create_madlib(default)```
      This function combines all of our helper functions to produce the final
      madlib story.
      First we get the prompts by calling get keys on the default.txt file
      Next we santize the txt by removing all of the keys
      Next we gather the user responses and store them in a variable
      Lastly we run the .format() method on our sanitized text, we pass
      in the responses which will be added to the story, store it in a variable
      and return it




### Testing
  pytest
  ptw
  

