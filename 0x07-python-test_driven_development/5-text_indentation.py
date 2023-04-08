#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """Splits a text into lines along "?", ":", "." followed by 2 new lines"""

    # check if text is a string
    if type(text) is not str:
        raise TypeError("text must be a string")

    # initialize flag to 0
    flag = 0

    # loop through each character in text
    for a in text:

        # if flag is 0
        if flag == 0:
            # if character is a space, skip it
            if a == ' ':
                continue
            else:
                # if character is not a space, set flag to 1
                flag = 1

        # if flag is 1
        if flag == 1:
            # if character is "?" or "." or ":"
            if a == '?' or a == '.' or a == ':':
                # print the character, followed by two newlines
                print(a)
                print()
                # set flag back to 0
                flag = 0
            else:
                # print the character
                print(a, end="")
