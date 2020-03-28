"""
Your input will be a string of majuscule letters. From this, create an ascii 
bar graph of the letter frequencies in that string (see samples).

Input Format: String

Constraints: Majuscule letters only
The y-axis should be right aligned, padded with spcaes. 
The maximum y value should be unpadded.

Output Format: Ascii Bar Graph
"""

import math
import os
import random
import re
import sys

alphabet = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 
        'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M':0, 'N':0, 'O':0,'P':0,'Q':0,'R':0,
        'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

def letter_frequency(s):
    """
    Update alphabet dictionary to reflect the number of times each letter 
    appears in string 's'.

    param:
        s(string): Random letters    
    """
    # GET DATA POINTS
    # Get the number of times each letter appears in s
    for key in alphabet:
        value = 0
        for char in s:    
            if char == key:
                # Letter appears in string
                value += 1
        # Add number of times letter is in s to alphabet dict
        alphabet[key] = value

def bargraph(s):   
    """
    Create a bargraph to represent the number of times a letter appears in a 
    string. The frequency is listed on the y-axis and the letters on the x-axis.
    
    For each letter there is a # from frequency to 1. 
    For any letter that doesn't appear there is a space. 

    param:
        s(string): Random letters

    return:
        string array: Lines of the bargraph stored desc order in list   
    """

    # Initialise bar graph output 
    output = []
    # Find the number of times each letter appears in s
    letter_frequency(s)

    
    # Find the max number of times letter appears (max y-axis)
    max_value = max(alphabet.values())
    # Get the number of digits for this value (spacing y-axis)
    max_num_digits = len(str(max_value))

    # Start with the max value line printed first
    current_value = max_value    
    while current_value > 0: 
        # Create line for every value from max value to 1
        out = ''
        for key in alphabet:
            # For every letter of the alphabet check if appears at 
            # least current_value times 
            if alphabet[key] == current_value:
                # Yes - add hash and minus 1 to its value for next line check
                out += '#'
                alphabet[key] -= 1                
            else:
                # No - print a space
                out += ' '
        
        # Get the number of spaces to appear before current value to align
        num_spaces = max_num_digits - len(str(current_value))
        # Create y-axis line and add to graph
        line = (f'{" " * num_spaces}{current_value}|{out}')
        output.append(line)
        
        # Go to the next value down the y-axis
        current_value -= 1
    
    # Create string of alphabet for x-axis
    alphabet_str = (max_num_digits * ' ') + '|' 
    # Create line of dashes for each letter in alphabet for x-axis
    axis = (max_num_digits * '-') + '+'
    for key in alphabet:
        axis += '-'
        alphabet_str += key
    # Add line of dashes then line of alphabet
    output.append(f'{axis}')
    output.append(alphabet_str)

    return output


# Sample input
s = 'EDTUGCUXKLKROWTLPWSANOCFMDGALKRUKONCZWLUURPATHOBHOWHHDOVXDBKLFRLFUOTHHCLRXTXGHNTCXKHHIIVILWNOHFGCXTNGFUWDINWTXGULUXJHCGTBAPDRCODNNXFMHTQKWXFIXAJRXDLXTUXXAFSOJRCNFKURWIKOONLJRCOKSDLTLQTTFOOSJTLNOOXBHQDNUHRHOKUHNDICTBILLBLRNIXGFKKKGQHUFMNFCNFAOLOBOFQXNUTUZCWTARMTOPYTWRRPXXJANUTNDNHNURKBRVXOGGNTBDDAPXWUNDBMJKTLBRJPNUDTHDBMLTBCLDTUGCUXKLKROWTLPWSANOCFMDGALKRUKONCZWLUURPATHOBHOWHHDOVXDBKLFRLFUOTHHCLRXTXGHNTCXKHHIIVILWNOHFGCXTNGFUWDINWTXGULUXJHCGTBAPDRCODNNXFMHTQKWXFIXAJRXDLXTUXXAFSOJRCNFKURWIKOONLJRCOKSDLTLQTTFOOSJTLNOOXBHQDNUHRHOKUHNDICTBILLBLRNIXGFKKKGQHUFMNFCNFAOLOBOFQXNUTUZCWTARMTOPYTWRRPXXJANUTNDNHNURKBRVXOGGNTBDDAPXWUNDBMJKTLBRJPNUDTHDBMLTBCLDTUGCUXKLKROWTLPWSANOCFMDGALKRUKONCZWLUURPATHOBHOWHHDOVXDBKLFRLFUOTHHCLRXTXGHNTCXKHHIIVILWNOHFGCXTNGFUWDINWTXGULUXJHCGTBAPDRCODNNXFMHTQKWXFIXAJRXDLXTUXXAFSOJRCNFKURWIKOONLJRCOKSDLTLQTTFOOSJTLNOOXBHQDNUHRHOKUHNDICTBILLBLRNIXGFKKKGQHUFMNFCNFAOLOBOFQXNUTUZCWTARMTOPYTWRRPXXJANUTNDNHNURKBRVXOGGNTBDDAPXWUNDBMJKTLBRJPNUDTHDBMLTBCLDTUGCUXKLKROWTLPWSANOCFMDGALKRUKONCZWLUURPATHOBHOWHHDOVXDBKLFRLFUOTHHCLRXTXGHNTCXKHHIIVILWNOHFGCXTNGFUWDINWTXGULUXJHCGTBAPDRCODNNXFMHTQKWXFIXAJRXDLXTUXXAFSOJRCNFKURWIKOONLJRCOKSDLTLQTTFOOSJTLNOOXBHQDNUHRHOKUHNDICTBILLBLRNIXGFKKKGQHUFMNFCNFAOLOBOFQXNUTUZCWTARMTOPYTWRRPXXJANUTNDNHNURKBRVXOGGNTBDDAPXWUNDBMJKTLBRJPNUDTHDBMLTBCL'

sample = bargraph(s)
mystring = '\n'.join(sample)
print(mystring)
