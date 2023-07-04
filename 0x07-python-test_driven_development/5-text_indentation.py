#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """texxt is pirinted after weo linkes of  '.', '?', and ':'.
    Args:
        text (string): string to be printed.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    charachter = 0
    while charachter < len(text) and text[charachter] == ' ':
        charachter += 1

    while charachter < len(text):
        print(text[charachter], end="")
        if text[charachter] == "\n" or text[charachter] in ".?:":
            if text[charachter] in ".?:":
                print("\n")
            charachter += 1
            while charachter < len(text) and text[charachter] == ' ':
                charachter += 1
            continue
        charachter += 1
