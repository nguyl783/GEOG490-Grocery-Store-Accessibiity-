"""
# CIS 122 Fall 2020 Assignment 6
# Author: Lauren Nguyen
# Partner:
# Description: Creating a shared code file
"""

def pad_string(data, size, direction = 'left padded', character = ' '):
    if len(data) > size:
        return data
""" Adding padding to a string

Args:
   data (str): data to be formatted
   size (int/float): size of the format space
   direction (str): left padded or right padded (defaulted to left pad)
   character (str): defaulted to single space

   Returns:
      Prints data to be formatted if length of data is greater than size of format space 
"""

def pad_left(data, size, character = ' '):
    pad_string(data, size, direction = 'left padded', character = ' ')
    result = data
    if len(data) < size:
        pad_size = size - len(data)
        result = character * pad_size + data
    return result
""" Adding padding to left of a string

Args:
   data (int/float): data to be formatted
   size (int/float): size of the format space
   character (str): defaulted to single space

   Returns:
    Print data with padding on left side 
"""

def pad_right(data, size, character = ' '):
    pad_string(data, size, direction = 'right padded', character = ' ')
    result = data
    if len(data) < size:
        pad_size = size - len(data)
        result = data + character * pad_size
    return result
""" Adding padding to right of a string

Args:
   data (int/float): data to be formatted
   size (int/float): size of the format space
   character (str): defaulted to single space

   Returns:
    Print data with padding on right side 
"""
