'''
Comma Code
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
'''
spam = ['apples', 'bananas', 'tofu', 'cats']

def list_to_string(list):
    output_string = ''
    for index, item in enumerate(list):
        if index == len(list)-1:
            # last item
            output_string += f'{item}.'
        elif index == len(list)-2:
            # second last item
            output_string += f'{item} and '
        else:
            output_string += f'{item}, '
    print(output_string)



list_to_string(spam)
