











# if __name__ == "__main__":
#     greeting()
#     default = read_file('default.txt')
#     story = output_story(default)
#     write_file('madlib_complete.txt', story)


menu_template = '{} and {} with a side of {} please'

foods = ['ham', 'eggs', 'bacon']

# format expects multiple arguments vs. a list
# so using the "splat" operator aka *
# will "unpack" the list into individual arguments
formatted = menu_template.format(*foods)

print(formatted)


key_word_template = '{num1} score and {num2} years ago'

# btw - can also use keyword arguments to with format
formatted_with_key_words = key_word_template.format(num1=4, num2=7)

print(formatted_with_key_words)